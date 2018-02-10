import threading
import time

def timer(name, delay, repeat):
	print("Start timer: ", name)
	while True:
		time.sleep(delay)
		print(name+": repeat="+str(repeat)+"; time="+str(time.ctime(time.time())))
		repeat -= 1
		if (repeat <=0):
			break
	print("End timer: ", name)

def Main():
	print("Main start")
	t1 = threading.Thread(target=timer, args=("Timer1",1,5))
	t2 = threading.Thread(target=timer, args=("Timer2",2,5))
	t1.start()
	t2.start()
	print("Main end")

if __name__ == '__main__':
	Main()