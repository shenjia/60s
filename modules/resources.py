import os
import pygame
from configs import constants as c
from .helpers import *

IMAGES = {}
AUDIOS = {}

# 加载图片
def loadImage(dir, file, name):
    image = pygame.image.load(os.path.join(dir, file))
    IMAGES[name] = image.convert_alpha() if image.get_alpha() else image.convert()

# 加载音效
def loadAudio(dir, file, name):
    AUDIOS[name] = pygame.mixer.Sound(os.path.join(dir, file))

# 加载音乐
def loadMusic(dir, file, name):
    pygame.mixer.music.load(os.path.join(dir, file))

# 加载所有资源
def loadAll():
    walk(abspath('resources', 'images'), loadImage, c.IMAGE_EXTS)
    walk(abspath('resources', 'audios'), loadAudio, c.AUDIO_EXTS)
    walk(abspath('resources', 'musics'), loadMusic, c.MUSIC_EXTS)
