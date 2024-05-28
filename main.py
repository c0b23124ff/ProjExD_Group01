# 初期化

import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Player():
    '''プレイヤー'''
    def __init__(self) -> None:
        pass
    def dummy(self):
        pass

class Reinforcement():
    '''強化欄'''
    def __init__(self) -> None:
        pass
    def dummy(self):
        pass

class Total():
    '''現在の総数'''
    def __init__(self) -> None:
        pass
    def dummy(self):
        pass


def main():
    pg.display.set_caption("ななしのげーむ（仮）")
    screen = pg.display.set_mode((1280,720))
    player = Player()
    r_block = Reinforcement()
    total = Total()
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50), rect = (0,0,640,720))
        screen.blit(txt, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(1)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()