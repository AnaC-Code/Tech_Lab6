#importing pandas library
import pandas as pd
import matplotlib.pyplot as plt

#reading in the datafile 
df = pd.read_csv('/Users/bugracantufan/Documents/GitHub/Tech_Lab6/Clean_Data.csv', encoding='ISO-8859–1')
    #'encoding='ISO-8859–1' gets rid of 'UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 2786: invalid start byte'

#Pie-Chart / City
df['City'].value_counts().plot.pie()
plt.show()
    #does not look good because aof too much values

#Pie-Chart / State
df['State'].value_counts().plot.pie()
plt.show()
    #does not look good because aof too much values

#Pie-Chart / Region
df['Region'].value_counts().plot.pie()
plt.show()
    #looking good 

#GONNA LOOK FOR A BETTER VISIALISATION METHOD FOR CITY AND STATE!!! 
#DOES NOT LOOK NICE WITH THIS MUCH OF VALUES   