import pandas


data = pandas.read_csv("weather_data.csv")

print(data)

data_excel = data.to_excel("output.xlsx")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(round(data["temp"].mean(), 2))
print(data["temp"].max())
print(data.temp.max())
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])
print(data[data.temp == 24])
print((data[data.day == 'Monday']).condition)



