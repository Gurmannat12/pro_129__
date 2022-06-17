import csv
dataset_1 = []
dataset_2 = []

with open("star.csv", "r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open("dwarf_star.csv", "r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
star_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
star_data = []
for index, data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index] + star_data_2[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

with open('merged_dataset.csv') as input, open('merged_dataset1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)