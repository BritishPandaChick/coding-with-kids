# add check_background function
def check_background():
    global background_change
    stage.set_background_x(stage.get_background_x() + background_change)
    if stage.get_background_x() < -2000:
        background_change = 1
    elif stage.get_background_x() > -250:
        background_change = -1
        
# add ball_movement function
def ball_movement():
    if stage.get_background_x() % 200 == 0 and bouncy.get_y() < 0:
        bouncy.set_y_speed(5)
    if bouncy.get_y() > -230:
        bouncy.set_y_speed(bouncy.get_y_speed() - 0.1)

# add main function
def main():
    stage.set_background("scrollingflowers")
    stage.set_background_x(-250)
    while True:
        check_background()
        ball_movement()
        stage.wait(0.001)
        
bouncy = codesters.Circle(0, -230, 40, "lightblue")
background_change = -1
main()
