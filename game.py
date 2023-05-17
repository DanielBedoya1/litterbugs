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

def start_timer():
    clock.schedule(time_up, 30.0)


def draw():
    if game_over:
        screen.fill("blue")
        screen.draw.text("Final Score: " + str(score), topleft = (10,10), fontsize=100)
    elif game_menu:
        screen.fill("black")
        screen.draw.text("Press Space to Start" , topleft = (10,10), fontsize=100)
    else:
        screen.blit(bg, (0,0))
        jim.draw()
        can.draw()
        paper.draw()
        trash.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10,10), fontsize=50)

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
    global score

    if game_menu:

        if keyboard.space:
            game_menu = False
            start_timer()

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
