import csv, matplotlib.pyplot as plt, numpy as np
rank = 10

#create loading function for required Data
#bring it into right shape for ploting it 
def load_data(rank):
  goldmedals = []
  silvermedals = []
  bronzemedals = []
  top_ranked = []
  with open("archive/medals_total.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if int(row["Rank"]) < rank:
        top_ranked.append(row["Country Code"])
        goldmedals.append(int(row["Gold Medal"]))
        silvermedals.append(int(row["Silver Medal"]))
        bronzemedals.append(int(row["Bronze Medal"]))
    return goldmedals, silvermedals, bronzemedals, top_ranked

#bind return to a value 
goldmedals, silvermedals,bronzemedals,top_ranked = load_data(rank)
width = 0.3
ind = np.arange(len(top_ranked))
fig, ax = plt.subplots()

#bar for goldmedals
#ax.bar(ind + width, goldmedals, width, label="Gold Medals")

#bar for silvermedals
#ax.bar(ind, silvermedals, width, label="Silver Medals")


#barhorizontel for goldmedals
ax.barh(ind, goldmedals, width, label="Gold Medals")

#barhorizontel for silvermedals
ax.barh(ind + width, silvermedals, width, label="Silver Medals")

#bar for bronzemedals
#ax.barh(ind + 2*width, bronzemedals, width, label="Bronze Medals")

#title,xlabel,ylabel
ax.set_title("Gold vs Silvermedals")
ax.set_ylabel("Country")
ax.set_xlabel("Amount of Medals")
ax.set_yticks(ind + width/2, top_ranked)
ax.legend()

plt.show()



