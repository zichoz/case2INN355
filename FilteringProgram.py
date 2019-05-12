import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print ("satan")

def load_data_pandas(filename):
    DataFrame = pd.read_csv(filename, encoding='cp1252')   #Creates a dataframe of the data read by the read_csv()
    return DataFrame




df = load_data_pandas("BPI_Challenge_2019.csv")
dftest = load_data_pandas("BPI_Challenge_2019.csv")
#print(df)
newdf = df["case Item Category"]

#for x in df:
 #   print(x)
is_3way = df["case Item Category"] == "3-way match, invoice after GR"
#newdf11 = df.filter(like="3-way match, invoice after GR", axis=0) #filter out the threeway matching invoice after GR
filtered3Way = df[is_3way]
filtered3Way = filtered3Way.set_index('eventID')

filterOutDate = filtered3Way["event time:timestamp"].str.contains("2018") #filter the date
filtered3Way = filtered3Way[filterOutDate]
#filtered3Way = filtered3Way[filfiterOutDate]
print(filtered3Way)
#print(filtered3Way["event User"])
#print(process_category_User_0)
filtered3Way.to_csv("BPI_ChallengeFull_with_Dates.csv")