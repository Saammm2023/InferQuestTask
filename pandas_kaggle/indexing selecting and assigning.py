import pandas as pd

review=pd.read_csv("D:\IITG.ai\dataforcsvreading.csv",index_col=0)#use index_col=0 function to set the indexes as the first column frm our csv file (if there is any)


print(review.Customer,'/n') #prints the single column of customer

print(review['Transaction ID'],'/n') #does the same thing as above, but we cant use upar wala fn coz there's a space in the column name
print(review['Transaction ID'][0],'/n')


#iloc-->same as normal python LL excluded, need to use index number to access
print(review.iloc[0])#to print the first row of the data frame

#format iloc[row,column] & ':' is used for slicing, ie accessing a certain part out of the whole thing
print(review.iloc[:,0],'/n')#prints the first column with all its rows
print(review.iloc[:3,0],'/n')#prints the 0th col bt only the first 3 rows
print(review.iloc[1:3,0],'/n')#prints the 0th col bt only rows frm index 1 to 2
print(review.iloc[[0,2,4],0],'/n')#prints 0th col bt rows w/ index 0,2,4
print(review.iloc[-5:],'/n')#prints the last 5 elements of the dataset (all cols, bt last 5 rows)


#loc-->indexes inclusive of both UL LL, need to put col/row name to access
print(review.loc[:,['Transaction ID','Item','Price']],'/n')#all rows bt only the specified cols

#can put conditional statements in loc
review.set_index('Item')#moves a column from being a normal column to being the index (row labels) of the DataFrame.
review.loc[review.Store_Location.isin(['New York','Las Vegas'])]#NY or LV
review.loc[review.Quantity.notnull()]#prints the quantity not null cols


