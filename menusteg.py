import mystegrar as msr
import mystegpyth as msp
try:
	ch=int(input('Do you want to compress the file using winrar or python ?\n1. Winrar\n2. Python\nEnter your choice:: '))
	if ch==1:
		msr.mainsteg()
	elif ch==2:
		msp.mymainsteg()
	else:
		pass
except Exception as e:
	print(str(e))
finally:
	input('Exit')