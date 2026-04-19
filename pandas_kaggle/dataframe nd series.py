import pandas as pd

tablewithoutind=pd.DataFrame({'yes':[50,21],'no':[131,2]})#has a by default indexing of 0 1 2 3 so on

tablewithind=pd.DataFrame({'yes':[50,21],'no':[131,2]},index=['product a','product b'])

series=pd.Series([30,35,40],index=['a','b','c'],name='likes')#series can only have 2 columns and an overall name to it

print(tablewithoutind,'\n')
print(tablewithind,'\n')
print(series)


review=pd.read_csv("D:\IITG.ai\dataforcsvreading.csv",index_col=0)#use index_col=0 function to set the indexes as the first column frm our csv file (if there is any)


print(review.shape,'\n')#tells the size of the table in (row,column) format

tableform=review.head()#gets the first five rows with the headings of each column and index (frm o to 4) of each row
print(tableform)

