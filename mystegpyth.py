import zipfile
import mystegrar as ms
import os
import shutil
def mymainsteg():
	myimg,myfilefol,myimgext=ms.takeinp()

	#creating a zip file
	def createzip(myfilefol):
		#if given file is already a zip file then return that, else create one zip file and return that
		myzipfilename=''
		if myfilefol.endswith('.zip'):
			return myfilefol
		else:
			if '.' in myfilefol:
				myzipfilename=myfilefol.split('.')[0]+'.zip' #to AVOID file.txt.zip as output zip name
			else:myzipfilename=f'{myfilefol}.zip'
			if os.path.isdir(f'{os.getcwd()}\\{myfilefol}'):
				shutil.make_archive(myfilefol,'zip',myfilefol)
			else:
				mycompfile=zipfile.ZipFile(myzipfilename,'w')
				mycompfile.write(myfilefol,compress_type=zipfile.ZIP_DEFLATED)
				mycompfile.close()
			return myzipfilename

	def dosteg():
		myoutfile=input("Enter the output file name\n<If you want to skip this press 'Enter' Key>: ") #fetching o/p file name
		myzipfile=createzip(myfilefol) #fetch the name of zipfile
		#executing the command with output image having the same extention as the input image
		if myoutfile=='':myoutfile='out'
		os.system(f'copy /b {myimg} + {myzipfile} {myoutfile}.{myimgext}') #command used = copy /b img.jpg + file.zip out.jpg
		listdirop=os.popen('dir').read()
		if f'{myoutfile}.{myimgext}' in listdirop:
			print(f'Success, output file name is {myoutfile}.{myimgext}')

	try:
		dosteg()
	except Exception as e:
		print(str(e))
	finally:
		pass
		#input('Exit') #Don't need to write this cuz we're importing mysteg and that has input('exit') which will be used 
if __name__=='__main__':
	mymainsteg()