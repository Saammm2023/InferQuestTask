import pandas as pd

review=pd.read_csv("D:\IITG.ai\dataforcsvreading.csv",index_col=0)#use index_col=0 function to set the indexes as the first column frm our csv file (if there is any)


#summary functions

review.Price.describe()#displays the count,mean,max etc for the numerical data in there
#if the column contains string data type, it displays the count, unique,top,freq

meanprice=review.Price.mean()#gives only mean
meanprice=review.Price.median()#gives only median
review.Store_Location.unique()#to see a list of unique values in the column
review.Store_Location.value_counts()#To see a list of unique values and how often they occur in the dataset


#Maps

#METHOD 1 : map()--> works on series(a single col)/applies function element by element

#A function that takes one set of values and "maps" them to another set of values.
#.map() returns a new Series where all the values have been transformed by the given function

review.Price.map(lambda p: p - meanprice)#calculates the deviation from the mean value of each record
'''the lambda is basically like a function :
def deviation(p):
    return p - review_points_mean
review.Price.map(deviation)
'''


#METHOD 2 : apply()--> works on series and dataframes/can apply function to each element or to rows/columns

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')


#METHOD 3
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean
reviews.country + " - " + reviews.region_1


#idxmax function:
ratio=reviews.points/reviews.price
indexofbestbargain=ratio.idxmax()
bargain_wine = reviews.loc[indexofbestbargain,'title']
