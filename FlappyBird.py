#小鸟游戏
import pygame
import random

#初始化并创建舞台
pygame.init()
screen=pygame.display.set_mode([288,512])

#加入背景并确定名字
background=pygame.image.load('assets/background.png')
pygame.display.set_caption('Flappy Bird')

#确定bgm
bgm=pygame.mixer.Sound('sound\\bgm.wav')
channel_1=pygame.mixer.Channel(1)
channel_1.play(bgm)

#主循环运行总参数与游戏帧数
keep_going=True
clock=pygame.time.Clock()

#小鸟类
class bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.birdSprites=[pygame.image.load('assets/0.png'),pygame.image.load('assets/1.png'),pygame.image.load('assets/2.png')]
        self.a=0
        self.birdx=50
        self.birdy=100
        self.jumpspeed=7
        self.gravity=0.4
        
        self.rect=self.birdSprites[self.a].get_rect()
        self.rect.center=(self.birdx,self.birdy)
        
    def birdupdate(self):
        self.jumpspeed-=self.gravity
        self.birdy-=self.jumpspeed
        
        self.rect.center=(self.birdx,self.birdy)
        
        if self.jumpspeed>0:
            self.a=2
        if self.jumpspeed<0:
            self.a=1
    
    def birdCrush(self):
        global keep_going
        resultu=self.rect.colliderect(wall_a.walluprect)
        resultd=self.rect.colliderect(wall_a.walldownrect)        
        
        if resultu or resultd or bird_a1.rect.top>512:
            hit=pygame.mixer.Sound('sound\\hit.wav')
            channel_1=pygame.mixer.Channel(3)
            channel_1.play(hit)
            keep_going=False
        
#柱子类
class wall():
    def __init__(self):
        self.wallUp=pygame.image.load('D:\\zuopin\\python_pygame_1\\assets\\top.png')
        self.wallDown=pygame.image.load('D:\\zuopin\\python_pygame_1\\assets\\bottom.png')
        
        self.walluprect=self.wallUp.get_rect()
        self.walldownrect=self.wallDown.get_rect()
        
        self.gap=50
        self.wallx=288
        self.offset=random.randint(-50,50)
        
        self.wallupy=-140+self.gap-self.offset
        self.walldowny=300+self.gap-self.offset
        
        self.walluprect.center=(self.wallx,self.wallupy)
        self.walldownrect.center=(self.wallx,self.walldowny)
    
    def wallUpdate(self):
        self.wallx=self.wallx-1
        self.walluprect.center=(self.wallx,self.wallupy)
        self.walldownrect.center=(self.wallx,self.walldowny)
        
        if self.wallx==-50:
            self.wallx=330
            self.offset=random.randint(-100,160)
            self.wallupy=-140+wall_a.gap-wall_a.offset
            self.walldowny=300+wall_a.gap-wall_a.offset

#实例对象 
bird_a1=bird()
wall_a=wall()        

#主循环
while keep_going:
    
    #判断事件
    for event in pygame.event.get():
        
        #是否关闭判断
        if event.type==pygame.QUIT:
            keep_going=False
        
        #鼠标点击判断
        if (event.type==pygame.MOUSEBUTTONDOWN):
            bird_a1.jumpspeed=7
        
        #空格点击判断与音效
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE)):
            bird_a1.jumpspeed = 7
            
            channel_2=pygame.mixer.Channel(2)
            fly=pygame.mixer.Sound('sound\\fly.wav')
            channel_2.play(fly)

    #加入角色
    screen.blit(background,(0,0))
    screen.blit(bird_a1.birdSprites[bird_a1.a],bird_a1.rect)
    screen.blit(wall_a.wallUp,wall_a.walluprect)  
    screen.blit(wall_a.wallDown,wall_a.walldownrect)
    
    #启用类
    wall_a.wallUpdate()
    bird_a1.birdupdate()
    bird_a1.birdCrush()
    pygame.display.update()
    
    #设置帧数
    clock.tick(60)

#关闭
pygame.quit()  