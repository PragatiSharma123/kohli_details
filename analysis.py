import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read the CSV file
df = pd.read_csv("dataset.csv")
print(df.head(10))

# find total number of runs kohli has scored
total_runs = df["Runs"].sum()
no_of_matches=len(["Runs"])
print(f"total number of runs kohli has scored in {no_of_matches} matches:",total_runs)

#average of number of runs he has scored
avg_runs=df["Runs"].mean()
#print(f"Average runs of kohli in {no_of_matches} matches:", int(avg_runs))

# number of matches he has played at different Positions
Positions = df["Pos"].unique()
print(Positions)
#print(Positions.unique())
df["Pos"] = df["Pos"].map({
    'V Sri Lanka': "Batting at 3",
    'V Australia': "Batting at 4",
    'V Bangladesh': "Batting at 2",
    'V SOuth Aferica': "Batting at 1",
    'V New Zealand': "Batting at 7",
    'V England': "Batting at 5",
    
})
#print(df{["Runs," "Pos","Opposition"]}.head())
def show_pie_plot(df,key):
    counts = df[key].value_counts()
    counts_values = counts_values
    count_labels = counts.index

    fig = plt.figure(figsize=(10,7))
    plt.pie(counts_values, labels=count_labels)
    plt.show()

    show_pie_plot(df, "pos")
    show_pie_plot(df, "opposition")
    show_pie_plot(df, "Ground")



#Pos_counts = df["Pos"].value_counts()
#print(Pos_counts)
#print(type(Pos_counts))

#Pos_values = Pos_counts.values
#Pos_labels = Pos_counts.index
#print(Pos_values)

#fig = plt.figure(figsize=(10,7))
#plt.pie(Pos_values, labels=count_labels)
#plt.show()

#show_pie_plot(df, "pos")

#total runs scored in different Positions(
runs_at_Pos = df.groupby("Pos")["Runs"].sum()
runs_at_Pos_values = runs_at_Pos.values
runs_at_Pos_labels = runs_at_Pos.index

fig = plt.figure(figsize=(10,7))
plt.Pie(runs_at_Pos_values,labels= runs_at_Pos.values)
plt.show()
#total sixes  scored with different oppositions
sixes_with_ops = df.groupby("Opposition")["6s"]
sixes_with_ops_values = sixes_with_ops.values
sixes_with_ops_labels = sixes_with_ops.as_index
fig = plt.figure(figsize=(10,7))
plt.pie(sixes_with_ops_values, labels= sixes_with_ops.values)
plt.show()
#calculate the dismissals of kohli
dismissals = df["Dissmissala"].value_Counts()
print(dismissals)

dismissals_counts = dismissals.values
dismissals_labels = dismissals.index

show_pie_plot(df, "Dissmissal")

#number of centuries scored by kohli in first a
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]
tons_t = centuries.groupby("Runs")["Inns"].value_countsprint(tons_t)
print(tons_t)
fig = plt.figure(figsize=(10,7))
plt.pie(innings, tons, color='blue', Width=0.2
plt.show)
# Against Which teams he has scored most centuries
runs = df.groupby("Opposition"), centuries["Runs"], 
runs_values

# Analyze the strike rate

#kohli's strike rate in first century