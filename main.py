import os
import sys
import pygame as pg
import math
import random
import time

WIDTH, HEIGHT = 1280,720
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Player(pg.sprite.Sprite):
    '''プレイヤー'''
    def __init__(self) -> None:
        pass
    def dummy(self):
        pass

class Reinforcement(pg.sprite.Sprite):
    '''強化欄'''
    def __init__(self,) -> None:
        pass
    def dummy(self):
        pass
    def update(self):
        pass

class Total():
    '''現在の総数'''
    def __init__(self) -> None:
        """変数の初期化"""
        self.fonto = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 30)
        self.color = (255, 255, 255)
        self.sum = 0
        self.total = int(self.sum)
        self.add = 0
        self.img = self.fonto.render(f"{self.total}:崛起ー", 0, self.color)
        self.centery = (200, 120)

    def update(self, add, screen):
        """数値を更新"""
        self.sum += add  # 今回増える分量の加算（減産はほかのものが出そろってから）
        self.total = int(self.sum)  # int表示
        total = 0
        if self.total < 10000:
            total = self.total
            self.img = self.fonto.render(f"{total}:崛起ー", 0, self.color)
        elif self.total >= 10000:  # 本家を見習って表示変更（必要なら億も実装）
            total = round(self.total/10000, 4)
            self.img = self.fonto.render(f"{total}万:崛起ー", 0, self.color)
        screen.blit(self.img, self.centery)
        


def main():
    pg.display.set_caption("ななしのげーむ（仮）")
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    bg_img = pg.image.load(f"image/dummy_0.png")
    total = Total()
    total.value = 10000
    player = Player()
    r_block = Reinforcement()
    timer = 0
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)
    add = 0
    tmr = 0

    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    total.value -= 1
                    print(total.value)
                if event.key == pg.K_x:
                    total.value += 1
                    print(total.value)
        screen.blit(bg_img,[0,0])
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])

        key_lst = pg.key.get_pressed()  # テスト用
        if key_lst[pg.K_SPACE]:  # テスト用
            add += 100  # テスト用

        total.update(add, screen)  # クッキーの合計量の更新
        add = 0  # 加算分を0にリセット
        tmr += 1        
        clock.tick(60)


        

        # player.update(screen)
        # r_block.update(screen)
        # total.update(screen)
        pg.display.update()
        timer += 1
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()