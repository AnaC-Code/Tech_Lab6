#importing pandas library
import pandas as pd

#reading in the datafile 
df = pd.read_csv('Data/superstore_final_dataset.csv', encoding='ISO-8859–1')
    #'encoding='ISO-8859–1' gets rid of 'UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 2786: invalid start byte'

#shows the first 5 rows of the Data 
df.head()

#info about the Dataframe
df.info()
    #3 different Data-Types: float / int / object 
    #no NaN in the dataset
    #18 Columns
    #9800 rows 

df['Order_ID'].value_counts()
    #4922 different ID's 

df['Order_Date'].value_counts()
    #total length: 1230 
    #top5: 5/9/2017 - 38; 10/11/2017 - 35; 2/12/2018 - 34; 1/12/2018 - 34; 2/9/2018 - 33;

df['Ship_Mode'].value_counts()
    #4 modes (Standard/Second/First/Same day)
    
df['Customer_ID'].value_counts()
    #793 costumer 
    #Top5: WB-21850 - 35; MA-17560 - 34; PP-18955 - 34; JL-15835 - 33; CK-12205 - 32;

df['Segment'].value_counts()
    #3 Segments (Consumer/Corporate/Home Office)

df['Country'].value_counts()
    #United States 

df['City'].value_counts()
    #529 different Cities 
    
df['State'].value_counts()

df['Product_ID'].value_counts()
    #1861 products 

df['Category'].value_counts()
    #3 Categories (Office Supplies/Furniture/Technology)

df['Sub_Category'].value_counts()
    #17 Sub_Categories 
    #Top 5: Binders - 1492; Paper - 1338; Furnishings - 931; Phones - 876; Storage - 832;

#converting Ship_Date and Order_Date to date 
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d/%m/%Y')
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], format='%d/%m/%Y')

#Sorting the data by Order_Date
df.sort_values(by=['Order_Date'])
#to safe the sorting 'inplace=True'