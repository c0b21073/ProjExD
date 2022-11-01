import pygame as pg
import sys
from random import randint


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


class Screen:
    def __init__(self,title,wh,back_img):
        pg.display.set_caption(title)
        self.scrn_sfc = pg.display.set_mode(wh)
        self.scrn_rct = self.scrn_sfc.get_rect()
        self.bgi_sfc = pg.image.load(back_img)
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.scrn_sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,bird_img,magnification,start_state):
        bird_sfc = pg.image.load(bird_img)
        self.bird_sfc = pg.transform.rotozoom(bird_sfc,0,magnification)
        self.bird_rct = bird_sfc.get_rect()
        self.bird_rct.center = (start_state)

    def blit(self,scr:Screen):
        scr.scrn_sfc.blit(self.bird_sfc, self.bird_rct)

    def update(self,scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.bird_rct.centerx += delta[0]
                self.bird_rct.centery += delta[1]
                if check_bound(self.bird_rct, scr.scrn_rct) != (+1, +1):
                    self.bird_rct.centerx -= delta[0]
                    self.bird_rct.centery -= delta[1]
        self.blit(scr)
        

class Bomb:
    def __init__(self,color,radius,vxy,scr:Screen):
        self.bomb_sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.bomb_sfc, (color), (radius, radius), radius) # 円を描く
        self.bomb_rct = self.bomb_sfc.get_rect()
        self.bomb_rct.centerx = randint(0, scr.scrn_rct.width)
        self.bomb_rct.centery = randint(0, scr.scrn_rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.scrn_sfc.blit(self.bomb_sfc, self.bomb_rct)

    def update(self,scr:Screen):
        self.bomb_rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.bomb_rct, scr.scrn_rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def main():
    # 練習1(スクリーンインスタンス生成)
    scr = Screen("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")

    # 練習2(こうかとんインスタンス生成)
    bird = Bird("fig/6.png",2.0,(900,400))

    # 練習3(爆弾インスタンス生成)
    bomb = Bomb((255,0,0),10,(+1,+1),scr)

    clock = pg.time.Clock()

    while True:
        scr.blit() 
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        bird.update(scr) # 練習2

        bomb.update(scr) # 練習3

        if bird.bird_rct.colliderect(bomb.bomb_rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() 
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()