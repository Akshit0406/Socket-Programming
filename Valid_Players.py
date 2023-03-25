import pandas as pd

# Reading a CSV file into a pandas DataFrame
df = pd.read_csv('players.csv')

#cleaning the data
#Removing all columns other than web_name, total_points and position
df = df[['web_name','total_points','position']]
#sorting with 2 params
df = df.sort_values(['position', 'total_points'], ascending=[True, False])

top_def = df.groupby('position').get_group('DEF').head(20) #selecting top 20 def and so on 
top_fwd = df.groupby('position').get_group('FWD').head(10)
top_gk = df.groupby('position').get_group('GKP').head(10)
top_mid = df.groupby('position').get_group('MID').head(30)

# Concatenate the selected players into a single DataFrame
df= pd.concat([top_def, top_fwd, top_gk, top_mid])

#print(df.head(10)) #checking if sorted properly
#print(df.tail(10))

buffer=input("Enter a player: ")

if buffer in df['web_name'].values:
    print("Good Pick!")
else:
    print("Entered player is invalid or not in the top picks.") 