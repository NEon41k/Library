import pygame
from pygame import *
#створи вікно гри
win = display.set_mode((900,575))
display.set_caption("Лабіринт")
#задай фон сцени

a = 0

scene = "menu"
scene_lvl = "lvl1"

money = 100

play = True

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.player_image = player_image
        self.image = transform.scale(image.load(self.player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))


class Helper(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,text1,text2,text3):
        super().__init__(player_image,player_x,player_y,player_speed)
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
    def show_help1(self):
        font.init()
        help1 = font.Font(None,15).render(self.text1,True,(0,0,0))
        help2 = font.Font(None,15).render(self.text2,True,(0,0,0))
        help3 = font.Font(None,15).render(self.text3,True,(0,0,0))
        helper_txt = transform.scale(image.load("txt_board.png"),(110,100))
        win.blit(help1,(102,52))
        win.blit(help2,(102,62))
        win.blit(help3,(102,72))
        win.blit(helper_txt,(90,30))
helper1 = Helper("helper.png",180,90,0,"Привіт, я твій помічник","для того щоб рухатися ","використовуй кнопки W A S D")


class Player(GameSprite):
        direction = None
        def update(self):
            if key.get_pressed()[K_d] and self.rect.x <= 900 - 80:
                self.rect.x += self.speed
                self.direction = "right" 
            if key.get_pressed()[K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
                self.direction = "left" 
            if key.get_pressed()[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed     
            if key.get_pressed()[K_s] and self.rect.y <= 580 - 80:
                self.rect.y += self.speed   
            if key.get_pressed()[K_q]:
                helper1.show_help1()
player = Player("sprite_right.png",100,100,3)   
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 380:
            self.direction = "right"
        if self.rect.x >= 700:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
enemy = Enemy("enemy.png",700,190,3)



#enemy_right = Enemy("enemy_right.png",200,200,3)

class Wall (sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_width,wall_height,wall_x,wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((wall_width,wall_height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Treasure():
    def __init__(self,money,tr_x,tr_y,img,size_x,size_y):
        self.money = money
        self.size_x = size_x
        self.size_y = size_y
        self.img = transform.scale(image.load(img),(size_x,size_y))
        self.rect = self.img.get_rect()
        self.rect.x = tr_x
        self.rect.y = tr_y
        
    def show_tr(self):
        win.blit(self.img,(self.rect.x,self.rect.y))

queen = Treasure(20,600,70,"queen.png",70,70)
gold = Treasure(20,805,5,"treasure.png",70,70)
mony = Treasure(20,805,5,"treasure.png",70,70)
class Button ():
    def __init__(self,height,width,x,y,color,button_text,font_size,indentation_y,indentation_x,pay,btn_img):
        self.height = height
        self.width = width 
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.width, self.height)
        self.button_text = button_text
        self.font_size = font_size
        self.identation_y = indentation_y
        self.indentation_x = indentation_x
        self.btn_pay = pay
        self.btn_img = btn_img
    def draw_btn(self,win):
        pygame.draw.rect(win,self.color,self.rect)
        font.init()
        btn_txt = font.Font(None,self.font_size).render(self.button_text,True,(0,0,0))
        win.blit(btn_txt,(self.x + self.indentation_x,self.y + self.identation_y)) 
#   #  #     #  # # # #  # # # # #  #   #  #      #
#  #   #     #  #     #  #       #  #  #   #    # #
# #    # # # #  #     #  #       #  # #    #   #  #
# #    # # # #  #     #  #       #  # #    #  #   #
#  #   #     #  #     #  #       #  #  #   # #    #
#   #  #     #  # # # #  #       #  #   #  #      #
btn_ex = Button(50,50,830,30,(250,250,50),"==>",30,12,5,0,None)
btn_buy_sound1 = Button(50,100,125,180,(250,250,50),"20 COINT",30,12,2,20,None)
btn_buy_sound2 = Button(50,100,425,180,(250,250,50),"20 COINT",30,12,2,20,None)
btn_buy_sound3 = Button(50,100,725,180,(250,250,50),"20 COINT",30,12,2,20,None)

btn_buy_skin1 = Button(50,100,125,340,(250,250,50),"5 COINT",30,12,9,5,"sprite_right.png")
btn_buy_skin2 = Button(50,100,425,340,(250,250,50),"5 COINT",30,12,9,5,"archer_right.png")
btn_buy_skin3 = Button(50,100,725,340,(250,250,50),"5 COINT",30,12,9,5,"wizard_rigth.png")

btn_buy_bck1 = Button(50,100,125,490,(250,250,50),"25 COINT",30,12,2,25,None)
btn_buy_bck2 = Button(50,100,425,490,(250,250,50),"25 COINT",30,12,2,25,None)
btn_buy_bck3 = Button(50,100,725,490,(250,250,50),"25 COINT",30,12,2,25,None)

skin1 = transform.scale(image.load("sprite.png"),(75,75))
skin2 = transform.scale(image.load("archer.png"),(75,75))
skin3 = transform.scale(image.load("wizard.png"),(75,75))

btn_play = Button(70,190,380,120,(250,250,50),"PLAY",70,12,33,0,None)  
btn_shop = Button(70,190,380,270,(250,250,50),"SHOP",70,12,25,0,None)  
btn_help = Button(70,190,380,420,(250,250,50),"HELP",70,12,33,0,None)

clock = time.Clock()
FPS = 60

background_shop = transform.scale(image.load("background_shop.jpg"),(900,575))
background = transform.scale(image.load("background.jpg"),(900,575))
background_menu =  transform.scale(image.load("background_menu1.png"),(900,575)) 
background_menu2 =  transform.scale(image.load("background_menu_2.png"),(900,575))
background_help =  transform.scale(image.load("background_menu.png"),(900,575)) 
mixer.init()
mixer.music.load("bethoven_-_simfoniya-nomer-5.mp3")
mixer.music.play()

finish = False

menu_btn = [btn_play,btn_shop,btn_help]
shop_buttons =[btn_buy_sound1,btn_buy_sound2,btn_buy_sound3,btn_buy_skin1,btn_buy_skin2,btn_buy_skin3,btn_buy_bck1,btn_buy_bck2,btn_buy_bck3,btn_ex]

while play:
    for e in event.get():
        if e.type == QUIT:
            play = False 
    if scene == "shop":
        win.blit(background_shop,(0,0))
        win.blit(skin1,(135,260))
        win.blit(skin2,(435,260))
        win.blit(skin3,(735,260))
        font.init()
        txt = font.Font(None,60).render("SHOP",True,(113,255,195))
        win.blit(txt,(410,20))
        for button in shop_buttons:
            button.draw_btn(win)
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos
                if button.rect.collidepoint(mouse_x,mouse_y):
                    if button.button_text == "==>":
                        scene = "menu"
                    if button.button_text == "5 COINT":
                        if money >= button.btn_pay:
                            money = money - button.btn_pay
                            print(str(money))
                            button.button_text = "SELECT"
                    if button.button_text == "20 COINT":
                        if money >= button.btn_pay:
                            money = money - button.btn_pay
                            print(str(money))
                            button.button_text = "SELECT"
                    if button.button_text == "25 COINT":
                        if money >= button.btn_pay:
                            money = money - button.btn_pay
                            print(str(money))
                            button.button_text = "SELECT"
                    if button.button_text == "SELECT" and button.btn_pay == 5:
                        player.player_image = button.btn_img 
    if scene == "lvl1":
        if finish != True:

                
            win.blit(background,(0,0))
            lvl_scene = "lvl1"
            gold.show_tr()

            enemy.update()
            enemy.reset() 
            player.update()
            player.reset()
            helper1.update()
            helper1.reset()
            
            
            wall1_1 = Wall(50,100,10,20,150,250,0)#lvl1
            wall1_2 = Wall(50,100,10,20,375,250,240)#lvl1
            wall1_3 = Wall(50,100,10,550,10,250,0)#lvl1
            wall1_4 = Wall(50,100,10,650,20,250,560)#lvl1
            wall1_5 = Wall(50,100,15,10,560,890,0)#lvl1
            wall1_6 = Wall(50,100,10,20,100,355,180)#lvl1
            wall1_7 = Wall(50,100,10,100,20,375,260)#lvl1
            wall1_8 = Wall(50,100,10,100,20,250,240)#lvl1
            wall1_9 = Wall(50,100,10,325,20,355,160)#lvl1
            wall1_10 = Wall(50,100,10,200,20,250,400)#lvl1
            wall1_11 = Wall(50,100,10,20,50,430,350)#lvl1
            wall1_12 = Wall(50,100,10,130,20,430,350)#lvl1
            wall1_13 = Wall(50,100,10,130,20,430,350)#lvl1
            wall1_14 = Wall(50,100,10,120,20,550,300)#lvl1
            wall1_15 = Wall(50,100,10,20,100,550,300)#lvl1
            wall1_16 = Wall(50,100,10,230,20,550,470)#lvl1
            wall1_17 = Wall(50,100,10,20,490,780,0)#lvl1
            wall1_18 = Wall(50,100,10,300,10,380,80)#lvl1

            lvl1_list_wall = [wall1_1,
                              wall1_2,  
                              wall1_3, 
                              wall1_4,  
                              wall1_5, 
                              wall1_6,  
                              wall1_7,  
                              wall1_8,  
                              wall1_9,  
                              wall1_10,  
                              wall1_11,  
                              wall1_12,  
                              wall1_13,  
                              wall1_14,  
                              wall1_15,  
                              wall1_16,  
                              wall1_17,  
                              wall1_18]
            


            




            for lvllst1 in lvl1_list_wall:
                lvllst1.draw_wall()
                if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,lvllst1):
                    font.init()
                    lose_txt = font.Font(None,50).render("YOU LOSE",True,(0,0,0))
                    win.blit(lose_txt,(360,200)) 
                    finish = True 
            if sprite.collide_rect(player,gold):
                lvl_scene = "lvl2" 
                scene = "lvl2" 
                player.rect.x = 100
                player.rect.y = 100
    if scene == "lvl2":
        if finish != True:
            win.blit(background,(0,0))
            wall2_1=  Wall(50,100,10,20,150,250,0)#чотирикутник
            wall2_2=  Wall(50,100,10,20,375,250,240)#чотирикутник
            wall2_3=  Wall(50,100,10,550,10,250,0)#чотирикутник
            wall2_4 = Wall(50,100,10,650,20,250,560)#чотирикутник
            wall2_5 = Wall(50,100,15,10,560,890,0)#чотирикутник
            #wall2_6 = Wall(50,100,10,)#lvl1
            

            listlvl2 = [wall2_1,
                        wall2_2,
                        wall2_3,
                        wall2_4,
                        wall2_5,
                        
                        ]

           
            lvl_scene = "lvl2"
            mony.show_tr()
            
            enemy.update()
            enemy.reset() 
            player.update()
            player.reset()
            helper1.update()
            helper1.reset()
            for lvllst2 in listlvl2:
                lvllst2.draw_wall()
                if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,lvllst2):
                    font.init()
                    lose_txt = font.Font(None,50).render("YOU LOSE",True,(0,0,0))
                    win.blit(lose_txt,(360,200)) 
                    finish = True 
            if sprite.collide_rect(player,gold):
                lvl_scene = "lvl3" 
                scene = "lvl3"   
        if scene == "lvl3":
            if finish != True:
                player.player_x = 100
                player.player_y = 100
                win.blit(background,(0,0))

                player.update()
                player.reset()
                helper1.update()
                helper1.reset()
                enemy.update()
                enemy.reset() 
            for lvllst3 in lvl1_list_wall:
                if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,lvllst3):
                    font.init()
                    lose_txt = font.Font(None,50).render("YOU LOSE",True,(0,0,0))
                    win.blit(lose_txt,(360,200)) 
                finish = True 
                if sprite.collide_rect(player,gold):
                    lvl_scene = "lvl3" 
                    scene = "lvl3"     
    if scene == 'help':
        win.blit(background_help,(0,0))
        btn_ex.draw_btn(win)
        for e in event.get(): 
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos
                if btn_ex.rect.collidepoint(mouse_x,mouse_y):
                    scene = "menu"
    

    if scene == "menu":
        win.blit(background_menu2,(0,0))
        win.blit(background_menu,(0,0))   
        btn_play.draw_btn(win)
        btn_shop.draw_btn(win)   
        btn_help.draw_btn(win) 
        font.init()
        txt = font.Font(None,60).render("MENU",True,(250,250,250))
        win.blit(txt,(410,20))                     
        for btn in menu_btn:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos
                if btn.rect.collidepoint(mouse_x,mouse_y):
                    if btn.button_text == "PLAY":
                        scene = scene_lvl
                    if btn.button_text == "SHOP":
                        scene = "shop"
                    if btn.button_text == "HELP":
                        scene = "help"
        
    display.update()
    clock.tick(FPS)
        #if button.rect.collidepoint(mouse_x, mouse_y):

        
        
