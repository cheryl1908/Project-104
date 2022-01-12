# Python program to print
# mode of elements
from collections import Counter
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][2]
	new_data.append(n_num)

#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for weight, occurence in data.items():
    if 50 < float(weight) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(weight) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(weight) < 80:
        mode_data_for_range["70-80"] += occurence
