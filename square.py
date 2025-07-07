import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")

t = turtle.Turtle()
for _ in range(4):
    t.right(90)
    t.forward(100)

screen.mainloop()
