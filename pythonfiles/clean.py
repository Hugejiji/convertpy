import csv
names =[]
with open("Athletes.csv", "r") as file:
  reader = csv.DictReader(file)
  next(reader)

  for row in reader:
    print(row["Name"])



  #for row in reader:
  #  if row[0].upper() in names:
  #    next(reader)
  #  else:
  #    names.append(row[0].upper())

#print(names)

