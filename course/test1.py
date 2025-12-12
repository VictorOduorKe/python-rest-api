import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

data =pd.read_csv('matches.csv')
df=pd.DataFrame(data)

print(df.head())
print(df.shape)

print (f'player of match {df["player_of_match"].value_counts()}')

# getting frequency of most player of match awards
top_players=df['player_of_match'].value_counts()[0:10]
print("Top 10 players with most Player of the Match awards:")
print(top_players)

 # making bar for top 5 players with most man of the match awards
plt.figure(figsize=(8,6))
plt.bar(list(df['player_of_match'].value_counts()[0:5].keys()),list(df['player_of_match'].value_counts()[0:5]),color=['blue','green','red','orange','purple'])
plt.title('Top 5 Players with Most Player of the Match Awards')
plt.xlabel('Players')
plt.ylabel('Number of Awards')
plt.savefig('top_player.png')
print("Plot ssaved as png")
plt.close()

# frequency of the results
result_counts=df['result'].value_counts()
print("Match Results Frequency:")
print(result_counts)

# team that has won most number of tosses
toss_wins=df['toss_winner'].value_counts()
print("Teams with Most Toss Wins:")
print(toss_wins)

# getting recods where team has won the batting first
win_by_batting_first=df[df['win_by_runs']!=0]
print(win_by_batting_first.head())

# visualizing the win by runs
plt.figure(figsize=(10,6))
plt.hist(win_by_batting_first['win_by_runs'],bins=30, color='cyan',alpha=0.7)
plt.title('Distribution of Wins by Runs')
plt.xlabel('Runs')
plt.ylabel('Number of Matches')
plt.grid(axis='y', alpha=0.75)
plt.savefig('win_by_runs_distribution.png')
print("Histogram saved as win_by_runs_distribution.png")
plt.close()

# finding the winner of wins for each team after batting first
batting_first_wins=win_by_batting_first['winner'].value_counts()
print("Number of Wins by Batting First for Each Team:")
print(batting_first_wins)

# ploting bar grapgh for wins after batting first
plt.figure(figsize=(8,6))
plt.bar(list(win_by_batting_first['winner'].value_counts()[0:3].keys()),list(win_by_batting_first['winner'].value_counts()[0:3]),color=['red','blue','green'])
plt.title(' Number of wins after batting first by each team')
plt.xlabel("Teams")
plt.ylabel("Number of wins")
plt.savefig('Wins_after_batting_first.png')
print("Plot saved as Wins_after_batting_first.png")
plt.close()

# pie chart for wins after batting first

plt.figure(figsize=(7,7))
plt.pie(win_by_batting_first['winner'].value_counts(),labels=list(win_by_batting_first['winner'].value_counts().keys()),autopct='%1.1f%%',startangle=140)
plt.title('Distribution of Wins after Batting First by Teams')
plt.tight_layout()
plt.savefig('batting_first_wins_distribution.png')
print("Pie chart saved as batting_first_wins_distribution.png")
plt.close()

# extrating data where team has won after batting second
batting_second_wins=df[df['win_by_wickets']!=0]
print(batting_second_wins.head())   

# histogram for wins after batting second
plt.figure(figsize=(10,6))
plt.hist(list(batting_second_wins['win_by_wickets']),bins=30,color='magenta',alpha=0.7)
plt.title("Distribution of wins by wicket")
plt.xlabel("Wickets")
plt.ylabel('Number of matches')
plt.grid(axis='y',alpha=0.75)
plt.savefig("wins_by_wickets_distribution.png")
print("Histogram saved as wins_by_wickets_distribution.png")
plt.close()

# finding frequency of wins after batting second by each team
batting_second_wins_count=batting_second_wins['winner'].value_counts()
print("Number of Wins by Batting Second for Each Team:")
print(batting_second_wins_count)

# bar graph for top 3 teams after batting second
plt.figure(figsize=(8,6))
plt.bar(list(batting_second_wins['winner'].value_counts()[0:3].keys()),list(batting_second_wins['winner'].value_counts()[0:3]),color=['orange','purple','cyan'])
plt.title('Number of wins after batting second by each team')
plt.xlabel('Teams')
plt.ylabel('Number of wins')
plt.savefig('Wins_after_batting_second.png')
print("Plot saved as Wins_after_batting_second.png")
plt.close()

# pie chart for wins after batting second
plt.figure(figsize=(7,7))
plt.pie(batting_second_wins['winner'].value_counts(),labels=list(batting_second_wins['winner'].value_counts().keys()),autopct='%0.1f%%',startangle=140)
plt.title('Distribution of Wins after Batting Second by Teams')
plt.tight_layout()  
plt.savefig('batting_second_wins_distribution.png')
print("Pie chart saved as batting_second_wins_distribution.png")
plt.close()

# number of matches played in each season
matches_per_season=df['season'].value_counts()
print("Number of Matches Played in Each Season:")
print(matches_per_season)

# line plot for number of matches played in each season
plt.figure(figsize=(10,6))
sns.lineplot(x=matches_per_season.index, y=matches_per_season.values, marker='o', color='teal')
plt.title('Number of Matches Played in Each Season')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.grid()
plt.savefig('matches_per_season.png')
print("Line plot saved as matches_per_season.png")
plt.close()

# number of matches played in each city
matches=df['city'].value_counts()
print("Number of matches played in each city")
print(matches)

# pie chart for number of matches played in each city
plt.figure(figsize=(8,8))
plt.pie(matches,labels=list(matches.keys()), autopct='%0.1f%%', startangle=140)
plt.title('Distribution of Matches Played in Each City')
plt.tight_layout()  
plt.savefig('matches_per_city.png')
print("Pie chart saved as matches_per_city.png")
plt.close()

# how many times team ha won the match after winning the toss
toss_wins_and_match_wins=df[df['toss_winner']==df['winner']]
toss_wins_and_match_wins_count=toss_wins_and_match_wins['toss_winner'].value_counts()
print("Number of Times Teams Won the Match After Winning the Toss:")
print(toss_wins_and_match_wins_count)

# bar graph for teams winning match after winning toss
plt.figure(figsize=(8,6))
plt.bar(list(toss_wins_and_match_wins_count.keys()),list(toss_wins_and_match_wins_count),color=['brown','pink','gray','olive','cyan'])
plt.title('Number of times teams won match after winning toss')
plt.xlabel('Teams')
plt.ylabel('Number of wins')
plt.savefig('toss_wins_and_match_wins.png')
print("Plot saved as toss_wins_and_match_wins.png")
plt.close()

#find sum team has won match after winning toss
total=np.sum(df['toss_winner']==df['winner'])
print(f"Total matches won by teams after winning toss: {total}")