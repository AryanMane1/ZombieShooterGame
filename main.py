'''
    Author: Aryan
    Date: 23 March 2021
    Purpose: Making a shooter game
'''
import pygame , sys , pygame.display , pygame.event , pygame.time , pygame.draw , pygame.font , pygame.mixer 
import pygame.image , pygame.mouse , pygame.transform , random , os , tkinter  , tkinter.messagebox
from pygame.locals import *
import pygame

def resize(image,width,height):
    return pygame.transform.scale( image ,(width,height))

def get_zombie():
    global player_X_pos
    zombieX = random.randint(100,SCREEN_WIDTH-200)
    type = random.choice([1,2,3,4,1,2,2,1,2,1,2,1,5,1,2,2,1,1,1,1,1,1,3,4,5,6])
    return [zombieX,-50,type]

bar_Y = 0
def Board():
    global Total_money,current_kill,health_persantage,bar_Y
    font_size = 40
    SCREEN.blit(resize(bomb_img,30,39),(0,0))
    screen_text(f"{Total_bomb:,}",font_size,white,35,10)

    SCREEN.blit(resize(kill_img,33,39),(SCREEN_WIDTH-33,0))
    screen_text(f"{current_kill:,}",font_size,white,SCREEN_WIDTH-43-len(str(current_kill))*15,7)

    SCREEN.blit(resize(rocket_img,30,35),(0,SCREEN_HEIGHT-40))
    screen_text(f"{Total_rocket:,}",font_size,white,38,SCREEN_HEIGHT-32)

    SCREEN.blit(resize(money_img,40,45),(SCREEN_WIDTH-45,SCREEN_HEIGHT-50))
    screen_text(f"{current_money:,}",font_size,white,SCREEN_WIDTH-50-len(str(current_money))*15,SCREEN_HEIGHT-40)
  
    bar_Y = (health_persantage*2)
    pygame.draw.rect(SCREEN,black,(20,150,5,200),2) # 150 - 350
    pygame.draw.rect(SCREEN,red,(20,350-bar_Y,5, bar_Y))

    SCREEN.blit(resize(heart_img,43,43),(5,362))

    screen_text(f"{health_persantage}%",23,white,13,378)

def screen_text(text,font_size,colour,x,y):
        '''
        text,font_size,colour,x,y
        '''
        font = pygame.font.SysFont(None, font_size-5,bold=True)
        # font = pygame.font.get_fonts()[1]
        TEXT = font.render(text,True,colour)
        SCREEN.blit(TEXT,[x,y])

