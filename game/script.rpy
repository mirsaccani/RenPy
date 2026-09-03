
# Declare the characters.
define e = Character(_('Eileen'), color="#c8ffc8", screen="character_say")

# The game starts here.
#begin start
label start:

    scene bg washington
    show eileen vhappy
    with dissolve

    # Start the background music playing.
    play music "sunflower-slow-drag.ogg"

    window show

    e "Hi! My name is Eileen."

    show eileen happy

    menu:
        "First Option":
            jump firstOption

        "Second Option":
            jump secondOption

    label firstOption:
        
        "Choose to talk to the mayor."
        jump endGame

    label secondOption:

        "Choose to search the office."
        jump endGame


    label endGame:
        
        "This is the end of the game."
        return


    # Returning from the top level quits the game.
    return
