import webbrowser
import time

total_breaks = 3
break_count = 0

print("The program started on " + time.ctime())
while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("http://www.infobae.com/")
	break_count = break_count + 1