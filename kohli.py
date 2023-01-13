import pandas as pd

df=pd.read_csv("dataset.csv")

#print(df.head(10))

#print(df.tail(10))

print(df.info)

print(df.shape)
print(df.describe())
print(["Opposition"].describe())
print(["Runs"].value_counts())
new_df=df(["runs", "4s" "6s","Opposition"])
print(new_df)
print(df["Opposition"]==" v Australia")
vs_aussies=df[df["Opposition"]=="v Australia"]
print(vs_aussies.head(10))
centuries = df[(df["Opposition"]=="v Australia")]
print(centuries)
#print(new_df.describe())
#print(new_df.iloc[2])