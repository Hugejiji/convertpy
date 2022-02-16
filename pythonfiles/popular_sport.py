import csv , matplotlib.pyplot as plt, numpy as np
rank = 300
countrys = []
disciplines = {}
rankings = {}


#load data into lists for matplotlib
with open("archive/Athletes.csv", "r") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #crate Dict with Discipline and number of participence
    discipline = row["Discipline"] 
    if not discipline in disciplines:
      disciplines[discipline]  = 1
    disciplines[discipline] += 1
    #Make List of every country
    country = row["NOC"]
    if country not in countrys:
      countrys.append(country)

#getting rid of disciplines with under 50 particpince
for i in disciplines:
  if disciplines[i] > rank:
    rankings[i] = disciplines[i]



#Plotting Data with Matplot
catogories = list(rankings.keys())
values = list(rankings.values())

fig, ax = plt.subplots()

ax.bar(catogories, values)
ax.set_xlabel("Categories")
ax.set_ylabel("Number of participants")
ax.set_title("Most Popular Activity in the Summer Olympics")

plt.show()
  
