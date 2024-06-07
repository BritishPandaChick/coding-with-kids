# global variables
score = 0
rows = 4
columns = 8
bricks = []

# score display
display = codesters.Text("Score: 0", 0, 235, "red")

# setup sprites
player = codesters.Rectangle(0, -220, 80, 15, "red")
player.lives = 3
ball = codesters.Circle(0, 0, 20, "blue")

# paddle controls
def left():
    player.move_left(15)
stage.event_key("a", left)

def right():
    player.move_right(15)
stage.event_key("d", right)

# Phase 2 - brick creation
# creates bricks in a grid
def creates_bricks():
    for row in range(rows):
        for col in range(columns):
            brick = codesters.Rectangle(col * 60 - 210, row * 30 + 120, 55, 25, "brown")
            brick.points = random.randint(1, 10)
            bricks.append(brick)

# Phase 4 - brick and paddle collision
# detects collision (of the ball) with any of the bricks by checking position; returns true if a brick was hit, otherwise false
def ball_collision(sprite, hit_sprite):
    global score
    # detects collision with paddle
    if hit_sprite.get_color() == "red":
        ball.set_y_speed(ball.get_y_speed() * -1.05)
        
    # detects collision with the bricks
    elif hit_sprite.get_color() == "brown":
        score += hit_sprite.points
        display.set_text("Score: {}".format(score))
        bricks.remove(hit_sprite)
        stage.remove_sprite(hit_sprite)
        ball.set_y_speed(ball.get_y_speed() * -1.05)
ball.event_collision(ball_collision)

# Phase 5 - Floor Collision
def floor_collision():
    # ball has fallen below the paddle, player loses a life and ball resets
    if ball.get_y() < -230:
        player.lives -= 1
        if player.lives > 0:
            reset_ball()
            return False
        # player has no more lives, end game by breaking the while loop
        else:
            return True

# Phase 3 - Main Game Loop and Movement
# resets the ball's position and speed
def reset_ball():
    ball.go_to(0, 0)
    stage.wait(3)
    ball.set_x_speed(random.randint(-5, 5))
    ball.set_y_speed(random.randint(-5, 5))
    
# main function
def main():
    creates_bricks()
    reset_ball()
    # main game loop runs while there are any bricks left
    while len(bricks) > 0:
        # Phase 5 - if true, player has no lives, game is over
        if floor_collision():
            break
        stage.wait(0.01)
    ball.set_x_speed(0) # add phase 5
    ball.set_y_speed(0) # add phase 5
    # Phase 5 - display final score after the game has ended
    display.set_text("GAME OVER! Final Score: {}".format(score))

# traditional way of running main functions in a python file
if __name__ == '__main__':
    main()