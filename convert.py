# TODO


# write programm that takes exe files as inputs and puts out visualiszed data
# all with gui ofc



# Step1: load files into memory and proceed
# Gui for Step1
# Visiuzialize Data and Ouptut them 
# Drag and drop file gui 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel (r'/Users/jannitselekoglou/Desktop/convertpy/test.xlsx')
print(df)



# Time series 


df.plot(x="Bauteil", y="Maße x")
plt.show()

