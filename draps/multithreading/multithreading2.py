import threading
import time

class AsyncTimer(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out

	def run(self):
		f = open(self.out, 'a')
		f.write(self.text + "\n")
		f.close()
		time.sleep(2)
		print("Finished Background Write To File " + self.out)

def Main():
	message = input("message:")
	bgThread = AsyncTimer(message, "out.txt")
	bgThread.start()

	print("Wait writing...")
	bgThread.join()
	print("End main")

if __name__ == '__main__':
	Main()
