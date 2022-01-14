import csv
from collections import Counter
with open('data1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
anylist = []
for i in range(len(file_data)):
    num = file_data[i][2]
    anylist.append(float(num))
n = len(anylist)
total = 0
for i in anylist:
    total += i
mean = total/n
print("MEAN: "+str(mean))


anylist.sort()
if n % 2 != 0:
    median = anylist[int((n+1)/2)]
else:
    median = (anylist[int((n)/2)]+anylist[(int((n)/2))+1])/2
print("MEDIAN: "+str(median))


data = Counter(anylist)
mode = {
    "90-100": 0, "100-110": 0, "110-120": 0, "120-130": 0, "130-140": 0, "140-150": 0, "150-160": 0
}
for height, occurence in data.items():
    if float(height) >= 90 and float(height) < 100:
        mode["90-100"] += occurence
    elif float(height) >= 100 and float(height) < 110:
        mode["100-110"] += occurence
    elif float(height) >= 110 and float(height) < 120:
        mode["110-120"] += occurence
    elif float(height) >= 120 and float(height) < 130:
        mode["120-130"] += occurence
    elif float(height) >= 130 and float(height) < 140:
        mode["130-140"] += occurence
    elif float(height) >= 140 and float(height) < 150:
        mode["140-150"] += occurence
    elif float(height) >= 150 and float(height) < 160:
        mode["150-160"] += occurence

modeRange, modeOccurrence = 0, 0
for range, occurrence in mode.items():
    if occurrence > modeOccurrence:
        modeRange, modeOccurrence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurrence
Mode = float((modeRange[0]+modeRange[1])/2)
print("MODE: "+str(Mode))
