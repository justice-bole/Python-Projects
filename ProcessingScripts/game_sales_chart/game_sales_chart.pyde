size(800, 800)
background('#FFFFFF')
tsv = loadStrings('list_of_best-selling_video_games.tsv')
noStroke()

#colors
r = '#FF0000' # red
o = '#FF9900' # orange
y = '#FFFF00' # yellow
g = '#00FF00' # green
b = '#0099FF' # blue
p = '#6633FF' # violet

colors = [r, o, y, g, b, p]

text_x = 10
text_y = 15

rect_x = 10
rect_y = 4

i = 0

for entry in tsv[1:]:
    game = entry.split('\t')
    game_name = game[1]
    game_sales = int(game[2])
    bar_size = game_sales / 230000
 
    if i <= 5:
        fill(colors[i])
        rect(rect_x, rect_y, bar_size, 15)
        i += 1
        rect_y += 15
    
        fill('#000000')
        textAlign(LEFT)
        text(game_name, text_x, text_y)
        text_y += 15
    else:
        i = 0
