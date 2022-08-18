from turtle import Turtle
position = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.list1 = []
        self.make()
        self.head = self.list1[0]
    def make(self):
        for i in position:
            self.add(i)
    def add(self, position):
        timy = Turtle("square")
        timy.penup()
        timy.color("white")
        timy.goto(position)
        self.list1.append(timy)
    def extend(self):
        self.add(self.list1[-1].position())
    def Move(self):
        for t in range(len(self.list1) - 1, 0, -1):
            new_x = self.list1[t - 1].xcor()
            new_y = self.list1[t - 1].ycor()
            self.list1[t].goto(new_x, new_y)
        self.list1[0].fd(20)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def reset(self):
        for t in self.list1:
            t.goto(1000, 1000)
        self.list1.clear()
        self.make()
        self.head = self.list1[0]




