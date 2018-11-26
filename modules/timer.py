import pygame
import math
from configs import constants as c
from modules import helpers

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
            text = self.getText()
            font = self.getFont()
            surface = font.render(text, True, c.TIMER_COLOR)
            position = surface.get_rect()
            position.center = ((c.SCREEN_WIDTH/2), c.TIMER_SIZE)
            pygame.display.get_surface().blit(surface, position)

    # 获取显示文案
    def getText(self):
        if self.isCountDown == True:
            return str(math.ceil((self.until - self.now) / 1000))
        else:
            return str(math.ceil(self.now / 1000))

    # 加载字体
    def getFont(self):
        if c.FONT_NAME in pygame.font.get_fonts():
            return pygame.font.SysFont(c.FONT_NAME, c.TIMER_SIZE, bold)
        else:
            filepath = helpers.abspath('resources', 'fonts', c.FONT_FILE)
            font = pygame.font.Font(filepath, c.TIMER_SIZE)
            font.set_bold(True)
            return font
