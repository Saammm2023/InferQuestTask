import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',100)#to see all columns in the dataset

game_dataset=pd.read_csv(r"D:\IITG.ai\Task1\Games.csv")

#DATA UNDERSTANDING

print(game_dataset.shape)
#print(game_dataset.head())
game_dataset.columns#displays a list of all the column titles
game_dataset.dtypes


#DATA PREPARATION AND CLEANING
df=game_dataset

print(df.duplicated(subset=['GameID']).sum())

#dropping the non required columns
df = df.drop(columns=[ 'GameID',
    'HoursPerWeek', 
    'MinimapAttacks', 
    'MinimapRightClicks', 
    'ComplexAbilitiesUsed'
])

df.head()
df.tail()

df[['TotalHours', 'Age']] = df[['TotalHours', 'Age']].replace('?', np.nan)
df=df.dropna()#players with league index of 8 have been dropped

df[['TotalHours', 'Age']] = df[['TotalHours', 'Age']].astype('Int64')

print(df.shape)
print(df.dtypes)

#print(df.describe())

#the max in total hrs is 1M
print(df[df['TotalHours'] == 1000000.000000]['Age'])#age is 18, which is not possible
#checking for any more such entries:
#print(df[df['Age'] * 365 * 24 < df['TotalHours']])
df=df[df['Age'] * 365 * 24 > df['TotalHours']]

print(df.shape)
print(df.describe())



#QUESTION 1

def ques1(df):

    plt.style.use("dark_background")
    palette = sns.color_palette("rocket",n_colors=7, as_cmap=False)

    plt.figure(figsize=(11,6))

    plt.subplot(1,2,1)
    sns.boxplot(x='LeagueIndex',y='APM',data=df,palette=palette,
                flierprops=dict( markerfacecolor='grey', markersize=5, linestyle='none'),
        medianprops=dict(color='grey'),
        whiskerprops=dict(color='grey'),
        capprops=dict(color='grey'))
    plt.title('Boxplot')

    plt.subplot(1,2,2)
    sns.barplot(x='LeagueIndex',y='APM',data=df,errcolor='grey',palette=palette)
    plt.title('Barplot')

    plt.tight_layout()
    plt.show()


ques1(df)

'''
INFERENCES:
APM is clearly increasing with increasing League Index.
More number of Outliers are seen in case of Pro players, which means some of the players perform at extremely high APM

The Bar plot shows a smooth upward trend.
The error bars get larger as skill increases. This suggests more diverse playing style among the top players
'''




#QUESTION 2


def ques2_scatterplot(df):
    plt.style.use("dark_background")

    plt.figure(figsize=(12,8))

    

    plt.subplot(2,2,1)
    sns.regplot(x=df['TotalHours'],y=df['LeagueIndex'],scatter_kws={'alpha':0.4,},color='#6c8ed3') #(kinda workin like i want it to)
    plt.ylim(0,8)
    plt.title("League Index vs Total Hours(Full Range)") 

    plt.subplot(2,2,2)
    sns.regplot(x=df['TotalHours'],y=df['LeagueIndex'],scatter_kws={'alpha':0.4,},color='#6c8ed3') #(kinda workin like i want it to)
    plt.xlim(0,6000)
    plt.ylim(0,8)
    plt.title("League Index vs Total Hours(Focused View)")

    plt.subplot(2,2,3)
    sns.regplot(x=df['TotalHours'],y=df['LeagueIndex'],logx=True, scatter_kws={'alpha':0.4,},color='#6c8ed3') 
    #plt.xlim(0,10000)
    plt.ylim(0,8)
    plt.title("League Index vs Total Hours(Log scaled regression)")

    
    plt.tight_layout()
    plt.show()


ques2_scatterplot(df)

'''
INFERENCES:
The full range plot has extreme outliers, which create distortion in the correlation.
Hence, by using the zoomed in view (by reducing the range), we see there is a slightly positive correlation between the two.
Using the logx scale, shows a rapid increase initially, bt tapers off later.

We see that few of the players have put in a lot of time to improve their skill.
Whereas, there are a bunch of players (at higher league index) who are naturally talented at the game.
We see that there is a decent correlation between League index and Hours spent playing. But clearly this relation is not linear.
'''



#QUESTION 3

def ques3(df):
    plt.style.use("dark_background")
    palette = sns.color_palette("rocket",n_colors=7, as_cmap=False)

    plt.figure(figsize=(13,7))

    plt.subplot(2,2,1)
    sns.kdeplot(data=df,x='SelectByHotkeys',hue='LeagueIndex',palette=palette)
    plt.title('Distribution of SelectByHotkeys across Leagues')

    plt.subplot(2,2,2)
    sns.kdeplot(data=df,x='AssignToHotkeys',hue='LeagueIndex',palette=palette)
    plt.title('Distribution of AssignToHotkeys across Leagues')

    plt.subplot(2,2,3)
    sns.kdeplot(data=df,x='UniqueHotkeys',hue='LeagueIndex',palette=palette)
    plt.title('Distribution of UniqueHotkeys across Leagues')
    #plt.legend(loc="lower right")

    plt.tight_layout()
    plt.show()


ques3(df)


'''
INFERENCES:
SelectByHotkeys and AssignToHotkeys are more right skewed for higher league players as compared to UniqueHotKeys
The unique hotkeys plot shows a greater shift in the plot. This means that unique hotkey usage by higher league players is more than the lower ones.

Overall, the distribution shows that gamers with league index greater than or equal to 5 tend to use the hotkey features more.

'''


#QUESTION 4


def ques4(df):
    
    plt.style.use("dark_background")
    colors = ['#ea745e', '#f6c4b5']
    
    #normalising the data for to obtain a proper plot
    LeagueAvgdf = (df.groupby(['LeagueIndex']).mean()/df.groupby(['LeagueIndex']).mean().iloc[0]).sort_values(by=7, axis=1, ascending=False)
    LeagueAvgdf=LeagueAvgdf.drop(columns=[ 'Age',
        'TotalHours', 'NumberOfPACs',
        'APM', 
        'SelectByHotkeys', 
        'AssignToHotkeys','UniqueHotkeys','ActionsInPAC','TotalMapExplored','WorkersMade','UniqueUnitsMade','ComplexUnitsMade'
    ])

    LeagueAvgdf.plot(color=colors, title = 'Relation between Skill levels, Action latency and Gap between PACs ')

    plt.show()


ques4(df)

'''
INFERENCES:
On normalizing the means per league and plotting only ActionLatency and GapBetweenPACs along with League index tells us that
players with higher skill levels have shorter gaps between PACs.
Though Action Latency also plays a significant role, but Gap between PACs is a dominant factor.
'''




#QUESTION 5

def ques5(df):
    plt.style.use("dark_background")

    plt.figure(figsize=(13,7))

    sns.heatmap(data=df.corr(),annot=True)#corr to exclude the non numeric dtypes
    plt.show()

ques5(df)


'''
INFERENCES:
Greater positive values denote greater relation between the two features being compared.
Similarly, more negative values show stronger influence.
When looking at the League Index column, we see that APM, SelectByHotkeys, AssignToHotkeys,
NumberOfPACs, GapBetweenPACs and ActionLatency are the most influential gameplay features in determining
a player's League Index.

'''
