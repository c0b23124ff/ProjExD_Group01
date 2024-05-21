# 初期化

import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Player():
    '''クリック対象の作成
    中心は320,360
    クリック判定はmain'''
    def __init__(self,defsize :float):
        self.defsize =defsize
        self.size = defsize
        #self.img=pg.Surface((2*defsize, 2*defsize))
        #pg.draw.circle(self.img, (150,130,100), (defsize, defsize), defsize)
        self.img = pg.transform.rotozoom(pg.image.load(f"image/dummy_{2}.png"), 0, self.size)
        self.img.set_colorkey((0, 0, 0))
        self.rct: pg.Rect = self.img.get_rect()
        self.rct.center = (320,360)
    
    def change_img(self,screen): #クリックされたときsizeを50
        self.size = self.defsize+0.1 #大きくする

    def update(self,screen): 
        if self.size > self.defsize:
            self.size -= 0.01
        else:
            self.size = self.defsize
        #self.img=pg.Surface((2*self.size, 2*self.size))
        #pg.draw.circle(self.img, (150,130,100), (self.size, self.size), self.size)
        self.img = pg.transform.rotozoom(pg.image.load(f"image/dummy_{2}.png"), 0, self.size)
        self.img.set_colorkey((0, 0, 0))
        self.rct: pg.Rect = self.img.get_rect()
        self.rct.center = (320,360)
        screen.blit(self.img, self.rct) 

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
    player = Player(0.5)
    r_block = Reinforcement()
    total = Total()
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.MOUSEBUTTONDOWN: #クリックしたとき
                mouseX,mouseY = pg.mouse.get_pos()
                if 220<= mouseX and mouseX <= 420: #xのあたり範囲　ターゲットの中心320,360
                    if 260<= mouseY and mouseY <= 460: #yのあたり範囲
                        #当たった時の処理
                        player.change_img(screen)

        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [100, 400])
        player.update(screen)
        pg.display.update()
        tmr += 1        
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()