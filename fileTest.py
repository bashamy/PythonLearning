fileLoc = 'C:\\Users\\abdul.yousuf\\Desktop\\'
fileName = "Test_File.txt"

read_file = open(fileLoc+fileName,"r")
print(read_file.readable())
read_file.close()

write_file = open(fileLoc+fileName,"a+")
write_file.writelines("\nIbrahim - 7")
write_file.close()

read_file = open(fileLoc+fileName,"r")
print(read_file.read())
read_file.close()