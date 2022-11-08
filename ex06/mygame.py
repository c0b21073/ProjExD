import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

fps =60

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("scrool_bird")

font = pygame.font.SysFont("None", 60)
white = (0, 0, 0)

bg_scroll = 0

# スクロールの速度
scroll_speed = 4

game_over = False

# 教科書の出現間隔
obj_frequency = 1500

last_obj = pygame.time.get_ticks() - obj_frequency

score = 0

# 背景、リスタートボタンの画像をロード
bg = pygame.image.load("fig/pg_bg.jpg")
buttom_img = pygame.image.load("fig/restart.png")

# 文字を描画する関数
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# ゲームオーバー後に各自変数をリセット
def reset_game():
    obj_group.empty()
    koukaton.rect.x = 100
    koukaton.rect.y = int(screen_height/2)
    score = 0
    return score

#Birdクラス作成
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fig/2.png")
        self.rect = self.image.get_rect()
        self.jumpep = 0
        self.rect.center = (x,y)
        self.entered = False
        self.jumped = False

    def update(self):
        key_states = pygame.key.get_pressed()
        if key_states[pygame.K_SPACE]:
            self.jump()
            
        if self.jumped:
            self.jumpep += 1
            self.rect.centery += self.jumpep
            if self.rect.centery > screen_height/2:
                self.rect.centery = screen_height/2
                self.jumped = False
    
    def jump(self):
        if not self.jumped:
            self.jumped = True
            self.jumpep = -30

# Objectクラス作成
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        random_textbook = random.randint(1,5)
        self.image = pygame.image.load(f"fig/textbook{str(random_textbook)}.png")
        self.image = pygame.transform.rotozoom(self.image,0,0.7)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
  

 # Buttonクラス作成   
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


bird_group = pygame.sprite.Group()
obj_group = pygame.sprite.Group()

koukaton = Bird(100,int(screen_height/2))

bird_group.add(koukaton)

bg_x = 0

button = Button(screen_width//2 - 50, screen_height//2 - 100, buttom_img)

running = True

while running:

    clock.tick(fps)

    # 背景画像を右側からスクロール
    bg_x = (bg_x-scroll_speed)%1600
    screen.blit(bg,(bg_x-1600,0))
    screen.blit(bg,(bg_x,0))

    bird_group.draw(screen)
    bird_group.update()

    obj_group.draw(screen)

    # スコアを表示
    draw_text("Score:" + str(int(score)), font, white, int(screen_width/2), 20)

    # bird_groupとobj_groupの衝突判定
    if pygame.sprite.groupcollide(bird_group, obj_group, False, False):
        game_over = True
    
    # ゲームオーバーでないなら
    if game_over == False:
        score += 0.01

        time_now = pygame.time.get_ticks()

        if time_now - last_obj > obj_frequency:
            obj = Object(screen_width, int(screen_height/2))
            obj_group.add(obj)
            last_obj = time_now
        obj_group.update()

    # ゲームオーバーならば
    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()