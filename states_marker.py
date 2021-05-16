from turtle import Turtle


class State_Writer(Turtle):

    def __init__(self,state_name,posx,posy):
        super().__init__()
        self.color("black")
        self.score=0
        self.penup()
        self.goto(posx,posy)
        self.write("{}".format(state_name), move=True, align="left", font=("Courier", 10, "bold"))
        self.hideturtle()


