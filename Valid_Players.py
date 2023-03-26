import pandas as pd

# Reading a CSV file into a pandas DataFrame
df= pd.read_csv('players.csv')

#cleaning the data
#Removing all columns other than web_name, total_points and position
df= df[['web_name','total_points','position']]
#sorting with 2 params
df = df.sort_values(['position', 'total_points'], ascending=[True, False])

top_def = df.groupby('position').get_group('DEF').head(20) #selecting top 20 def and so on 
top_fwd = df.groupby('position').get_group('FWD').head(10)
top_gk = df.groupby('position').get_group('GKP').head(10)
top_mid = df.groupby('position').get_group('MID').head(30)

sn=range(1,71)
# Concatenate the selected players into a single DataFrame
df= pd.concat([top_def, top_fwd, top_gk, top_mid])
df['Serial_No']=sn
df=df[['Serial_No','web_name','total_points','position']]
#print(df.head(10)) #checking if sorted properly
#print(df.tail(10))
