from random import randint

WIDTH = 800
HEIGHT = 512
score = 0
game_over = False
game_menu = True

bg = "background"

jim = Actor("jim")
jim.pos = 100, 100

can = Actor("can")
can.pos = 100, 100

paper = Actor("paper")
paper.pos = 100, 100

trash = Actor("trash")
trash.pos = 100, 100

main_screen = Actor("mainmenu")
over_screen = Actor("gameover")
def start_timer():
    clock.schedule(time_up, 30.0)


def draw():
    if game_over:
        over_screen.draw()
        screen.draw.text("Total Score: " + str(score), color="black" , topright = (780,10), fontsize=50)
    elif game_menu:
        main_screen.draw()
    else:
        screen.blit(bg, (0,0))
        jim.draw()
        can.draw()
        paper.draw()
        trash.draw()
        screen.draw.text("Trash Collected: " + str(score), color="black", topleft=(10,10), fontsize=50)

def place_can():
    can.x = randint(50, (WIDTH - 20))
    can.y = randint(50, (HEIGHT - 20))


def place_paper():
    paper.x = randint(20, (WIDTH - 20))
    paper.y = randint(20, (HEIGHT - 20))


def place_trash():
    trash.x = randint(20, (WIDTH - 20))
    trash.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global game_menu
    global game_over
    global score

    if game_menu:

        if keyboard.space:
            game_menu = False
            start_timer()
    elif game_over:
        if keyboard[keys.SPACE]:
            score = 0
            game_menu = True  
            game_over = False
    

    else:
        if keyboard.left:
            jim.x = jim.x - 3
        elif keyboard.right:
            jim.x = jim.x + 3
        elif keyboard.up:
            jim.y = jim.y - 3
        elif keyboard.down:
            jim.y = jim.y + 3

        can_collected = jim.colliderect(can)

        if can_collected:
            score = score + 1
            place_can()

        paper_collected = jim.colliderect(paper)

        if paper_collected:
            score = score + 1
            place_paper()

        trash_collected = jim.colliderect(trash)

        if trash_collected:
            score = score + 1
            place_trash()



place_can()
place_paper()
place_trash()
