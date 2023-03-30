import turtle 
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ["green", "yellow", "dark red", "pink"]
for number in range (400):
	t.forward(number+1)
	t.right(150)
	t.right(30)
	t.right (90)
	t.left(20)
	t.left(45)
	t.pencolor(colors[number%4])
turtle.done()
