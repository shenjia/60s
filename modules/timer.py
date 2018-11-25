import pygame
import math
from configs import constants as c

class Timer:

    template = {
        'since' : 0,
        'until' : 0,
        'seconds' : c.TIMER_SECONDS,
        'isHide' : False,
        'isRunning' : True,
        'isCountDown' : True,
        'callback' : None
    }

    def __init__(self, config):
        config = dict(self.template, **config)
        for key in config:
            setattr(self, key, config[key])
        self.now = self.since
        self.until = self.since + self.seconds * 1000

    # 更新时间
    def update(self):
        if self.isRunning:
            self.now = pygame.time.get_ticks()
            if self.now > self.until:
                self.now = self.until
                self.isRunning = False
                if self.callback != None:
                    self.callback()


    # 显示倒计时
    def draw(self):
        if not self.isHide:
            timer = self.getText()
            font = pygame.font.Font(c.TIMER_FONT,c.TIMER_SIZE)
            text = font.render(timer, True, c.TIMER_COLOR)
            position = text.get_rect()
            position.center = ((c.SCREEN_WIDTH/2), c.TIMER_SIZE)
            pygame.display.get_surface().blit(text, position)

    # 获取显示文案
    def getText(self):
        if self.isCountDown == True:
            return str(math.ceil((self.until - self.now) / 1000))
        else:
            return str(math.ceil(self.now / 1000))
