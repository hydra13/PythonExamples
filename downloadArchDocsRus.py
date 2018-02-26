import urllib.request
from bs4 import BeautifulSoup
import sys
from xhtml2pdf import pisa
import os
import threading
import time

ignoringDict = {
	'Page information':'',
	'Log in':'',
	'Read':'',
	'View source':'',
	'View history':'',
	'Create account':'',
	'Русский':'',
	'Privacy policy':'',
	'Disclaimers':'',
	'About ArchWiki':'',
	'GNU Free Documentation License 1.3 or later':'',
	'Discussion':'',
	'Help':'',
	'What links here':'',
	'Page':'',
}

usedTextDict = {}
usedLinkDict = {}

class AsyncTimer(threading.Thread):
	def __init__(self, pdf_path, link):
		threading.Thread.__init__(self)
		self.pdf_path = pdf_path
		self.link = link

	def SaveToPdf(self, pdf_path, link):
		try:
			os.remove(pdf_path)
		except OSError:
			pass

		page = urllib.request.urlopen(link).read().decode('UTF-8')
		page = page.replace("</head>", "<style>@font-face {font-family: \"Verdana\";src: url(\"d:/verdana.ttf\");}html {font-family: \"Verdana\";font-size: 11pt;}</style></head>")
		resultFile = open(pdf_path, "w+b")
		pisaStatus = pisa.CreatePDF(
				page,
				dest=resultFile,
				encoding='UTF-8')
		resultFile.close()
		return pisaStatus.err

	def run(self):
		SaveToPdf(self.pdf_path, self.link)
		time.sleep(2)
		fileName = self.pdf_path
		fileName = fileName.replace("d:/archDoc/", "")
		print("File downloaded: " + fileName)

def Main():
	path = "https://wiki.archlinux.org/index.php/Table_of_contents_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)"
	links,names = GetLinks(path)
	# pdf_path = "d:/test.pdf"
	pdf_path = "d:/archDoc/"
	num = 0
	max_level = 3

	DownloadLinks(links, names, pdf_path, "0.", 0, max_level)

	print("--- Downloading complete! ---")

def DownloadLinks(links, names, pdf_path, num, level, max_level):
	lnum = 0
	pos = -1
	bgThreads = []
	for link in links:
		pos += 1
		if (level == 0):
			if (link.find('/index.php/Category:%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9') != -1):
				continue
			if (link.find('Category') == -1):
				continue
		lnum += 1
		file_name = num+str(lnum)+ " " + names[pos] + ".pdf"
		bgThread = AsyncTimer(pdf_path+file_name, 'https://wiki.archlinux.org'+link)
		bgThreads.append(bgThread)
		bgThread.start()
		if (level < max_level):
			sub_links,sub_names = GetLinks("https://wiki.archlinux.org"+link)
			DownloadLinks(sub_links, sub_names, pdf_path, num+str(lnum)+".", level+1, max_level)
	for thread in bgThreads:
		thread.join()

def GetLinks(path):
	links = []
	names = []
	print('Start to get russian links')
	try:
		page = urllib.request.urlopen(path).read().decode('UTF-8')
	except:
		return links,names

	soup = BeautifulSoup(page, 'html.parser')

	for link in soup.find_all('a'):
		if link.has_attr('href'):
			string = link.get('href')
			text = link.get_text()
			if (string.find('%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9') != -1 and len(text) > 1 and (text not in ignoringDict) and (text not in usedTextDict) and (string not in usedLinkDict)):
				links.append(string)
				names.append(text)
				usedTextDict[text]=''
				usedLinkDict[string]=''
	print('End to get russian links. Count: '+str(len(links)))
	return links,names

def SaveToPdf(pdf_path, link):
	try:
		os.remove(pdf_path)
	except OSError:
		pass

	page = urllib.request.urlopen(link).read().decode('UTF-8')
	page = page.replace("</head>", "<style>@font-face {font-family: \"Verdana\";src: url(\"d:/verdana.ttf\");}html {font-family: \"Verdana\";font-size: 11pt;}</style></head>")
	page = page.replace("src=\"/images/", "src=\"https://wiki.archlinux.org/images/")
	resultFile = open(pdf_path, "w+b")
	pisaStatus = pisa.CreatePDF(
            page,
            dest=resultFile,
            encoding='UTF-8')
	resultFile.close()
	return pisaStatus.err

if __name__ == '__main__':
	Main()
	
