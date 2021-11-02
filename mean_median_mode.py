import csv
from collections import Counter

# mean
with open(r"C:\Users\bhuvi\Google Drive\WHJr\Python\Project 104 - Mean, Median, Mode\height-weight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][2]
	new_data.append(float(n_num))
n = len(new_data)
total = 0
for x in new_data:
    total += x

mean = round(total / n)
print("Mean / Average is: " + str(mean))

# median
with open(r'C:\Users\bhuvi\Google Drive\WHJr\Python\Project 104 - Mean, Median, Mode\height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][2]
	new_data.append(n_num)

n = len(new_data)
new_data.sort()

if n % 2 == 0:
	med1 = float(new_data[n//2])
	med2 = float(new_data[(n//2)+ 1])
	median = (med1 + med2)/2
else:
	median = new_data[round(n/2)]

print("Median is: " + str(median))

# mode
with open(r'C:\Users\bhuvi\Google Drive\WHJr\Python\Project 104 - Mean, Median, Mode\height-weight.csv', newline='') as f:
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
                        "115-125": 0,
                        "125-135": 0,
                        "135-145": 0
                    }
for weight, occurence in data.items():
    if 115 < float(weight) < 125:
        mode_data_for_range["115-125"] += occurence
    elif 125 < float(weight) < 135:
        mode_data_for_range["125-135"] += occurence
    elif 135 < float(weight) < 145:
        mode_data_for_range["135-145"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")