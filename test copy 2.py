import os
import csv

working_dir = r"C:\Users\r-kajihara\Documents\Python\Versatilel_VirEnv\test"
file_name = "01.brs"
each_file = os.path.join(working_dir, file_name) 
save_file = os.path.join(working_dir, "01save.brs") 
with open(each_file, "r", encoding="SHIFT-JIS") as file_data:
#    r1 = file_data.read()
#    r2 = file_data.readline()
    r3 = file_data.readlines()

data_length = r3[174]
print(r3[int(data_length)])

with open(save_file, mode="w", encoding="SHIFT-JIS") as new_file:
    new_file.writelines(r3)
