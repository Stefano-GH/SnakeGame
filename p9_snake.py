from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up_direction = 90
left_direction = 180
down_direction = 270
right_direction = 0


class Snake: 
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.game_on = True


    def create_snake(self):
        for position in positions:
            self.add_segment(position)
    
    
    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.snake_body.append(turtle)
    
    
    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
    
    
    def extend(self):
        self.add_segment(self.snake_body[-1].position())
    
    
    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(move_distance)
    
    
    def up(self):
        if self.head.heading() != down_direction:
            self.head.setheading(up_direction)
    
    
    def left(self):
        if self.head.heading() != right_direction:
            self.head.setheading(left_direction)
    
    
    def down(self):
        if self.head.heading() != up_direction:
            self.head.setheading(down_direction)
    
    
    def right(self):
        if self.head.heading() != left_direction:
            self.head.setheading(right_direction)
    
    
    def game_off(self):
        self.game_on = False