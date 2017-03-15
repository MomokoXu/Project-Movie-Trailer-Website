import time
import webbrowser

total_count = 3;
break_count = 0;

while break_count < total_count:
	time.sleep(2)
	webbrowser.open("https://www.youtube.com/watch?v=ZgnClGC8-WQ")
	break_count += 1
