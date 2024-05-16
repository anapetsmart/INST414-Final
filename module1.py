import json
import statistics
with open("breast_cancer.json", "r") as token:
    data = token.read()
data_list = json.loads(data)
sort = sorted(data_list, key=lambda x: x['radius_mean'], reverse=True)
mal_list = []
benign_list = []
count = 0
for i in sort:
    if data_list[count]['diagnosis'] == 'B':
        benign_list.append(i)
    else:
        mal_list.append(i)
    count += 1
rad_benign_list = []
for i in benign_list:
    rad_benign_list.append(i['radius_mean'])
rad_mal_list = []
for i in mal_list:
    rad_mal_list.append(i['radius_mean'])
print(f"Benign Radius Mean: {sum(rad_benign_list)/len(rad_benign_list)}")
print(f"Malignant Radius Mean: {sum(rad_mal_list)/len(rad_mal_list)}")
print(f"Benign Standard Devation: {statistics.stdev(rad_benign_list)}")
print(f"Malignant Standard Deviation: {statistics.stdev(rad_mal_list)}")
print(f"Benign Highest Value: {rad_benign_list[0]:}")
print(f"Malignant Highest Value: {rad_mal_list[0]}")
print(f"Benign Smallest Value: {rad_benign_list[-1]}")
print(f"Malignant Smallest Value: {rad_mal_list[-1]}")

