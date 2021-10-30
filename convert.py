# TODO
# write programm that takes exe files as inputs and puts out visualiszed data
# all with gui ofc
# Thx geohotz for this nice looking commant text
# Step1: load files into memory and proceed
# Gui for Step1
# Visiuzialize Data and Ouptut them 
# Drag and drop file gui
# fucking implement a gui with tinker and learn more abotu matoplot and pandas 

import sys 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
  try: 
    input_file = sys.argv[1]
    df = pd.read_excel(input_file)
    x = []
    y = []
    name = list(df["Bauteil"])
    x = list(df["Maße x"])
    y = list(df["Maße y"])
    z = list(df["Maße z"])


    plt.plot(name,x,y,z)  
    plt.ylabel("Bauteile")  
    plt.xlabel("Maße")
    plt.show()
  except: 
    print("Usage: python3 convert.py + Filename")


if __name__ == "__main__": 
  main()

