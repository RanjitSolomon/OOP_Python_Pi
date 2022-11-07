from shapes import Paper, Rectangle, Oval, Triangle

paper=Paper()

rect1=Rectangle()
rect1.set_color("blue")
rect1.set_height(100)
rect1.set_width(200)
rect1.draw()

rect2=Rectangle()
rect2.set_x(10)
rect2.set_y(10)
rect2.set_height(200)
rect2.set_width(300)
rect2.set_color("green")
rect2.draw()

ovl=Oval()
ovl.set_color("yellow")
ovl.randomize(125, 150)
ovl.draw()


tri = Triangle(5,5,100,5,100,200)
tri.draw()

paper.display()

