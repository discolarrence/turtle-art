import turtle

turtle.down()
x = 0
y = 5
for side in range(720):
    x = x + .01
    y = y - .01
    turtle.forward(x)
    turtle.right(y)

turtle.done()
