size(600, 300)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(4)

#Nose
point(175, 150)

#Forehead
triangle(125,25, 225,25, 175,75)

#Left Eye
ellipse(100,100, 100, 50)
fill('#FFFFFF')
ellipse(100,100, 10, 50)
noFill()
circle(100,100, 50)

#Right eye
ellipse(250,100, 100, 50)
fill('#FFFFFF')
ellipse(250,100, 10, 50)
noFill()
circle(250,100, 50)

#Mouth
quad(100,160, 175,200, 250,160, 175,250)

#Random Line
line(450,80, 520,220)
