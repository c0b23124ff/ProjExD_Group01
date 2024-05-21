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
        self.value = 0
    def dummy(self):
        pass


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