import turtle

bob = turtle.Turtle()




bob.color('#000000', '#E0E0E0')
bob.pensize(5)
bob.penup()
bob.goto(-100,-50)
bob.pendown()
bob.right(45)
bob.begin_fill()
bob.circle(100,270)
bob.penup()
bob.goto(-101,-50)
bob.pendown()
bob.left(110)
bob.end_fill()
bob.color('#000000','#ffffff')
bob.begin_fill()
bob.circle(78,229)
bob.end_fill()
bob.penup()
bob.color('#000000', '#E0E0E0')
bob.goto(8,25)
bob.left(20)
bob.pendown()
bob.begin_fill()
bob.forward(40)
bob.left(135)
bob.forward(35)
bob.end_fill()
bob.penup()
bob.goto(-5,-25)
bob.pendown()
bob.right(45)
bob.circle(20,70)
bob.penup()
bob.goto(25,20)
bob.color('#000000', '#ffffff')
bob.right(130)
bob.pendown()
bob.begin_fill()
bob.circle(10,180)
bob.end_fill()
bob.forward(10)

bob.circle(10,180)

bob.forward(10)
bob.back(5)
bob.left(90)
bob.forward(20)
bob.back(5)
bob.right(90)
bob.circle(10,45)

bob.penup()
bob.goto(-20,-75)
bob.left(60)
bob.back(10)
bob.pendown()
bob.color('#CCCACA')
bob.circle(90,160)
bob.right(178)
bob.circle(-90,90)
bob.left(178)
bob.circle(90,90)
bob.right(178)
bob.circle(-90,45)
bob.penup()
bob.goto(-75,103)
bob.left(70)
bob.pendown()
bob.circle(-78,45)





turtle.done()
