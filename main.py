import os
import sys
import pygame as pg
import math
import random
import time

WIDTH,HEIGHT = 1280,720
FRAMERATE = 60
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Player(pg.sprite.Sprite):
    '''プレイヤー'''
    def __init__(self) -> None:
        pass
    def dummy(self):
        pass

class Reinforcement(pg.sprite.Sprite):
    '''
    total_output -> totalを入れる
    timer_clock -> フレーム
    total_input -> 消費する量
    '''
    def __init__(self,x,y,total_output,timer_clock,total_input) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.total_output = total_output
        self.timer_clock = timer_clock
        self.total_input = total_input
        self.object_number = 0
        self.font = pg.font.Font(None,10)
        # input
        self.text_input = self.font.render(str(""), True, (255, 255, 255))
        self.rect_text_input = self.text_input.get_rect()
        self.rect_text_input.center = x-150,y+20
        # output
        self.text_output = self.font.render(str(""), True, (255, 255, 255))
        self.rect_text_output = self.text_output.get_rect()
        self.rect_text_output.center = x-150,y-20
        # count
        self.text_counter = self.font.render(str(""), True, (255, 255, 255))
        self.rect_text_counter = self.text_counter.get_rect()
        self.rect_text_counter.center = x+50,y-20
        self.image = pg.Surface((WIDTH/2-200,100))
        pg.draw.rect(self.image,(0,0,0),(WIDTH/2-200,0,WIDTH/2+200,100))
        self.rect = self.image.get_rect()
        self.rect.center = x,y

    def check(self, pos):
        return self.rect.collidepoint(pos)

    def counter(self,total):
        if total >= self.total_output:
            self.object_number += 1
            return self.total_output
        else:
            return 0

    def update(self,screen:pg.Surface):
        self.font = pg.font.Font(None,50)
        self.text_output = self.font.render(str(self.total_output),True,(255, 255, 255))
        self.text_input = self.font.render(str(self.timer_clock),True,(255, 255, 255))
        self.font = pg.font.Font(None,100)
        self.text_counter = self.font.render(str(self.object_number),True,(255, 255, 255))
        screen.blit(self.image,self.rect)
        screen.blit(self.text_counter,self.rect_text_counter)
        screen.blit(self.text_input,self.rect_text_input)
        screen.blit(self.text_output,self.rect_text_output)

class Total():  # ここ
    '''現在の総数'''
    def __init__(self) -> None:
        """変数の初期化"""
        self.fonto = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 30)
        self.color = (255, 255, 255)
        self.sum = 0
        self.total = 0
        self.img = self.fonto.render(f"{self.total}:崛起ー", 0, self.color)
        self.centery = (200, 120)

    def update(self, total, screen):
        """数値を更新"""
        self.total = int(total)  # int表示算
        total = 0
        if self.total < 10000:
            total = self.total
            self.img = self.fonto.render(f"{total}:崛起ー", 0, self.color)
        elif self.total >= 10000:  # 本家を見習って表示変更（必要なら億も実装）
            total = round(self.total/10000, 4)
            self.img = self.fonto.render(f"{total}万:崛起ー", 0, self.color)
        screen.blit(self.img, self.centery)

class FallingImage(pg.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.original_image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.original_image,(self.original_image.get_width()//10,self.original_image.get_height()//10))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, (WIDTH//2)-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 5
        if self.rect.y > HEIGHT:
            self.kill()


def main():
    pg.display.set_caption("ななしのげーむ（仮）")
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    bg_img = pg.image.load(f"image/dummy_0.png")
    total = Total()
    total.value = 10000
    total_sum = 0
    player = Player()
    reinforcement_list = [[5,FRAMERATE,1],[20,FRAMERATE/2,1],[100,FRAMERATE/6,1],[1000,1,1]]
    r_blocks = pg.sprite.Group()
    for y,(q,w,e) in zip(range(len(reinforcement_list)),reinforcement_list):
        r_blocks.add(Reinforcement(WIDTH/4*3,100+y*125,q,w,e))
    timer = 0
    clock = pg.time.Clock()
    font = pg.font.Font(None,80)
    falling_images = pg.sprite.Group()

    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    total.value -= 1
                if event.key == pg.K_x:
                    total.value += 1
                print(total.value)
            if event.type == pg.MOUSEBUTTONDOWN:
                x,y = event.pos
                for r_block in r_blocks:
                    if r_block.check(event.pos):
                        total.value -= r_block.counter(total.value)
                        print(total.value,r_block.y)
                print(f"mouse moved -> ({x},{y})")
        screen.blit(bg_img,[0,0])
        txt = font.render("Timer:"+str(int(timer/FRAMERATE)), True, (255, 255, 255))
        screen.blit(txt, [300, 200])

        
        # player.update(screen)
        total_sum = 0
        for r_block in r_blocks:
            if timer % r_block.timer_clock == 0:
                total_sum += r_block.total_input * r_block.object_number
        total.value += total_sum


        spawn_probability = min(0.1+(total_sum/1000) **2,10)
        if random.random() < spawn_probability:
            new_image = FallingImage("image/dummy_2.png")
            falling_images.add(new_image)
        
        falling_images.update()
        falling_images.draw(screen)
        # player.update(screen)
        r_blocks.draw(screen)
        r_blocks.update(screen)
        total.update(total.value,screen)  # クッキーの合計量の更新
        timer += 1
        clock.tick(FRAMERATE)
        pg.display.update()
        screen.blit(bg_img,[0,0])

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()