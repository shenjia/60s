import pygame
import random
from . import resources as res
from configs import constants as c
from modules.sprite import Sprite
from modules import helpers

class Bullet(Sprite):

    def __init__(self, config = {}):
        config.setdefault('speed', 0)
        config.setdefault('speedX', 0)
        config.setdefault('speedY', 0)
        Sprite.__init__(self, config)

        # 设定图像和遮罩
        self.image = res.IMAGES['bullet']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # 计算活动范围
        self.minX = - self.width / 2
        self.maxX = c.SCREEN_WIDTH + self.width / 2
        self.minY = - self.height / 2
        self.maxY = c.SCREEN_HEIGHT + self.height / 2

        # 随机生成出发点
        self.X, self.Y = self.getNewPosition()

    # 给子弹随机生成一个出发点
    def getNewPosition(self):
        dice = random.random()
        if dice > 0.5:
            # 在上下边缘出现
            x = random.uniform(self.minX, self.maxX)
            y = self.maxY if dice > 0.75 else self.minY
        else:
            # 在左右边缘出现
            x = random.uniform(self.minY, self.maxY)
            y = self.maxY if dice > 0.25 else self.minY
        return x, y

    # 指定子弹飞行的目标
    def goto(self, position):
        px, py = position
        dx = px - self.X
        dy = py - self.Y
        dz = helpers.distance(self.X, self.Y, px, py)
        time = dz / self.speed
        self.speedX = dx / time
        self.speedY = dy / time

    # 更新子弹位置
    def update(self):

        # 按速度更新坐标
        self.X = self.X + self.speedX / c.FPS
        self.Y = self.Y + self.speedY / c.FPS

        # 如果移动出屏幕，就销毁并生成新的子弹
        if self.invisible():
            self.kill()
            event = pygame.event.Event(c.EVENT_MAKE_BULLET)
            pygame.event.post(event)

        Sprite.update(self)

    # 判断子弹是否可见
    def invisible(self):
        return self.X < self.minX or self.X > self.maxX or self.Y < self.minY or self.Y > self.maxY
