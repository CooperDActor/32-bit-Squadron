import pygame,random,time

#values
x = 720
y = 720
px = x / 2 -50
py = y - 100
cx1 = random.randint(0,640)
cy1 = random.randint(-1000,0)
cx2 = random.randint(0,640)
cy2 = random.randint(-1000,0)
tx1 = random.randint(0,640)
ty1 = random.randint(-1000,0)
tx2 = random.randint(0,640)
ty2 = random.randint(-1000,0)
lx = random.randint(0,640)
ly = random.randint(-1000,0)
ex1 = random.randint(0,640)
ey1 = random.randint(-1000,0)
ex2 = random.randint(0,640)
ey2 = random.randint(-1000,0)
ex3 = random.randint(0,640)
ey3 = random.randint(-1000,0)
ex4 = random.randint(0,640)
ey4 = random.randint(-1000,0)
ex5 = random.randint(0,640)
ey5 = random.randint(-1000,0)
bx = random.randint(0,640)
by = random.randint(-1000,0)
prx = random.randint(0,640)
pry = random.randint(-1000,0)
spvel = 1
vel = 0.5
screen = pygame.display.set_mode((x,y))
run = True
page = "menu"
keys = pygame.key.get_pressed()

#assets
playersprite = pygame.image.load("Assets/Player.png")
enemysprite1 = pygame.image.load("Assets/BF-109.png")
enemysprite2 = pygame.image.load("Assets/Avro Lancaster.png")
enemysprite3 = pygame.image.load("Assets/Bomber.png")
enemysprite4 = pygame.image.load("Assets/Warthog.png")
enemysprite5 = pygame.image.load("Assets/Tomcat.png")
cloudsprite1 = pygame.image.load("Assets/Cloud 1.png")
cloudsprite2 = pygame.image.load("Assets/Cloud 2.png")
treesprite = pygame.image.load("Assets/Tree.png")
lakesprite = pygame.image.load("Assets/Lake.png")
parachutesprite = pygame.image.load("Assets/Parachute.png")
basesprite = pygame.image.load("Assets/Base.png")
gamelogo = pygame.image.load("Assets/32bit Squadron logo.png")
startsprite = pygame.image.load("Assets/Start.png")

pygame.init()
pygame.display.set_icon(playersprite)
pygame.display.set_caption("32bit Squadron") 

while run:
    pygame.time.Clock().tick(5000)

    keys = pygame.key.get_pressed()

    if page == "menu":
      #resets variables
      px = x / 2 -50
      py = y - 100
      ex1 = random.randint(0,640)
      ey1 = random.randint(-1000,0)
      ex2 = random.randint(0,640)
      ey2 = random.randint(-1000,0)
      ex3 = random.randint(0,640)
      ey3 = random.randint(-1000,0)
      ex4 = random.randint(0,640)
      ey4 = random.randint(-1000,0)
      ex5 = random.randint(0,640)
      ey5 = random.randint(-1000,0)
      #renders menu
      screen.fill((0,0,0))
      screen.blit(gamelogo,(113,10))
      start = screen.blit(startsprite,(260,500))
      if keys[pygame.K_SPACE]:
            page = "game"
    
    if page == "game":
        screen.fill((0,50,0))

        spvel = 1
        vel = 0.5

        #renders sprites
        screen.blit(lakesprite,(lx,ly))
        screen.blit(treesprite,(tx1,ty1))
        screen.blit(treesprite,(tx2,ty2))
        screen.blit(basesprite,(bx,by))
        screen.blit(parachutesprite,(prx,pry))
        player = screen.blit(playersprite,(px,py))
        enemy1 = screen.blit(enemysprite1,(ex1,ey1))
        enemy2 = screen.blit(enemysprite2,(ex2,ey2))
        enemy3 = screen.blit(enemysprite3,(ex3,ey3))
        enemy4 = screen.blit(enemysprite4,(ex4,ey4))
        enemy5 = screen.blit(enemysprite5,(ex5,ey5))
        screen.blit(cloudsprite1,(cx1,cy1))
        screen.blit(cloudsprite2,(cx2,cy2))

        #detects collision with sides
        if px > 640:
          px = 640
        if px < 0:
            px = 0

        #cloud movement
        if cy1 > 720:
            cx1 = random.randint(0,640)
            cy1 = random.randint(-1000,0)
        if cy2 > 720:
           cx2 = random.randint(0,640)
           cy2 = random.randint(-1000,0)
        cy1 += vel
        cy2 += vel

        #tree movement
        if ty1 > 720:
            tx1 = random.randint(0,640)
            ty1 = random.randint(-1000,0)
        if ty2 > 720:
            tx2 = random.randint(0,640)
            ty2 = random.randint(-1000,0)
        ty1 += vel
        ty2 += vel

        #Lake movement
        if ly > 720:
            lx = random.randint(0,640)
            ly = random.randint(-1000,0)
        ly += vel

        #Base movement
        if by > 720:
            bx = random.randint(0,640)
            by = random.randint(-1000,0)
        by += vel

        #parachute movement
        if pry > 720:
            prx = random.randint(0,640)
            pry = random.randint(-1000,0)
        pry += vel

        #enemy movement
        if ey1 > 720:
            ex1 = random.randint(0,640)
            ey1 = random.randint(-1000,0)
        if ey2 > 720:
            ex2 = random.randint(0,640)
            ey2 = random.randint(-1000,0)
        if ey3 > 720:
            ex3 = random.randint(0,640)
            ey3 = random.randint(-1000,0)
        if ey4 > 720:
            ex4 = random.randint(0,640)
            ey4 = random.randint(-1000,0)
        if ey5 > 720:
            ex5 = random.randint(0,640)
            ey5 = random.randint(-1000,0)
        ey1 += spvel
        ey2 += spvel
        ey3 += spvel
        ey4 += spvel
        ey5 += spvel

        #collision
        if pygame.Rect.colliderect(player,(enemy1)):
           page = "menu"
        if pygame.Rect.colliderect(player,enemy2):
           page = "menu"
        if pygame.Rect.colliderect(player,enemy3):
           page = "menu"
        if pygame.Rect.colliderect(player,enemy4):
           page = "menu"
        if pygame.Rect.colliderect(player,enemy5):
           page = "menu"

        #keybinds
        if keys[pygame.K_d]:
          px += spvel
        if keys[pygame.K_a]:
          px -= spvel
        if keys[pygame.K_RIGHT]:
          px += spvel
        if keys[pygame.K_LEFT]:
          px -= spvel
        if keys[pygame.K_p]:
            if spvel == 1:
                spvel = 0
                vel = 0
            elif spvel == 0:
                spvel = 1
                vel = 0.5
            time.sleep(0.2)

    #detects quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    pygame.display.update()
    
pygame.quit()
