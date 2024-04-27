#Files
#1st program
f=open("abc.txt","w")#creating new file
#1st parameter is name of file
#2nd parameter is mode of file
f.write("This is a file")
#Writing text to file
f.close()



#2nd program
f=open("a.txt","a")#creating new file
#1st parameter is name of file
#2nd parameter is mode of file
f.write("\nHello")
#appending text to file
f.close()

Output
This is a file
Hello

#3rd program
f=open("grp.txt","r")
print(f.read())
f.close()

Output
Grp 1:
1
2
3
4

Grp 2:
1
2
3
4

#4th program
f=open("grp.txt","r")
print(f.readline(),end=" ")
print(f.readline(),end=" ")
print(f.readline(),end=" ")
print(f.readline(),end=" ")
print(f.readline(),end=" ")
f.close()

Output
Grp 1:
 1
 2
 3
 4

#5th program
#creating two files and copying content of one file to another
f1=open("grp.txt","r")
f2=open("newgrp.txt","w")
f2.write(f1.read())
f2.close()
f1.close()

Output
new file is created and the contents of first file is copied to new file

#6th program
#task1
f1=open("names.txt","w")
f1.write("Raja\nRani\nMantri\nPolice\n")
f1=open("names.txt","r")
print(f1.read())
f1.close()
f2=open("newnames.txt","w")
f1=open("names.txt","r")
f2.write(f1.read())
f2=open("newnames.txt","r")
print(f2.read())
f2.close()
f1.close()


#7th program
#task-2
f1=open("Rollnumbers.txt","w")
f1.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")
f1.close()
f1=open("Rollnumbers.txt","r")
print(f1.readline(),end=" ")
print(f1.readline(),end=" ")
print(f1.readline(),end=" ")
print(f1.readline(),end=" ")
f1.close()

f2=open("Specialstudents.txt","w")
f1=open("Rollnumbers.txt","r")
f1.readline()#just moving the pointer to next line
f2.write(f1.readline())
f2.write(f1.readline())
f2.write(f1.readline())
f2.write(f1.readline())
f2.write(f1.readline())
f2.close()
f1.close()

f2=open("SpecialStudents.txt","r")
print(f2.read())
f2.close()

f3=open("otherlist.txt","w")
f1=open("Rollnumbers.txt","r")
f3.write(f1.readline())
f1.readline()
f3.write(f1.readline())
f1.readline()
f3.write(f1.readline())
f1.readline()
f3.write(f1.readline())
f1.readline()
f3.write(f1.readline())
f1.readline()
f1.close()
f3.close()

f3=open("otherlist.txt","r")
print(f3.read())
f3.close()
