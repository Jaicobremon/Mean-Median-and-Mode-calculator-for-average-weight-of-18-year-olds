#Importing modules
from collections import Counter
import csv

#Opening csv file and converting into list
with open("SOCR-HeightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)

#Creating two variables to hold data
new_data1 = []

#For lopps to calculate totals of both lists
for i in range(len(file_data)):
    n_num1 = file_data[i][2]
    new_data1.append(float(n_num1))
    n1 = len(new_data1)

#Variables of total of each list
total1 = 0

#Calculating both totals
for x in new_data1:
    total1 += x



#Calculating both averages
mean1 = total1/n1


#Printing both averages
print("The mean/average of the weight(pounds) is -> " + str(mean1))


new_data1.sort()


if n1 % 2 == 0:
    #getting the first number
	median1 = float(new_data1[n1//2])
    #getting the second number
	median2 = float(new_data1[n1//2 - 1])
    #getting mean of those numbers
	median01 = (median1 + median2)/2
else:
	median01 = new_data1[n1//2]



print("The median of weight(pounds) is -> " + str(median01))


data = Counter(new_data1)
mode_data_for_range = {
                        "75-85": 0,
                        "85-95": 0,
                        "95-105": 0,
                        "105-115":0,
                        "115-125":0,
                        "125-135":0,
                        "135-145":0,
                        "145-155":0,
                        "155-165":0,
                        "165-175":0,
                    }
for height, occurence in data.items():
    if 75 < float(height) < 85:
        mode_data_for_range["75-85"] += occurence
    elif 85 < float(height) < 95:
        mode_data_for_range["85-95"] += occurence
    elif 95 < float(height) < 105:
        mode_data_for_range["95-105"] += occurence
    elif 105 < float(height) < 115:
        mode_data_for_range["105-115"] += occurence
    elif 115 < float(height) < 125:
        mode_data_for_range["115-125"] += occurence
    elif 125 < float(height) < 135:
        mode_data_for_range["125-135"] += occurence
    elif 135 < float(height) < 145:
        mode_data_for_range["135-145"] += occurence
    elif 145 < float(height) < 155:
        mode_data_for_range["145-155"] += occurence
    elif 155 < float(height) < 165:
        mode_data_for_range["155-165"] += occurence
    elif 165 < float(height) < 175:
        mode_data_for_range["165-175"] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode1 = float((mode_range[0] + mode_range[1]) / 2)

print(f"The mode of the weight(pounds) is -> {mode1:2f}")
