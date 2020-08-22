import pandas as pd
import operator

file_loc_in = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\01\\IN\\'
file_loc_out = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\01\\OUT\\'
fileToRead = "Input_File.txt"
fileToWrite ="Output_File"

#file_data = pd.read_csv(file_loc_in + fileToRead, delimiter=None, header=None, engine='python')
file_data = pd.read_csv(file_loc_in + fileToRead, delimiter="NoValue", header=None, engine='python')

new_fd1 = file_data

lst = new_fd1[new_fd1[0].str.contains('{/')].index+1
end_tag_index = list(lst)
#print(end_tag_index)
#print(end_tag_index[1:])
check = 0
prev_index = 0

if len(end_tag_index) == 1:
    test_df = new_fd1[prev_index:]
    test_df.to_csv(file_loc_out + fileToWrite + "_1" + ".txt", index=False, header=False)
else:
    #end_tag_index = end_tag_index[1:]
    for i in end_tag_index:
        test_df = new_fd1[prev_index:i]
        #test_df.to_csv(file_loc_out + fileToWrite + "_" + str(i)+".txt", index=False)
        test_df.to_csv(file_loc_out + fileToWrite + "_" + str(i) + ".txt", index=False, header=False)
        prev_index = i
