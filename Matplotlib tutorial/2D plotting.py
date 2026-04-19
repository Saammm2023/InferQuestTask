import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x_data=np.random.random(50)*100 #generates a 1D arr of 50 random numbers bt they r btwn 0.0 to 1.0, so multiply by 100. now they r btwn 0.0 to 100.0
y_data=np.random.random(50)*100


#SCATTER PLOT : bunch of different data points plotted as dots

plt.scatter(x_data,y_data)#to create
plt.show()#to print it

#plt.scatter(x_data,y_data,c="red")#to colour the dots using name
#plt.scatter(x_data,y_data,c="#000",s=150,marker="*")#to colour the dots using the hex code of the colour/s is the siz of the marker/ marker gives * instead of dots
#alpha is used to manage the transparency if the points are overlapping



#LINE PLOT

years=[2006 + x for x in range(16)]
weights=[80,83,84,85,86,82,81,79,83,80,82,82,83,79,80,87]

plt.plot(years,weights,c='g',lw=3,linestyle="--")#default plot function plots a line chart
plt.show()


#BAR CHART
#popularity/ likes for each programming language

x=["C","C++","python","java"]
y=[25,30,50,40]
plt.bar(x,y,color="r",width=5,edgecolor="green",lw=3)
plt.show()


#HISTOGRAM

ages=np.random.normal(20,1.5,1000)#(mean,deviation,number of values u want)

plt.hist(ages,"bins=20",bins=[ages.min(),18,21,ages.max()],cumulative=True)#cumulative histo is on)
plt.show()


#PIE CHART
langs=["C","C++","python","java"]
votes=[25,30,50,40]

explodes=[0.3,0,0,0]
         
plt.pie(votes,labels=langs,explode=explodes,autopct="%.2f%%",pctdistance=1.3,startangle=90)
plt.show()

#explode pulls the one with 0.3 out of the pie chart to highlight it
#autopct assigns percentage to each pie part
#pctdistance is basically arrangement of the display percentage
#startangle starts the pie at exactly 90 degrees



#BOX PLOT : shows the min, max,avg etc


heights=np.random.normal(172,8,300)

plt.boxplot(heights)
plt.show()


#another example
first=np.linspace(0,10,25)#linspace(start, stop, even gap)
second=np.linspace(10,20,25)
third=np.linspace(200,210,25)
fourth=np.linspace(210,230,25)


data=np.concatenate((first,second,third,fourth))

plt.boxplot(data)
plt.show()



#PLOT CUSTOMIZATION

#example 1
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
income = [55, 56, 62, 61, 72, 72, 73, 75]
income_ticks = list(range(50, 81, 2))

plt.plot(years,income)
plt.title("Income of Nilay(in USD)",fontsize=25,fontfamily="Comic Sans")#adds title to the overall plot
plt.xlabel("Year")#title of X axis
plt.ylabel("Yearly Income in USD")#title of Y axis
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])#gives  "$50k", "$52k", ..., "$80k" on each value on the y axis

plt.show()


#example 2
stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [90, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]

plt.plot(stock_a,label="company 1")
plt.plot(stock_b,label="company 2")
plt.plot(stock_c,label="company 3")
plt.legend(loc="lower center")#the labels we added wont show up unless we do this command

plt.show()



#LEGENDS 
votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=None)#the labels wont be added on the pie pieces
plt.legend(labels=people)#rather a legend will be added separately

plt.show()



#PLOT STYLING : used to change the look of the plot using the preprovided style sheets /need to import the style module for this part


style.use("ggplot")
style.use("dark_background")

# Link: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# Link: https://matplotlib.org/stable/tutorials/introductory/customizing.html

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=None)#the labels wont be added on the pie pieces
plt.legend(labels=people)#rather a legend will be added separately

plt.show()



#MULTIPLE FIGURES : to plot multiple different charts side by side

#method 1 : shows the figure 1 and figure 2 in two separate windows
x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)#np.arange is similar to linspace (explanation in numpy doubts chatgpt)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.plot(x2, y2)

plt.show()


#method 2: showing 4 different figures in one window

x = np.arange(100)

fig, axs = plt.subplots(2, 2)#this creates a kinda matrix of size 2*2

axs[0, 0].plot(x, np.sin(x))#this is the first element first row
axs[0, 0].set_title("Sine Wave")

axs[0, 1].plot(x, np.cos(x))#this is the second element first row
axs[0, 1].set_title("Cosine Wave")

axs[1, 0].plot(x, np.random.random(100))#this is the first element second row
axs[1, 0].set_title("Random Function")

axs[1, 1].plot(x, np.log(x))#this is the second element second row
axs[1, 1].set_title("Log Function")
axs[1,1].set_title("smth smth")

fig.suptitle("Four Plots")

plt.show()
#plt.savefig("fourplots.png",dpi=300) saves it in png format

















