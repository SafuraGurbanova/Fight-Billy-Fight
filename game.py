#pgzero
import random


WIDTH = 900 
HEIGHT = 450 

TITLE = "Fight Billy Fight" 
FPS = 70

beebs = []
beeys = []
worms = []
bullets = []
ubil = []
mode = "menu"
enemy_type = 0
enemy_count = 0 
treehealth = 100
beebhealth = 40
beeyhealth = 60
wormhealt = 80
beebattack = 5
beeyattack = 7
wormattack = 10
ggattack = 20
wave = 1 
speed = 1

fon = Actor("fo321n")
gg = Actor("up",(200,320))
tree = Actor("treeeee",(70,200))
knopka = Actor("button",(450,155))
pula = Actor("pula")
play = Actor("play",(350,170))
pause = Actor("pause",(500,170))

def beebsdraw():
    for i in range(len(beebs)):
        beebs[i].draw()
def beeysdraw():
    for i in range(len(beeys)):
        beeys[i].draw()
def wormsdraw():
    for i in range(len(worms)):
        worms[i].draw()
def bulletsdraw():
    for i in range(len(bullets)):
        bullets[i].draw()
def draw():
 
    if mode == "menu":
        fon.image = "fo321nn"
        fon.draw()
        knopka.draw()
 
    if mode == "game":
        fon.image = "fo321n"
        fon.draw()
        gg.draw()
        beebsdraw()
        beeysdraw()
        wormsdraw()
        tree.draw()
        bulletsdraw()
        screen.draw.text("HP:", center=(30, 400), color="white", fontsize = 20)
        screen.draw.text(treehealth, center=(62, 400), color="white", fontsize = 20)
    if mode == "pause":
        fon.draw()
        gg.draw()
        tree.draw()
        play.draw()
        pause.draw()
        screen.draw.text("HP:", center=(30, 400), color="white", fontsize = 20)
        screen.draw.text(treehealth, center=(62, 400), color="white", fontsize = 20)

    if mode == "lose":
        fon.image = "fo321nnn"
        fon.draw()
   
    if mode == "win":
        fon.image = "fo321nnnn"
        fon.draw()


        

def beebmove():
    if beeb.x > -20:
        beeb.x = beeb.x - 1
    else:
        beeb.x = WIDTH + 20
def beeymove():
    if beey.x > -20:
        beey.x = beey.x - 1
    else:
        beey.x = WIDTH + 20
def wormmove():
    if worm.x > -20:
        worm.x = worm.x - 1
    else:
        worm.x = WIDTH + 20
        
def beeb_move2():
    if beebs[0].x > 0:
        beebs[0].x = beebs[0].x - beebs[0].speed
    else:
        beebs.pop(0)
def beey_move():
    if beeys[0].x > 0:
        beeys[0].x = beeys[0].x - beeys[0].speed
    else:
        beeys.pop(0)
def worm_move():
    if worms[0].x > 0:
        worms[0].x = worms[0].x - worms[0].speed
    else:
        worms.pop(0)
        
def beebs_collide():
    global treehealth
    global beebhealth
    for i in range(len(bullets)):
       st = bullets[i].collidelist(beebs)
       if st!=-1:
           bullets.pop(i)
           beebs.pop(st)
           ubil.append(1)
           break
    for a in range(len(beebs)):
        dd = tree.collidelist(beebs)
        if dd!=-1:
            treehealth -= beebattack
            beebs.pop(dd)
            break

def beeys_collide():
    global treehealth
    for i in range(len(bullets)):
       bb = bullets[i].collidelist(beeys)
       if bb!=-1:
           bullets.pop(i)
           beeys.pop(bb)
           ubil.append(1)
           break
    for a in range(len(beeys)):
       ww = tree.collidelist(beeys)
       if ww!=-1:
            treehealth -= beeyattack
            beeys.pop(ww)
            break
def worms_collide():
    global treehealth
    for i in range(len(bullets)):
       dd = bullets[i].collidelist(worms)
       if dd!=-1:
           bullets.pop(i)
           worms.pop(dd)
           ubil.append(1)
           break
    for a in range(len(worms)):
       qq = tree.collidelist(worms)
       if qq!=-1:
            treehealth -= wormattack
            worms.pop(qq)
            break
        
