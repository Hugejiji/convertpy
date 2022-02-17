import csv, matplotlib.pyplot as plt, numpy as np, pandas as pd 
from matplotlib.ticker import MaxNLocator

disciplines = {}
counter = {}
country = "Greece"
k = {}
def loaddata():
  with open("archive/Athletes.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row["NOC"]== country:
        discipline = row["Discipline"]
        if discipline not in disciplines:
          disciplines[discipline] = 1
        disciplines[discipline] += 1
        counter[discipline] = disciplines[discipline]  

      for i in counter:
        if counter[i] > 5:
          k[i] = disciplines[i]
    return k

data = loaddata()
fig, ax = plt.subplots()
numbers = data.keys()
activity = data.values()


ax.bar(numbers, activity, width=0.8, color=["blue"])
#Set bar to only integers
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel("Sport Categorie")
ax.set_ylabel("Participants")
ax.set_title(country)

plt.show()





        



