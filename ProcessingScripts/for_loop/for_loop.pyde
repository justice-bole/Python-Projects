size(500, 500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

'''
circle(width/2, height/2, 30)
circle(width/2, height/2, 60)
circle(width/2, height/2, 90)
'''
'''
i = 0
while i < 24:
    print(i)
    i += 1
    circle(width/2, height/2, 30*i)
'''
'''
for i in range(3, 13, 3):
    print(i)
    circle(width/2, height/2, 30*i)
'''
'''
for i in range(12):
    line(width/6, height/6 * i/12, width/1.5, height/4 * i/12)
'''
line(width/5, height/5, width/3, height/4)
for i in range(13):
    if i % 2 == 0:
        line(width/6, height/6 * i/12, width/3, height/4 * i/12)
    else:
        line(width/5, height/5 * i/12, width/3, height/4 * i/12)
