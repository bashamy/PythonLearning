file_loc_in = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\02\\'
out_file1 = "file_compare1.txt"
out_file2 = "file_compare2.txt"

file1 = open(file_loc_in+"file1.txt").readlines()
file1_line = []
for lines in file1:
    file1_line.append(lines)

file2 = open(file_loc_in+"file1.txt").readlines()
file2_line = []
for lines in file2:
    file2_line.append(lines)

def files_compare():
    for x in range(len(file1)):
        a = 0
        y = 0
        for y in range(len(file2)):
            if file1_line[x] == file2_line[y]:
                a = a+1
                y = len(file2)
        if a == 0:
            write_file = open(file_loc_in + out_file1, "a+")
            write_file.writelines(file1_line[x])
            write_file.close()

    for y in range(len(file2)):
        a = 0
        x = 0
        for x in range(len(file1)):
            if file1_line[x] == file2_line[y]:
                a = a+1
                x = len(file1)
        if a == 0:
            write_file = open(file_loc_in + out_file2, "a+")
            write_file.writelines(file2_line[y])
            write_file.close()

files_compare()