def movement():
    if keyboard.right or keyboard.d and gg.x < 680:
            gg.x = gg.x + 5
            gg.image = 'up'
    if keyboard.left or keyboard.a and gg.x > 20:
            gg.x = gg.x - 5
            gg.image = 'left'
def bulletsmove():
    for i in range(len(bullets)):
        if bullets[i].x > 900:
            bullets.pop(i)
            break
        else:
            bullets[i].x = bullets[i].x + 5
            bullets[i].y = bullets[i].y + bullets[i].dy
def move_ment():
    global enemy_type
    if enemy_type == 0 and len(beebs)>0:
        beeb_move2()
        if len(beebs) == 0:
            enemy_type = 1
    if enemy_type == 0 and len(beeys)>0:
        beey_move()
        if len(beeys) == 0:
            enemy_type = 1
    if enemy_type == 0 and len(worms)>0:
        worm_move()
        if len(worms) == 0:
            enemy_type = 1
            
def enemies():
    global wave
    global mode
    global ubil
    if wave == 1 and len(ubil) == 9:
        mode = "pause"
        ubil = []
    if wave == 2 and len(ubil) == 15:
        mode = "pause"
        ubil = []
    if wave == 3 and len(ubil) == 21:
        mode = "pause"
        ubil = []
    if len(ubil) < 9 and wave == 1 and len(beebs) == 0 and len(beeys) == 0 and len(worms) == 0 :
        for i in range(3):
            y = random.randint(100, 310)
            beeb = Actor("beef", (920, y))
            beeb.speed = speed
            beebs.append(beeb)
        for i in range(3):
            y = random.randint(100, 310)
            beey = Actor("beeo", (970, y))
            beey.speed = speed
            beeys.append(beey)
        for i in range(3):
            worm = Actor("worm", (1000, 320))
            worm.speed = speed
            worms.append(worm)
    if len(ubil) < 15 and wave == 2 and len(beebs) == 0 and len(beeys) == 0 and len(worms) == 0 :
        for i in range(5):
            y = random.randint(100, 310)
            beeb = Actor("beef", (920, y))
            beeb.speed = speed
            beebs.append(beeb)
        for i in range(5):
            y = random.randint(100, 310)
            beey = Actor("beeo", (970, y))
            beey.speed = speed
            beeys.append(beey)
        for i in range(5):
            worm = Actor("worm", (1000, 320))
            worm.speed = speed
            worms.append(worm)
    if len(ubil) < 21 and wave == 3 and len(beebs) == 0 and len(beeys) == 0 and len(worms) == 0 :
        for i in range(7):
            y = random.randint(100, 310)
            beeb = Actor("beef", (920, y))
            beeb.speed = speed
            beebs.append(beeb)
        for i in range(7):
            y = random.randint(100, 310)
            beey = Actor("beeo", (970, y))
            beey.speed = speed
            beeys.append(beey)
        for i in range(7):
            worm = Actor("worm", (1000, 320))
            worm.speed = speed
            worms.append(worm)
        
        
        
        
        
def update(dt):
    global enemy_type
    global treehealth
    global mode
    if mode == "about":
        beebmove()
        beeymove()
        wormmove()
    if mode == "game":
        movement()
        move_ment()
        beebs_collide()
        beeys_collide()
        worms_collide()
        bulletsmove()
        enemies()
        if treehealth < 0 or treehealth == 0:
            mode = "lose"
        if wave == 4:
            mode ="win"



    
def on_mouse_down(button, pos):
    global mode 
    global wave
    global speed
    global ggattack

    if button == mouse.LEFT and mode == "game":
        bullet = Actor("pula")
        bullet.x = gg.x
        bullet.y = gg.y 
        shag = (pos[0] - gg.x) // 5
        dy = (pos[1] - gg.y) // shag
        bullet.dy = dy
        bullets.append(bullet)
    if button == mouse.LEFT and mode == "menu":
        if knopka.collidepoint(pos):
            mode = "game"
    if button == mouse.LEFT and mode == "pause":
        if play.collidepoint(pos):
            wave += 1
            speed += 3
            ggattack += 10
            mode = "game"
        if pause.collidepoint(pos):
            wave += 1
            speed += 3
            ggattack += 10
            mode = "menu"
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        gg.image = "up"
        gg.y = 280
        animate(gg, tween='bounce_end', duration=1, y=320)
print(ubil)
print(beebs)

        
    
