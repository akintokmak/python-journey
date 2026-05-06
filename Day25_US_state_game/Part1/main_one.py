# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

"""CSV"""
from numpy.ma.extras import average

import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
"""Pandas"""
#
import pandas
# data = pandas.read_csv("weather_data.csv")
#
# # print(data)
# # print("------------------")
# # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # print(temp_list)
"""average"""
# # print(average(temp_list))
# # print(data["temp"].mean())
"""max"""
# # print(data["temp"].max())
"""min"""
# # print(data["temp"].min())
# #
# #
"""Get Data in Columns"""
# # print(data["condition"])
# # print("----")
# # print(data.condition)
#
"""Get Data in Row"""
# # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = (monday.temp[0] * 1.8) + 32
# print(monday_temp)
#
"""Create a dataframe from scratch"""
# data_dict = {
#     "students" : ["Amy","James","Angela"],
#     "scores"   : [76,56,60]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Red"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

