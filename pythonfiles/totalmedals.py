import matplotlib.pyplot as plt, numpy as np
from data import csvtransfer

k = csvtransfer()
totalmedals, top_ranked, goldmedals, silvermedals, bronzemedals = k.load_data(5)

width = 0.3
fig, ax = plt.subplots()
ind = np.arange(len(top_ranked))

ax.bar(ind , totalmedals, width)
ax.set_xlabel("Country")
ax.set_ylabel("Total Number")
ax.set_xticks(ind , top_ranked)

plt.show()









