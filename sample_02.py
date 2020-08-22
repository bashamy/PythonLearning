file_loc_in = 'C:\\Users\\abdul.yousuf\\Desktop\\DumpHere\\Python_Files\\02\\'
out_file1 = "file_com1.txt"
out_file2 = "file_com2.txt"


with open(file_loc_in+"file1.txt", 'r') as f1:
    list1 = f1.readlines()
print(list1)

with open(file_loc_in+"file2.txt", 'r') as f2:
    list2 = f2.readlines()
print(list2)


with open(file_loc_in + out_file1, "a") as f3:
    for a in list1:
        c=0
        for b in list2:
            if a in b:
                c=c+1
        if c==0:
            f3.writelines(a)

'''    
    for a, b in zip(list1, list2):
        if a.strip() not in b:
            f3.writelines(a)
'''