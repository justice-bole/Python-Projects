size(600, 600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(4)

''' arc() arguements
arc(
    x_coordinate, y_coordinate,
    width, height,
    start_angle, end_angle
)'''

#arc(width/2, height/2,200, 200,0, 2)
#arc(width/2, height/2, 300, 300, 0, PI) #half circle
#arc(width/2, height/2, 400, 400, 0, PI*2) #full circle
#arc(width/2, height/2, 350, 350, 3.4, (PI*2)-(PI/2), PIE) #optional PIE arguement at end, makes a pie 'slice'

diskScale = 150 

#outermost circle
fill('#00FF00') #green
arc(width/2, height/2, diskScale*4, diskScale*4, 5, 5.5, PIE) #vacation

#outer circle
fill('#FF6067') #peach
arc(width/2, height/2, diskScale*3, diskScale*3, PI, 4, PIE) #metal
arc(width/2, height/2, diskScale*3, diskScale*3, 4, 5, PIE) #rap
fill('#0000FF') #blue
arc(width/2, height/2, diskScale*3, diskScale*3, 5, 6, PIE) #photos
arc(width/2, height/2, diskScale*3, diskScale*3, 6, 2*PI, PIE) #work

#inner circle
fill('#FF0000')
arc(width/2, height/2, diskScale*2, diskScale*2, 0, PI, PIE) #videos
fill('#FF1070') #pink
arc(width/2, height/2, diskScale*2, diskScale*2, PI, 5, PIE) #music
fill('#900090') #purple
arc(width/2, height/2, diskScale*2, diskScale*2, 5, 2*PI, PIE) #docs

#innermost circle
fill('#004477')
circle(width/2, height/2, diskScale)#HDD
