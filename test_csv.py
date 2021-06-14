import csv

def read_csv(filename):
    lines = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            lines.append(line)
    return lines


inputs = read_csv('submission2.csv')

inputs = inputs[1:] # skip header

print(inputs) 
print(len(inputs))

seriesuids = []
labels = []
for i in range(len(inputs)):
    seriesuid = inputs[i][0]
    label = inputs[i][1]

    print(seriesuid)
    print()
    print(label)