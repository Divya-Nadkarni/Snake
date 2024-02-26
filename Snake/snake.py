from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
            new_segment=Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())
    
    def move(self):
        for segment_pos in range(len(self.segments)-1,0,-1):
            new_x=self.segments[segment_pos-1].xcor()
            new_y=self.segments[segment_pos-1].ycor()
            self.segments[segment_pos].goto(new_x,new_y)
        self.head.fd(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
     

