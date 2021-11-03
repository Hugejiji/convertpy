import csv
names = []

with open("Athletes.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    names.append(row["Name"].strip(" ").lower())

only_lastname = {}


#Take last names and count them to see whats most commen last name
def sort_lastname(names):
  for i in sorted(names):
    i = i.split()
    if i[0] in only_lastname:
      only_lastname[i[0]] +=1
    else:
      only_lastname[i[0]] = 1

  return only_lastname

#Lambdas ist abhäning von welcher funktion man quasi eingibt, da ich .values() mache gibt es dem entsprechend auch nur einen wert der resutliert, daher soll lambda kv als input nehmen und kv returnen. 


#sorted_x = sorted(sort_lastname(names).values(), key=lambda kv: kv, reverse=True)
#print(sorted_x)


# Json to get indent in output 
#json_x = json.dumps(sorted_x, indent=2)
#print(json_x)

sorted_x = sorted(sort_lastname(names).items(), key=lambda kv: kv[1], reverse=False)
print(sorted_x)

