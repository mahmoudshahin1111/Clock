import pygame
import math
import time

pygame.init()

def rotate_point(r_angle,point,origi_point):
    #rotate point
    rad = 0.0174533
    angle = 0
    angle += r_angle
    angle *= rad
    op = point[0]-origi_point[0],point[1]-origi_point[1]
    initx=op[0]*math.cos(angle) - op[1]*math.sin(angle)
    inity=op[0]*math.sin(angle) + op[1]*math.cos(angle)
    initx += origi_point[0]
    inity += origi_point[1]
    return [initx,inity]

width,height = 400,400

screen = pygame.display.set_mode([width,height])

centerP=(200,200)

#watch hands end points that we will use in rotation
hh_ep=(200,120)
mh_ep=(200,80)
sh_ep=(200,40)

#Colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)



#watch_hands
hour_hand=[centerP,hh_ep]
min_hand=[centerP,mh_ep]
sec_hand=[centerP,sh_ep]

#constatns angle hands
hour_angle = 30
min_angle = 6
sec_angle = 6

#text
font=pygame.font.SysFont('ARIAL',20)
clockClip = pygame.image.load(r'clock_clip.jpg')


run=True
while run:

    text='12'
    
    #get current time
    local_time = time.localtime(time.time())
    hour_time = local_time[3] - 12
    min_time = local_time[4]
    sec_time = local_time[5]

    #update end point (angle to hour , min , seconds)
    hour_point = rotate_point((min_time*.5)+(hour_time*hour_angle),hh_ep,centerP)
    min_point = rotate_point(min_time*min_angle,mh_ep,centerP)
    sec_point = rotate_point(sec_time*sec_angle,sh_ep,centerP)

    #draw screen
    screen.fill(0)

    #draw clock
    pygame.draw.circle(screen,(50,50,50),centerP,200)
    twelve = font.render('12',True,(100,100,100))
    one = font.render('1',True,(100,100,100))
    two = font.render('2',True,(100,100,100))
    three = font.render('3',True,(100,100,100))
    four = font.render('4',True,(100,100,100))
    five = font.render('5',True,(100,100,100))
    six = font.render('6',True,(100,100,100))
    seven = font.render('7',True,(100,100,100))
    eight = font.render('8',True,(100,100,100))
    nine = font.render('9',True,(100,100,100))
    ten = font.render('10',True,(100,100,100))
    eleven = font.render('11',True,(100,100,100))

    screen.blit(twelve,(200,10))
    screen.blit(one,(300,40))
    screen.blit(two,(360,100))
    screen.blit(three,(380,185))
    screen.blit(four,(360,280))
    screen.blit(five,(300,340))
    screen.blit(six,(200,370))
    screen.blit(seven,(100,340))
    screen.blit(eight,(30,280))
    screen.blit(nine,(13,185))
    screen.blit(ten,(40,100))
    screen.blit(eleven,(100,40))
    
    #draw watch hands
    pygame.draw.line(screen,red,hour_hand[0],(hour_point[0],hour_point[1]))
    pygame.draw.line(screen,green,min_hand[0],(min_point[0],min_point[1]))
    pygame.draw.line(screen,blue,sec_hand[0],(sec_point[0],sec_point[1]))

    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


pygame.quit()
        
