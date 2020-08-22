file_loc_in = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\02\\'
out_file1 = "file_com1.txt"
out_file2 = "file_com2.txt"


with open(file_loc_in+"Before.csv", 'r') as f1:
    list1 = f1.readlines()

with open(file_loc_in+"After.csv", 'r') as f2:
    list2 = f2.readlines()

with open(file_loc_in + out_file1, "a") as f3:
    for a in list1:
        c=0
        for b in list2:
            if a in b:
                c=c+1
        if c==0:
            f3.writelines(a)

with open(file_loc_in + out_file2, "a") as f4:
    for b in list2:
        c=0
        for a in list1:
            if b in a:
                c=c+1
        if c==0:
            f3.writelines(b)