def profile():
    global Character
    X,Y = 0,0
    while True:
        SCREEN.blit((resize(homebg_img,SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))
        for env in pygame.event.get():
                if env.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  

                if env.type == MOUSEBUTTONDOWN:
                    X = pygame.mouse.get_pos()[0]
                    Y = pygame.mouse.get_pos()[1]
    
        SCREEN.blit((resize(boy_profile_img,200,200)),(150,100))
        SCREEN.blit((resize(girl_profile_img,200,200)),(150,340))

        if 187<X<314 and 122<Y<270:
            Character = "boy"
            break
        if 183<X<314 and 370<Y<517:
            Character = "girl"
            break
        pygame.display.update()
        CLOCK.tick(30)

def buy_weapon(): 
    global Total_bomb , Total_rocket , Total_money , Total_kill , Character
    X,Y=0,0

    while True:
        SCREEN.blit((resize(homebg_img,SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))
        for env in pygame.event.get():
                if env.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  

                if env.type == MOUSEBUTTONDOWN:
                    X = pygame.mouse.get_pos()[0]
                    Y = pygame.mouse.get_pos()[1]
       
        SCREEN.blit((resize(money_img,50,50)),(180,345))
        screen_text(str(f"{Total_money:,}"),40,white,238,355)

        pygame.draw.line(SCREEN,white,(0,SCREEN_HEIGHT-130),(SCREEN_WIDTH,SCREEN_HEIGHT-130),8)

        SCREEN.blit((resize(backward_img,60,80)),(10,SCREEN_HEIGHT-100))

        SCREEN.blit((resize(wooden_img,160,80)),(100,SCREEN_HEIGHT-100))

        SCREEN.blit((resize(wooden_img,160,80)),(300,SCREEN_HEIGHT-100))

        SCREEN.blit((resize(bomb_img,28,34)),(360,SCREEN_HEIGHT-94))
        screen_text(f"Total {Total_bomb:,}",30,black,330,SCREEN_HEIGHT-50)

        SCREEN.blit((resize(rocket_img,30,40)),(160,SCREEN_HEIGHT-94))
        screen_text(f"Total {Total_rocket:,}",30,black,130,SCREEN_HEIGHT-50)

        dist = 1
        price = "20,000"
        num = 100
        get_1 = False
        for i in range(1,4):
            if i==2:dist,price,num=170,"1,50,000","1,000"
            if i==3:dist,price,num=340,"10,00,000","10,000"
              
            SCREEN.blit((resize(wooden_img,150,110)),(0+dist,210))
            SCREEN.blit((resize(bomb_img,40,50)),(10+dist,220))
            screen_text(f"x {num}",32,black,54+dist,230)
            screen_text(f"{price} Rs.",30,black,30+dist,280)

            if Total_money <= int(price.replace(",","")):
                SCREEN.blit(resize(lock_img,80,80),(0+dist+30,210))
                get_1 = True

        get_2 = False
        dist = 1
        price = "10,000"
        num = 500
        for i in range(1,4):
            if i==2:dist,price,num=170,"90,000","5,000"
            if i==3:dist,price,num=340,"9,50,000","50,000"

            SCREEN.blit((resize(wooden_img,150,110)),(0+dist,420))
            SCREEN.blit((resize(rocket_img,40,50)),(10+dist,430))
            screen_text(f"x {num}",32,black,55+dist,440)
            screen_text(f"{price} Rs.",30,black,30+dist,490)

            if Total_money <= int(price.replace(",","")):
                SCREEN.blit(resize(lock_img,80,80),(0+dist+30,420)) 
                get_2 = False
            else:True

        # Bomb
        if 9<X<139 and 216<Y<305 and Total_money >= 20000:
            Total_bomb+=100
            Total_money-=20000
            X,Y = 0,0

        if 182<X<312 and 216<Y<305 and Total_money >= 90000:
            Total_bomb+=1000
            Total_money-=90000
            X,Y = 0,0

        if 350<X<481 and 216<Y<305 and Total_money >=1000000:
            Total_bomb+=10000
            Total_money-=1000000
            X,Y = 0,0
        # Rocket
        if 9<X<139 and 428<Y<518  and Total_money >= 10000:
            Total_rocket+=500
            Total_money-=10000
            X,Y = 0,0

        if 182<X<312 and 428<Y<518 and Total_money >= 90000:
            Total_rocket+=5000
            Total_money-=90000
            X,Y = 0,0

        if 350<X<481 and 427<Y<518 and Total_money >= 1200000:
            Total_rocket+=50000
            Total_money-=950000
            X,Y = 0,0

        # Back
        if 25<X<63 and 605<Y<674:
            with open("info.txt","w") as f:
                f.write(f"{Total_kill}\n{Total_money}\n{Character}\n{Total_rocket}\n{Total_bomb}\n{Highest_kill}")
            return 0

        pygame.display.update()
        CLOCK.tick(30)

def reset():
    global Total_kill ,Total_money,Character ,Total_rocket ,Total_bomb ,  player_X_pos ,zombie_pos_Y ,All_bullets,All_zombie,All_rockets,All_bombs,All_notes,All_bag,fire_time ,game_time , player_img, zombie_img,page_num,X_pos,current_kill,current_money,health_persantage,X,Y


    player_X_pos = 300
    zombie_pos_Y = 0
    All_bullets = []
    All_zombie = []
    All_rockets = []
    All_bombs = []
    All_notes = []
    All_bag = []
    fire_time = 0
    game_time = 0
    player_img = player1_img


    zombie_img = random.choice([zombie1_img,zombie2_img])
    page_num = 1
    X_pos = 0
    current_kill = 0
    current_money = 0
    health_persantage = 100

    with open("info.txt","r") as f:
        Total_kill = int(f.readline().replace("\n",""))
        Total_money = int(f.readline().replace("\n",""))
        Character = f.readline().replace("\n","")
        Total_rocket = int(f.readline().replace("\n",""))
        Total_bomb = int(f.readline().replace("\n",""))
    X,Y=0,0

def game_over():
    global Highest_kill

    over_Y = 80
    up = False
    down = True
    while True:
        SCREEN.blit((resize(BG_img,SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))

        for env in pygame.event.get():
                if env.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  

                if env.type == MOUSEBUTTONDOWN:
                    health_persantage = 100
                    if Highest_kill < current_kill:
                        Highest_kill = current_kill
                    with open("info.txt","w") as f:
                        f.write(f"{current_kill+Total_kill}\n{current_money+Total_money}\n{Character}\n{Total_rocket}\n{Total_bomb}\n{Highest_kill}")
                    reset()
                    return 0

        SCREEN.blit((resize(game_over_img,300,200)),(100,over_Y))
        screen_text("!! Tap here to continue game !!",46,black,10,over_Y+430)
        if up:over_Y-=1
        elif down:over_Y+=1

        if over_Y>=100:
            down=False
            up = True
        if over_Y<=50:
            down=True
            up = False
                    
        SCREEN.blit((resize(money_img,50,50)),(180,345))
        screen_text(str(f"{current_money:,}"),45,black,240,355)

        SCREEN.blit((resize(kill_img,50,50)),(180,400))
        screen_text(str(f"{current_kill:,}"),45,black,240,410)
        pygame.display.update()
        CLOCK.tick(32)
        


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

if __name__ == '__main__':
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Zombie attack by Aryan")
    CLOCK = pygame.time.Clock()

    #---------------- Images initialize -----------

    BG_img = pygame.image.load("gallary/images/back1.jpg").convert_alpha()
    player1_img =pygame.image.load("gallary/images/shoot3.png").convert_alpha()
    bullet_img = pygame.image.load("gallary/images/bullet.png").convert_alpha()
    bullet_spark_img = pygame.image.load("gallary/images/bulletspark.png").convert_alpha()
    bomb_img = pygame.image.load("gallary/images/bomb.png").convert_alpha()
    rocket_img = pygame.image.load("gallary/images/rocket.png").convert_alpha()
    blast_img = pygame.image.load("gallary/images/blast.png").convert_alpha()
    zombie1_img = pygame.transform.rotate(pygame.image.load("gallary/images/zombie1.png").convert_alpha(),180)
    zombie2_img = pygame.transform.rotate(pygame.image.load("gallary/images/zombie2.png").convert_alpha(),180)
    zombie6_img = pygame.transform.rotate(pygame.image.load("gallary/images/zombie6.png").convert_alpha(),180)
    welcome_zombie_img = pygame.image.load("gallary/images/welcome_zombie.png").convert_alpha()
    title_img = pygame.image.load("gallary/images/title.png").convert_alpha()
    homebg_img = pygame.image.load("gallary/images/homebg.png").convert_alpha()
    boy_profile_img = pygame.image.load("gallary/images/boy.png").convert_alpha()
    girl_profile_img = pygame.image.load("gallary/images/girl.png").convert_alpha()
    backward_img = pygame.image.load("gallary/images/goback.png").convert_alpha()
    money_img = pygame.image.load("gallary/images/money.png").convert_alpha()
    kill_img = pygame.image.load("gallary/images/kill2.png").convert_alpha()
    start_img = pygame.image.load("gallary/images/start.png").convert_alpha()
    buy_weapon_img = pygame.image.load("gallary/images/buy_weapon.png").convert_alpha()
    wooden_img = pygame.image.load("gallary/images/wooden.png").convert_alpha()
    big_board_img = pygame.image.load("gallary/images/bigboard.png").convert_alpha()
    blood_img = pygame.image.load("gallary/images/blood.png").convert_alpha()
    lock_img = pygame.image.load("gallary/images/lock.png").convert_alpha()
    heart_img = pygame.image.load("gallary/images/heart.png").convert_alpha()
    player_blood_img = pygame.image.load("gallary/images/player_blood.png").convert_alpha()
    money_bag_img = pygame.image.load("gallary/images/money_bag.png").convert_alpha()
    money_note_img = pygame.image.load("gallary/images/money_note.png").convert_alpha()
    game_over_img = pygame.image.load("gallary/images/game_over.png").convert_alpha()
    zombie3_img = pygame.image.load("gallary/images/zombie3.png").convert_alpha()
    zombie4_img = pygame.image.load("gallary/images/zombie4.png").convert_alpha()
    zombie5_img = pygame.image.load("gallary/images/zombie5.png").convert_alpha()

    #------------------ Sounds Initialize ----------------

    bullet_sound = pygame.mixer.Sound('gallary/sounds/bullet.mp3')
    kill_sound = pygame.mixer.Sound('gallary/sounds/kill.mp3')
    reload_sound = pygame.mixer.Sound('gallary/sounds/reload.mp3')
    rocket_sound = pygame.mixer.Sound('gallary/sounds/rocket.mp3')
    zombie_sound = pygame.mixer.Sound('gallary/sounds/zombie.mp3')
    explosion_sound = pygame.mixer.Sound('gallary/sounds/Explosion.mp3')


    player_X_pos = 300
    zombie_pos_Y = 0
    All_bullets = []
    All_zombie = []
    All_rockets = []
    All_bombs = []
    All_notes = []
    All_bag = []
    fire_time = 0
    game_time = 0
    player_img = player1_img

    zombie_img = random.choice([zombie1_img,zombie2_img])
    page_num = 1
    X_pos = 0
    Total_kill = 0
    Total_money =0
    Character = ""
    Total_rocket =0
    Total_bomb = 0
    Highest_kill = 0
    current_kill = 0
    current_money = 0
    health_persantage = 100
#--------- ingo.txt variables
    if os.path.exists("info.txt") == False:
        with open("info.txt","w") as f:
            f.write("0\n0\nboy\n0\n0\n0")

    with open("info.txt","r") as f:
        Total_kill = int(f.readline().replace("\n",""))
        Total_money = int(f.readline().replace("\n",""))
        Character = f.readline().replace("\n","")
        Total_rocket = int(f.readline().replace("\n",""))
        Total_bomb = int(f.readline().replace("\n",""))
        Highest_kill = int(f.readline().replace("\n",""))

    X,Y=0,0
   
    while True:

        if page_num == 1:
            SCREEN.blit((resize(BG_img,SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))

            for env in pygame.event.get():
                if env.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
            Key = pygame.key.get_pressed()

            pygame.draw.rect(SCREEN,black,(120,660,X_pos,20))
            screen_text(f"Loading...  {int(X_pos/2.3)}%",30,black,180,630)
         
            if X_pos >= 230:
                page_num=2
            X_pos+=6

            SCREEN.blit((resize(welcome_zombie_img,350,350)),(80,220))
            SCREEN.blit((resize(title_img,400,230)),(50,0))


        if page_num == 2:
            for env in pygame.event.get():
                if env.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  

                if env.type == MOUSEBUTTONDOWN:
                    X = pygame.mouse.get_pos()[0]
                    Y = pygame.mouse.get_pos()[1]
    

            SCREEN.blit((resize(homebg_img,SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))
            SCREEN.blit((resize(title_img,300,150)),(100,10))
            if Character == "boy" :SCREEN.blit((resize(boy_profile_img,150,150)),(180,170))
            elif Character == 'girl':SCREEN.blit((resize(girl_profile_img,150,150)),(180,170))


            SCREEN.blit((resize(wooden_img,160,80)),(0,230))
            SCREEN.blit((resize(bomb_img,35,40)),(10,250))
            screen_text(f"{Total_bomb:,}",35,black,50,255)

            SCREEN.blit((resize(wooden_img,160,80)),(SCREEN_WIDTH-160,230))
            SCREEN.blit((resize(rocket_img,35,45)),(SCREEN_WIDTH-150,245))
            screen_text(f"{Total_rocket:,}",35,black,SCREEN_WIDTH-110,255)

            SCREEN.blit((resize(wooden_img,200,130)),(160,350))
            SCREEN.blit((resize(kill_img,30,35)),(230-(5*len(str(Total_kill+1))),360))
            screen_text(str(f"{Total_kill:,}"),35,black,265-(5*len(str(Total_kill+1))),365)

            SCREEN.blit((resize(money_img,45,45)),(225-(5*len(str(Total_money+1))),400))
            screen_text(str(f"{Total_money:,}"),35,black,275-(5*len(str(Total_money+1))),410)

            screen_text(f"Highest Kill: {Highest_kill}",31,black,200-len(str(Highest_kill))*5,452)
            
            SCREEN.blit(resize(buy_weapon_img,buy_weapon_img.get_width()+5,buy_weapon_img.get_height()+5),(130,500))

            SCREEN.blit((resize(start_img,200,100)),(150,580))

            screen_text(f"{Character.capitalize()}",35 ,white,230,323)
            # print(X,Y)
            if 207<X<300 and 193<Y<300:
                profile()
                X,Y = 0,0

            if 137<X<377 and 496<Y<550:
                buy_weapon()
                with open("info.txt","r") as f:
                    Total_kill = int(f.readline().replace("\n",""))
                    Total_money = int(f.readline().replace("\n",""))
                    Character = f.readline().replace("\n","")
                    Total_rocket = int(f.readline().replace("\n",""))
                    Total_bomb = int(f.readline().replace("\n",""))
                    Highest_kill = int(f.readline().replace("\n",""))
                X,Y = 0,0

            if 165<X<339 and 593<Y<655:
                page_num = 3
                X,Y = 0,0


        if page_num == 3:

            for env in pygame.event.get():
                if env.type == pygame.QUIT:
                    if Highest_kill < current_kill:
                        Highest_kill = current_kill
                    with open("info.txt","w") as f:
                        f.write(f"{Total_kill}\n{Total_money}\n{Character}\n{Total_rocket}\n{Total_bomb}\n{Highest_kill}")
                    pygame.quit()
                    sys.exit()  

            SCREEN.blit((resize(BG_img,SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))
            SCREEN.blit((resize(player_img,100,140)),(player_X_pos,SCREEN_HEIGHT-150))

            #Game over
            if health_persantage <= 1:
               game_over()


            # Main Game
            else:
                # --------------- Zombie sound
                if game_time%100==0:
                    zombie_sound.set_volume(1)
                    pygame.mixer.Channel(5).play(zombie_sound)

                if Highest_kill < current_kill:
                        Highest_kill = current_kill

                # ----------------- handling zombies
                if game_time%10==0:
                    All_zombie.append(get_zombie())
                    zombie_pos_Y=5

                if game_time > 10000:
                    if game_time%1==0:
                        All_zombie.append(get_zombie())
                        zombie_pos_Y=1

                elif game_time > 7000:
                    if game_time%3==0:
                        All_zombie.append(get_zombie())
                        zombie_pos_Y+=2

                elif game_time > 2000:
                    if game_time%4==0:
                        All_zombie.append(get_zombie())
                        zombie_pos_Y=3

                elif game_time > 1000:
                    if game_time%5==0:
                        All_zombie.append(get_zombie())
                        zombie_pos_Y=4  

                for note in All_notes:
                    SCREEN.blit(resize(money_note_img,50,40),(note[0],note[1]))    
                    note[1]+=15               
                    note[0]+=7 
                    if note[0]>SCREEN_WIDTH-20 or note[1]>SCREEN_HEIGHT-10:
                        current_money+=10
                        All_notes.remove(note)  

                for bag in All_bag:
                    SCREEN.blit(resize(money_bag_img,90,90),(bag[0],bag[1]))    
                    bag[1]+=15               
                    bag[0]+=7 
                    if bag[0]>SCREEN_WIDTH-20 or bag[1]>SCREEN_HEIGHT-10:
                        current_money+=10
                        All_bag.remove(bag)                 

                i = 0
                for zombie in All_zombie:
                    if zombie[2] == 1:
                        SCREEN.blit((resize(zombie1_img,70,60)),(zombie[0],zombie[1]))
                        zombie[1]=zombie_pos_Y+zombie[1]
                    elif zombie[2] == 2:
                        SCREEN.blit((resize(zombie2_img,70,60)),(zombie[0],zombie[1]))
                        zombie[1]=zombie_pos_Y+zombie[1]
                    elif zombie[2] == 3:
                        SCREEN.blit((resize(zombie3_img,90,100)),(zombie[0],zombie[1]))
                        zombie[1]=zombie_pos_Y+zombie[1]+7
                    elif zombie[2] == 4:
                        SCREEN.blit((resize(zombie4_img,90,120)),(zombie[0],zombie[1]))
                        zombie[1]=zombie_pos_Y+zombie[1]+10
                    elif zombie[2] == 5:
                        SCREEN.blit((resize(zombie5_img,90,120)),(zombie[0],zombie[1]))
                        zombie[1]=zombie_pos_Y+zombie[1]+10
                    elif zombie[2] == 6:
                        SCREEN.blit((resize(zombie6_img,90,120)),(zombie[0],zombie[1]))
                        zombie[1]=zombie_pos_Y+zombie[1]+30

                    # Game Over
                    if zombie[1]>SCREEN_HEIGHT-180 and player_X_pos-50<zombie[0]<player_X_pos+100:
                        for i in range(2):
                            SCREEN.blit((resize(player_blood_img,100,100)),(zombie[0]+10,zombie[1]+10))
                            pygame.display.update()
                        health_persantage-=10
                        All_zombie.remove(zombie)
                    i+=1
                    if zombie[1]>SCREEN_HEIGHT:
                        health_persantage-=1
                        try:All_zombie.remove(zombie)
                        except:pass

                # Killing zombie in BULLETS
                for bullet in All_bullets:
                    for zombie in All_zombie:
                        if zombie[0] < bullet[0] < zombie[0]+zombie_img.get_width()-100 and zombie[1] < bullet[1] < zombie[1]+zombie_img.get_height()-120:
                            All_notes.append([zombie[0]+10,zombie[1]+10])
                            
                            try:

                                All_bullets.remove(bullet)
                                All_zombie.remove(zombie)
                            except:pass
                            current_kill+=1
                            kill_sound.set_volume(1)
                            pygame.mixer.Channel(0).play(kill_sound)
                            
                # Killing zombie in Rockets
                for rocket in All_rockets:
                    for zombie in All_zombie:
                        if zombie[0] < rocket[0] < zombie[0]+zombie_img.get_width()-100 and zombie[1] < rocket[1] < zombie[1]+zombie_img.get_height()-120:
                            try:
                                All_rockets.remove(rocket)
                                All_zombie.remove(zombie)
                            except:pass
                            blast_X = zombie[0]
                            blast_Y = int(zombie[1])-110
                            SCREEN.blit((resize(blast_img,150,150)),(blast_X,blast_Y))
                            for Z in All_zombie:
                                if blast_X < Z[0] < blast_X+blast_img.get_width() and blast_Y < Z[1] < blast_Y+blast_img.get_height():
                                    SCREEN.blit((resize(blood_img,50,50)),(Z[0]+10,Z[1]+10))
                                    All_zombie.remove(Z)
                                    All_notes.append([zombie[0]+10,zombie[1]+10])
                                    current_money+=10
                                    current_kill+=1 
                                    kill_sound.set_volume(1)
                                    pygame.mixer.Channel(1).play(kill_sound)
                # Killing Bomb     
                for bomb in All_bombs:
                    for zombie in All_zombie:
                        if zombie[0] < bomb[0] < zombie[0]+zombie_img.get_width()-100 and zombie[1] < bomb[1] < zombie[1]+zombie_img.get_height()-120:
                            try:
                                All_bombs.remove(bomb)
                                All_zombie.remove(zombie)
                            except:pass
                            blast_X = zombie[0]-500
                            blast_Y = int(zombie[1])- 400
                            explosion_sound.set_volume(1)
                            pygame.mixer.Channel(6).play(explosion_sound)
                            for i in range(3):
                                SCREEN.blit((resize(blood_img,50,50)),(zombie[0]+10,zombie[1]+10))
                                SCREEN.blit((resize(blast_img,600,600)),(0,blast_Y-200))
                                pygame.display.update()
                            num = 0
                            for Z in All_zombie:
                                if blast_X < Z[0] < blast_X+900 and blast_Y < Z[1] < blast_Y+900:
                                    All_zombie.remove(Z)
                                    current_kill+=1 
                                    kill_sound.set_volume(1)
                                    pygame.mixer.Channel(1).play(kill_sound)
                                    num+=1
                                    All_notes.append([Z[0]+10,Z[1]+10])
                            if num>6:
                                All_bag.append([zombie[0]+10,zombie[1]+10])
                                current_money+=100

                #Handling events
        
                Key = pygame.key.get_pressed()

                if Key[K_LEFT]:
                    if player_X_pos>80: player_X_pos-=7

                elif Key[K_RIGHT]:
                    if player_X_pos<SCREEN_WIDTH-170:player_X_pos+=7

                if (Key[K_RSHIFT] or Key[K_LSHIFT]) and Total_bomb!=0:
                    fire_time+=1

                    if fire_time%5 == 0:
                        Total_bomb-=1
                        Bomb_X = player_X_pos+10
                        Bomb_Y = SCREEN_HEIGHT-100
                        Degree = 0
                        All_bombs.append([Bomb_X,Bomb_Y,0])
                        fire_time=0

                if Key[K_UP]:
                    fire_time+=1
                    player_img=player1_img                                                                                                                                  
                    if game_time%50 == 0 and game_time!=0:
                        reload_sound.set_volume(0.5)
                        pygame.mixer.Channel(7).play(reload_sound)
                        fire_time=0

                    if fire_time == 5:
                        bullet_sound.set_volume(0.5)
                        pygame.mixer.Channel(2).play(bullet_sound)
                        bullet_x1 = int(player_X_pos+player_img.get_width()/2)
                        All_bullets.append([bullet_x1-11,SCREEN_HEIGHT-160])
                        fire_time=0
                        SCREEN.blit((resize(bullet_spark_img,25,25)),(bullet_x1-25,SCREEN_HEIGHT-170))
                    

                elif Key[K_SPACE] and Total_rocket!=0:
                    player_img = player1_img
                    fire_time+=1
                    if fire_time == 5:
                        rocket_sound.set_volume(0.5)
                        pygame.mixer.Channel(3).play(rocket_sound)
                        Total_rocket-=1        
                        bullet_x2 = int(player_X_pos+player_img.get_width()/2)
                        All_rockets.append([bullet_x2-18,SCREEN_HEIGHT-160])
                        fire_time=0
                        SCREEN.blit((resize(bullet_spark_img,45,45)),(bullet_x2-20,SCREEN_HEIGHT-170))

                # Bomb
                for bomb in All_bombs:
                    SCREEN.blit(pygame.transform.rotate(resize(bomb_img,20,30),bomb[2]),(bomb[0],bomb[1]))   
                    bomb[1]-=15
                    bomb[2]-=random.randint(5,15)
                
                    if bomb[2]>360:
                        bomb[2]=0
                    if bomb[1]<0:
                        All_bombs.remove(bomb)

                # Handling Bullets
                for bullet in All_bullets:
                    SCREEN.blit((resize(bullet_img,7,20)),(bullet[0],bullet[1]))   
                    bullet[1]-=10
                    if bullet[1]<0:
                        All_bullets.remove(bullet)

                #Rockets 
                for rocket in All_rockets:
                    SCREEN.blit((resize(rocket_img,20,30)),(rocket[0],rocket[1]))   
                    rocket[1]-=10
                    if rocket[1]<0:
                        All_rockets.remove(rocket)
                Board()

            game_time+=1
        
        
        
        pygame.display.update()
        CLOCK.tick(32)
