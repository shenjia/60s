import pygame
import random
import math
import time
from configs import constants as c
from modules import helpers
from modules import resources
from modules.ship import Ship
from modules.bullet import Bullet
from modules.timer import Timer
from sys import exit

class Game():

    isMusic = True

    def __init__(self):
        pass

    # 启动游戏
    def start(self):

        # 主循环
        while True:

            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    self.onKeyDown(event.key)
                if event.type == pygame.KEYUP:
                    self.onKeyUp(event.key)
                if event.type == c.EVENT_OVER:
                    self.over()
                if event.type == c.EVENT_MAKE_BULLET:
                    self.makeBullet()

            # 更新并绘制画面
            self.update()
            self.draw()
            self.clock.tick(c.FPS)

    # 更新游戏信息
    def update(self):

        # 更新飞船位置
        self.ship.update()

        # 更新子弹位置
        for bullet in self.bullets:
            bullet.update()

        # 更新计时器
        self.timer.update()

        # 处理移动和碰撞
        self.handleMove()
        self.handleCollision()

    # 绘制游戏画面
    def draw(self):

        # 背景
        self.screen.fill(c.BLACK)

        # 显示球和矩形
        self.ship.draw()
        for bullet in self.bullets:
            bullet.draw()

        # 显示计时器
        self.timer.draw()

        pygame.display.update()

    # 初始化游戏
    def setup(self):

        # 初始化pygame
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(c.TITLE)
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0, 32)

        # 加载资源
        resources.loadAll()
        pygame.display.set_icon(resources.IMAGES['ship'])
        self.clock = pygame.time.Clock()

        # 播放音乐
        if self.isMusic:
            pygame.mixer.music.set_volume(c.MUSIC_VOLUME)
            pygame.mixer.music.play(loops=1)

        # 初始化飞船
        self.ship = Ship()
        self.ship.move(c.SCREEN_CENTER)

        # 初始化子弹
        self.bullets = pygame.sprite.Group()
        pygame.time.set_timer(c.EVENT_MAKE_BULLET, c.BULLETS_DELAY)

        # 进入准备状态
        resources.AUDIOS['ready_go'].play()
        self.isReady = False
        self.timer = Timer({
            'since' : pygame.time.get_ticks(),
            'seconds' : c.READY_SECONDS,
            'isCountDown' : True,
            'isHide' : True,
            'callback' : self.ready
        })

    # 创建新的子弹
    def makeBullet(self):
        if self.isReady and len(self.bullets) < c.BULLETS_LIMIT:
            bullet = Bullet({
                'speed': random.uniform(c.BULLET_MIN_SPEED, c.BULLET_MAX_SPEED)
            })
            bullet.goto(self.ship.position)
            bullet.add(self.bullets)

    # 处理碰撞
    def handleCollision(self):

        # 先根据外部矩阵做快速检测，找到可能发生碰撞的子弹
        dangerBullets = pygame.sprite.spritecollide(self.ship, self.bullets, dokill=False)

        # 对矩阵有碰撞的子弹再进行像素检测
        for bullet in dangerBullets:
            hit = pygame.sprite.collide_mask(self.ship, bullet)
            if hit == None:
                # 这颗子弹没碰到，再看下一个
                pass
            else:
                # 不幸命中，Game Over
                event = pygame.event.Event(c.EVENT_OVER)
                pygame.event.post(event)

    # 处理按下键
    def onKeyDown(self, key):
        if (key == pygame.K_ESCAPE):
            self.exit()
        if (key == pygame.K_SPACE):
            if self.isMusic:
                pygame.mixer.music.stop()
                self.isMusic = False
            else:
                pygame.mixer.music.play(loops=1)
                self.isMusic = True

    # 处理松开键
    def onKeyUp(self, key):
        pass

    # 处理移动
    def handleMove(self):
        speedX = speedY = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            speedX = speedX - c.SHIP_SPEED
        if pressed[pygame.K_RIGHT]:
            speedX = speedX + c.SHIP_SPEED
        if pressed[pygame.K_UP]:
            speedY = speedY - c.SHIP_SPEED
        if pressed[pygame.K_DOWN]:
            speedY = speedY + c.SHIP_SPEED
        self.ship.speedX = speedX
        self.ship.speedY = speedY

    # 准备好了
    def ready(self):

        self.isReady = True

        # 开始胜利倒计时
        self.timer = Timer({
            'since' : pygame.time.get_ticks(),
            'seconds' : c.TIMER_SECONDS,
            'isCountDown' : True,
            'callback' : self.win
        })

    # 游戏胜利
    def win(self):
        pygame.mixer.music.stop()
        resources.AUDIOS['you_win'].play()
        self.showMessage('You Win!', c.GREEN)
        self.setup()

    # 游戏失败
    def over(self):
        pygame.mixer.music.stop()
        resources.AUDIOS['game_over'].play()
        self.showMessage('Game Over', c.RED)
        self.setup()

    # 退出游戏
    def exit(self):
        #pygame.quit()
        exit()

    # 显示文本提示
    def showMessage(self, message, color = c.MESSAGE_COLOR, seconds = c.MESSAGE_SECONDS):

        font = pygame.font.Font(c.MESSAGE_FONT,c.MESSAGE_SIZE)
        text = font.render(message, True, color)
        position = text.get_rect()
        position.center = c.SCREEN_CENTER

        self.timer = Timer({
            'since' : pygame.time.get_ticks(),
            'seconds' : seconds,
        })

        while self.timer.isRunning:

            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    self.onKeyDown(event.key)

            # 更新并绘制画面
            self.timer.update()
            self.screen.fill(c.BLACK)
            self.screen.blit(text, position)
            self.clock.tick(c.FPS)
            pygame.display.update()

game = Game()
