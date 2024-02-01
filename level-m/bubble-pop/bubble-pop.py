stage.set_background_color("LightGray")
back_board = codesters.Rectangle(0, 220, 500, 5, "Pink")
arrow_url = "http://www.pngall.com/wp-content/uploads/2016/07/Arrow-Free-Download-PNG.png"
arrow = codesters.Sprite(arrow_url, 0, -210)
arrow.set_size(.2)
arrow.set_rotation(90)
ball = codesters.Circle(0, -210, 20)

#global variables 
bubbles = []
colors = ["blue", "yellow", "#00ff55", "#0099ff"]
rows = 3
columns = 19
moving = False
game_over = False
shot_count = 0
color = ""

# create initial bubbles
def create_bubbles():
    for row in range(rows):
        for col in range(columns):
            bubble = codesters.Circle(col*25-230, 205-row*22, 20, random.choice(colors))
            bubbles.append(bubble)
    
#resets the ball to its starting point and to a new color 
def reset_ball():
    ball.go_to(0, -210)
    ball.set_color(random.choice(colors))

def main():
    reset_ball()
    create_bubbles()
    
if __name__ == '__main__':
    main()