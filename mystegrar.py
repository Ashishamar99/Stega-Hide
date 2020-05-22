import sys
import os

def takeinp():
	'''
	#checking if the number of args is correct, we will need 3 arguments, prg.py img file
	if len(sys.argv)!=3:
		input("Enter image name and file name please (with extention)")
	#if we have 3 args, we will proceed with the steg operation
	myimg=sys.argv[1] #getting the image name
	myfilefol=sys.argv[2] #getting the filename/foldername
	myimgext=myimg.split(".")[1] #fetching the extention for o/p file
	'''
	mytempimg=input("Enter image name with extension: ") #getting the image name
	mytempfilefol=input("Enter file or folder name: ") #getting the filename/foldername
	mytempimgext=mytempimg.split(".")[1] #fetching the extention for o/p file
	return mytempimg,mytempfilefol,mytempimgext

def mainsteg():
	myimg,myfilefol,myimgext=takeinp()

	def checkrarexec():
		if 'Rar.exe' in os.listdir():pass #if rar file exists then do nothing
		else:
			#raise Exception('checking checkrarexec')
			#copying the Rar.exe file from WINRAR if installed
			dest=os.getcwd()+'\\'
			src='C:\\Program Files\\WinRAR\\Rar.exe'
			os.popen(f'copy "{src}" "{dest}"')

	def createrar(myfilefol):
		myrarfile=''
		myfilefolname=myfilefol.split('.')[0]
		#print(myfilefolname,myfilefol)
		os.system(f'Rar.exe -r a {myfilefolname} {myfilefol}') #Running command Rar.exe -r a file file
		#checking if rar file exists else, raise an exception
		myrarfile=f'{myfilefolname}.rar'
		if myrarfile in os.listdir():pass
		else:raise Exception("Rar file not created")
		return myrarfile

	def performsteg():
		myout=input("Enter the output file name\n<If you want to skip this press 'Enter' Key>: ") #fetching o/p file name
		if myfilefol.endswith('.rar'):myrarfile=myfilefol
		else:myrarfile=createrar(myfilefol)
		#executing the command with output image having the same extention as the input image
		if myout=='':myout='out'
		os.system(f'copy /b {myimg} + {myrarfile} {myout}.{myimgext}') #command used = copy /b img.jpg + file.rar out.jpg
		listdirop=os.popen('dir').read()
		if f'{myout}.{myimgext}' in listdirop:
			print(f'Success, output file name is {myout}.{myimgext}')

	try:
		#takeinp()
		checkrarexec()
		performsteg()
	except Exception as e:
		if 'Rar.exe' not in os.listdir():
			print("Rar file missing")
		else:
			print(str(e))

if __name__=='__main__':
	mainsteg()
	input('Exit')