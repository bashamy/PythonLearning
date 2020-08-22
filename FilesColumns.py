import pandas as pd
import operator

file_loc_in = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\01\\IN\\'
file_loc_out = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\01\\OUT\\'
fileToRead = "Input_File.txt"
fileToWrite1 ="Output_File_Comma"
fileToWrite2 ="Output_File_Tab"
my_list = []
for i in range(40):
    val = "col"+str(i+1)
    my_list.append(val)

file_data = pd.read_csv(file_loc_in + fileToRead, delimiter=":", names=my_list, engine='python')
new_fd1 = file_data
#print(new_fd1.head(5))
new_fd1.to_csv(file_loc_out + fileToWrite1 + ".csv", index=False, header=True)
new_fd1.to_csv(file_loc_out + fileToWrite2 + ".txt", sep='\t', index=False, header=True)