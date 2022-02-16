import csv

class csvtransfer():
  def load_data(self,rank):
    totalmedals = []
    goldmedals = []
    silvermedals = []
    bronzemedals = []
    top_ranked = []
    with open("archive/medals_total.csv", "r") as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        if int(row["Rank"]) < rank:
          top_ranked.append(row["Country Code"])
          totalmedals.append(int(row["Total"]))
          goldmedals.append(int(row["Gold Medal"]))
          silvermedals.append(int(row["Silver Medal"]))
          bronzemedals.append(int(row["Bronze Medal"]))
      return totalmedals, top_ranked, goldmedals, silvermedals, bronzemedals
