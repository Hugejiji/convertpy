import matplotlib.pyplot as plt, numpy as np
from data import csvtransfer

k = csvtransfer()
totalmedals, top_ranked, countrys_total, goldmedals, silvermedals, bronzemedals = k.load_data(11)

width = 0.6
fig, ax = plt.subplots()
ind = np.arange(len(top_ranked))

totalmedals = sorted(totalmedals)
dict(sorted(countrys_total.items(), key=lambda item: item[1]))
ax.barh(ind, totalmedals , width)
ax.set_xlabel("Country")
ax.set_ylabel("Total Number")
ax.set_yticks(ind , list(countrys_total))

plt.show()









