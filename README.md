# Steg-Hide
Steganography is the art of concealing a file or a message within another file.
- This program takes in 2/3 inputs (3rd input is optional). The first input is the name of the superficial file and the second input is the name of the file you want to hide. The third input is the name of the final file (if not entered. the program will name it "out" with the appropriate extention).
- The user is presented with 2 choices, to compress the file to be hidden using winrar or python. If winrar is installed using the default path, the program will use the winrar's executable file to compress the file. 
- If the user wants to compress the file using python then using the default modules of python the file will be compressed. 
- The steganographic operation is done using the copy command (Windows) and the final file is generated along with the compressed file in both the cases. 
- It is important to note that for this program to work you will need to have the files in the same folder as the program and also that you provide the file names with correct extensions.



**To run the program - python menusteg.py**

**Note - To open the hidden compressed file, open the final image file with a compression software such as winzip/winrar/peazip/7zip and extract it to a specified location.**
