import pandas

data = pandas.read_csv("weather_data.csv")
# Just read the CSV, output_type <class 'pandas.core.frame.DataFrame'>
# data is the object created to DataFrame
# print(type(data["temp"]))#<class 'pandas.core.series.Series'>

##for row in data["temp"]: #temp could be any coloumn ,returns Series or list
##    print(row)

##print(data.to_dict()) #it will convert data to dictionary

##print(data["temp"].to_list()) # it will convert Series to python list

##print(data["temp"].mean()) # ==data.temp.mean()
##print(data.temp.mean())
##print(data["temp"].max())
##print(data["day"]) # any coloumn can be used and it will give a list
##print(data["condition"]) # == data.condition
#pandas take each of the heading and converts it into attributes

#To Get data in row

##print(data[data['day']=='Monday'])
###OR
##print(data[data.day=='Monday'])
##print(data[data.temp==data.temp.max()])
#OR
##print(data[data.temp==data["temp"].max()])
monday = data[data.day=="Monday"] # ROW for Monday 
##print(monday.temp*1.8+32)
#OR
##print(data[data.day=="Monday"].temp*1.8 +32)

my_dict = {
    "students":["Amy","James","Angela"],
    "Score": [45,57,83]
    }

##new_data = pandas.DataFrame(my_dict)
##print(new_data)
##new_data.to_csv("sample.csv")


states = pd.read_csv("50_states.csv")
# print(states)
for (idx,row) in states.iterrows():
    print(row.state)
states_list = states.state.to_list()
remaining_states = states_list.copy()











