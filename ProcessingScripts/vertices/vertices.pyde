size(800, 800)
grid = loadImage('grid.png')
image(grid, 0, 0)
noFill()
stroke('#FFFFFF')
strokeWeight(10)

beginShape()
vertex(262, 238)
vertex(262, 178)
bezierVertex(262,40, 370,30, 500,30)
bezierVertex(630,30, 730,40, 735,178)
bezierVertex(735,380, 735,380, 735,380)
bezierVertex(735,380, 690,490, 620,490)
endShape()





'''
beginShape() # begins recording vertices for a shape ...
vertex(100, 100)
vertex(200, 100)
vertex(200, 200)
vertex(100, 200)
endShape() # stops recording

beginShape() # S curve
vertex(400, 200)
bezierVertex(
    300, 300,
    500, 500,
    400, 600    
)
endShape()

beginShape() #heart
vertex(600, 400)
bezierVertex(420,300, 550,150, 600,250)
bezierVertex(650,150, 775,300, 600,400)
endShape()

fill('#6633FF')
beginShape() #coin
vertex(100, 600)
bezierVertex(100,545, 145,500, 200,500)
bezierVertex(255,500, 300,545, 300,600)
bezierVertex(300,655, 255,700, 200,700)
bezierVertex(145,700, 100,655, 100,600)
beginContour()
vertex(180, 580)
vertex(180, 620)
vertex(220, 620)
vertex(220, 580)
endContour()
endShape()
'''
