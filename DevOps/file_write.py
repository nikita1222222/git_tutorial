#Write a file
# Write a program to create a text file and write some content to it.


#Opened text.txt file with read mode
f = open("text.txt", 'r+') 

 # Will read all lines in the file
f.readline()     

#write data which we want to write 
f.write("\nLittle knowledge is very very dangerous thing") 

#close the file
f.close()