from matplotlib import pyplot as plt
import pandas as pd


data = pd.read_excel(r'/Users/jannitselekoglou/Desktop/convertpy/test.xlsx')


x = []
y = []

x = list(data["Bauteil "])
y = list(data["Maße x"])


plt.plot(x,y)
plt.show()
