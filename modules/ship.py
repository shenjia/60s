import pygame
import math
from . import resources as res
from configs import constants as c
from modules.sprite import Sprite

class Ship(Sprite):

    def __init__(self, config = {}):

        config.setdefault('speedX', 0)
        config.setdefault('speedY', 0)
        Sprite.__init__(self, config)

        # 设定图像和遮罩
        self.image = res.IMAGES['ship']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # 计算活动范围
        self.minX = self.width / 2
        self.maxX = c.SCREEN_WIDTH - self.width / 2
        self.minY = self.height / 2
        self.maxY = c.SCREEN_HEIGHT - self.height / 2

    def update(self):

        # 按速度更新坐标
        self.X = self.X + self.speedX / c.FPS
        self.Y = self.Y + self.speedY / c.FPS

        # 限制移动范围
        if self.X < self.minX: self.X = self.minX
        if self.Y < self.minY: self.Y = self.minY
        if self.X > self.maxX: self.X = self.maxX
        if self.Y > self.maxY: self.Y = self.maxY

        Sprite.update(self)
