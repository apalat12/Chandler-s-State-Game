# with open('weather_data.csv',mode='r') as data:
#     cont = data.readlines()
#
# print(cont)
# import csv

# with open('weather_data.csv', mode='r') as data:
#     cont = csv.reader(data)
#     print(cont)
#     temp = [int(row[1]) for row in cont if row[1] != 'temp']
#     print(temp)

import pandas as pd
from turtle import Screen
from turtle import Turtle
from states_marker import State_Writer

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # data_list = data["temp"].to_list()
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(data.condition)
# # print(sum(data_list)/len(data_list))
# # data_dict = data.to_dict()
# # print(data_dict)
# # get dat in Row
# # print(data[data.day=='Monday'])
#
# # print(data[data.temp==data["temp"].max()])
#
# monday = data[data.day=='Monday']
# print(monday.temp*1.8 + 32)
#
# #create dataframe from scratch
#
# data_dict = {
#     "students": ['Amy','James','Angela'],
#     "scores": [76,56,65]
# }
#
# new_d= pandas.DataFrame(data_dict)
# print(new_d)
# new_d.to_csv("new_data.csv")

# sqr_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(sqr_data["Primary Fur Color"]) # rows of that coloumn
# g, c, b = 0, 0, 0
# for color in sqr_data["Primary Fur Color"]:
#     if color == 'Gray':
#         g += 1
#     elif color == 'Cinnamon':
#         c += 1
#     elif color == 'Black':
#         b += 1
# grey_sqr = len(sqr_data[sqr_data["Primary Fur Color"]=="Gray"])
# # print(grey_sqr)
# # gray_sqr = sqr_data[sqr_data.Primary_Fur_Color=='Gray']
# # cin_sqr = sqr_data[sqr_data.Primary_Fur_Color=='Cinnamon']
# # blk_sqr = sqr_data[sqr_data.Primary_Fur_Color=='Black']
# # print(len(gray_sqr),len(cin_sqr),len(blk_sqr))
# #
# sqr_dict = {
#     "color":['Gray','Cinnamon','Black'],
#     "count":[g,c,b]
# }
# new_sqr_data = pandas.DataFrame(sqr_dict)
# new_sqr_data.to_csv("new_sqr_data.csv")

screen = Screen()
tim = Turtle()

screen.title("U.S. States Game")
screen.setup(800, 800)
screen.addshape("blank_states_img.gif")

state_write = State_Writer("", 10, 100)

tim.shape("blank_states_img.gif")

# def mouse_click(x,y):
#     print(x,y)
# screen.onscreenclick(fun=mouse_click)
# screen.mainloop()

states = pd.read_csv("50_states.csv")
# # print(states)
# for (idx,row) in states.iterrows():
#     print(row.state)
states_list = states.state.to_list()
remaining_states = states_list.copy()

Game_ON = True
correct = 0
while Game_ON:

    screen_input = screen.textinput("{}/50 Correct States:".format(correct), "Name Another state:")
    usr_state = screen_input.title()
    if screen_input.title() in states_list:
        loc = states[states.state == usr_state]
        # state_write.__init__(usr_state,loc.x.to_list()[0],loc.y.to_list()[0])
        state_write.__init__(usr_state, int(loc.x), int(loc.y))
        correct += 1
        try:
            remaining_states.remove(usr_state)
        except:
            pass

    else:
        screen_input = screen.textinput("Enter 0 to give up", "")
        if screen_input == '0':
            Game_ON = False
    if correct == 50:
        Game_ON = False

# print(remaining_states)
new_d = pd.DataFrame(remaining_states)
# print(new_d)
new_d.to_csv("remaining_states.csv")

# screen.exitonclick()
