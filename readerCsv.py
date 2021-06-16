import csv
with open('births.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    print(csv.field_size_limit())
    lineCount = 0

    for row in csv_reader:
        print("I am Csv File")
        if(row[3] == 'F'):

          print(lineCount)
          print(row[3])
        lineCount = lineCount +1




