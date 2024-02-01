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

# Player controls 
def left_key():
    if not game_over:
        arrow.set_rotation(arrow.get_rotation()+5)
stage.event_key("left", left_key)

def right_key():
    if not game_over:
        arrow.set_rotation(arrow.get_rotation()-5)
stage.event_key("right", right_key)

def up_key():
    global moving, shot_count, color
    if not moving and not game_over:
        color = ball.get_color()
        ball.set_rotation(arrow.get_rotation())
        moving = True 
        while moving:
            ball.move_forward(8)
            stage.wait(.02)
            # create side walls 
            if ball.get_x() > 240 or ball.get_x() < -240:
                ball.set_rotation(180-ball.get_rotation())
        #move balls down the screen ever 5 shots 
        shot_count += 1
        if shot_count%5 == 0:
            move_bubbles()
        reset_ball()
stage.event_key("up", up_key)

#move bubbles down the screen 
def move_bubbles():
    global game_over
    back_board.set_y(back_board.get_y()-15)
    for bubble in bubbles:
        bubble.set_y(bubble.get_y()-15)
        
    if bubbles[len(bubbles)-1].get_y() < -170:
        text.set_text("Game Over")
        game_over = True

def main():
    reset_ball()
    create_bubbles()
    
if __name__ == '__main__':
    main()