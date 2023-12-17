import pandas as pd
import openpyxl as op
# import numpy as np
# import pylab as pl

class first_draft:
    dataframe1 = pd.read_excel("periods.xlsx")
    fo = open("periods.xlsx", "r")
    #print(dataframe1)
    
    # Using pd.DataFrame.mean() method to get average cycle length
    pd.DataFrame(dataframe1, columns = "C")
    avg = dataframe1["C"].mean()
    print(avg)

    # periods.xlsx["C"].mean()


first_draft()


