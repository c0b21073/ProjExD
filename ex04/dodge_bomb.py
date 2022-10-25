import pygame as pg
import sys
from random import randint


def game():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    bomb_sfc_size = 20
    bomb_rct_size = 10


    bomb1_sfc = pg.Surface((bomb_sfc_size,bomb_sfc_size))
    bomb1_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb1_sfc, (255,0,0), (bomb_sfc_size/2,bomb_sfc_size/2), bomb_rct_size)
    bomb1_rct = bomb1_sfc.get_rect()
    bomb1_rct.centerx = randint(0,scrn_rct.width)
    bomb1_rct.centery = randint(0,scrn_rct.height)

    bomb2_sfc = pg.Surface((bomb_sfc_size,bomb_sfc_size))
    bomb2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb2_sfc, (191,0,0), (bomb_sfc_size/2,bomb_sfc_size/2), bomb_rct_size)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0,scrn_rct.width)
    bomb2_rct.centery = randint(0,scrn_rct.height)

    bomb3_sfc = pg.Surface((bomb_sfc_size,bomb_sfc_size))
    bomb3_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb3_sfc, (127,0,0), (bomb_sfc_size/2,bomb_sfc_size/2), bomb_rct_size)
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = randint(0,scrn_rct.width)
    bomb3_rct.centery = randint(0,scrn_rct.height)

    bomb4_sfc = pg.Surface((bomb_sfc_size,bomb_sfc_size))
    bomb4_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb4_sfc, (63,0,0), (bomb_sfc_size/2,bomb_sfc_size/2), bomb_rct_size)
    bomb4_rct = bomb4_sfc.get_rect()
    bomb4_rct.centerx = randint(0,scrn_rct.width)
    bomb4_rct.centery = randint(0,scrn_rct.height)

    bomb5_sfc = pg.Surface((bomb_sfc_size,bomb_sfc_size))
    bomb5_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb5_sfc, (0,0,255), (bomb_sfc_size/2,bomb_sfc_size/2), bomb_rct_size)
    bomb5_rct = bomb5_sfc.get_rect()
    bomb5_rct.centerx = randint(0,scrn_rct.width)
    bomb5_rct.centery = randint(0,scrn_rct.height)


    vx1,vx2,vx3,vx4,vx5 =+1,+1,+1,+1,+1
    vy1,vy2,vy3,vy4,vy5 =+1,+1,+1,+1,+1
    
    tmr = "don't mind!!!"

    clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)

        bomb_sfc_size += 1
        bomb_rct_size += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
            if tori_rct.centery == 0:
                tori_rct.centery += 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
            if tori_rct.centery == scrn_rct.height:
                tori_rct.centery -= 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1
            if tori_rct.centerx == 0:
                tori_rct.centerx += 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1
            if tori_rct.centerx == scrn_rct.width:
                tori_rct.centerx -= 1


        bomb1_rct.move_ip(vx1, vy1)
        if bomb1_rct.centerx == 0:
            vx1 = +1
        if bomb1_rct.centerx == scrn_rct.width:
            vx1 = -1
        if bomb1_rct.centery == 0:
            vy1 = +1
        if bomb1_rct.centery == scrn_rct.height:
            vy1 = -1

        bomb2_rct.move_ip(vx2, vy2)
        if bomb2_rct.centerx == 0:
            vx2 = +1
        if bomb2_rct.centerx == scrn_rct.width:
            vx2 = -1
        if bomb2_rct.centery == 0:
            vy2 = +1
        if bomb2_rct.centery == scrn_rct.height:
            vy2 = -1
        
        bomb3_rct.move_ip(vx3, vy3)
        if bomb3_rct.centerx == 0:
            vx3 = +1
        if bomb3_rct.centerx == scrn_rct.width:
            vx3 = -1
        if bomb3_rct.centery == 0:
            vy3 = +1
        if bomb3_rct.centery == scrn_rct.height:
            vy3 = -1
        
        bomb4_rct.move_ip(vx4, vy4)
        if bomb4_rct.centerx == 0:
            vx4 = +1
        if bomb4_rct.centerx == scrn_rct.width:
            vx4 = -1
        if bomb4_rct.centery == 0:
            vy4 = +1
        if bomb4_rct.centery == scrn_rct.height:
            vy4 = -1

        bomb5_rct.move_ip(vx5, vy5)
        if bomb5_rct.centerx == 0:
            vx5 = +1
        if bomb5_rct.centerx == scrn_rct.width:
            vx5 = -1
        if bomb5_rct.centery == 0:
            vy5 = +1
        if bomb5_rct.centery == scrn_rct.height:
            vy5 = -1

        
        scrn_sfc.blit(tori_sfc, tori_rct)
        scrn_sfc.blit(bomb1_sfc, bomb1_rct)


        if pg.time.get_ticks() >= 5000:
            scrn_sfc.blit(bomb2_sfc, bomb2_rct)
        if pg.time.get_ticks() >= 10000:
            scrn_sfc.blit(bomb3_sfc, bomb3_rct)
        if pg.time.get_ticks() >= 15000:
            scrn_sfc.blit(bomb4_sfc, bomb4_rct)
        if pg.time.get_ticks() >= 20000:
            scrn_sfc.blit(bomb5_sfc, bomb5_rct)

        if tori_rct.colliderect(bomb1_rct) or tori_rct.colliderect(bomb2_rct) or tori_rct.colliderect(bomb3_rct) or tori_rct.colliderect(bomb4_rct) or tori_rct.colliderect(bomb5_rct):
            fonto = pg.font.Font(None, 300)
            txt = fonto.render(tmr, True, (0,0,0))
            scrn_sfc.blit(txt, (200, 300))
            tori_sfc = pg.image.load("fig/7.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() 
    game() 
    pg.quit() 
    sys.exit()

