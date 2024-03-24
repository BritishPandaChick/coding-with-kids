stage.set_background("space")
stage.disable_all_walls()
ufo = codesters.Sprite("ufo")

def up_key():
    ufo.move_up(20)
    
def down_key():
    ufo.move_down(20)
    
stage.event_key("up", up_key)
stage.event_key("down", down_key)