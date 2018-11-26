import pygame

# 颜色配置
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 屏幕尺寸
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# 信息提示
MESSAGE_FONT = "resources/fonts/Consolas Bold.ttf"
MESSAGE_COLOR = RED
MESSAGE_SIZE = 50
MESSAGE_SECONDS = 5

# 计时器
TIMER_FONT = "resources/fonts/Consolas Bold.ttf"
TIMER_COLOR = WHITE
TIMER_SIZE = 30
TIMER_SECONDS = 60
READY_SECONDS = 1.4

# 游戏性
TITLE = str(TIMER_SECONDS) + "S by zhangshenjia"
FPS = 60
SHIP_SPEED = 200
MUSIC_VOLUME = 0.3

# 子弹
BULLETS_LIMIT = 50
BULLETS_DELAY = 200
BULLET_MIN_SPEED = 50
BULLET_MAX_SPEED = 200

# 游戏事件
EVENT_OVER = pygame.USEREVENT + 1
EVENT_READY = pygame.USEREVENT + 2
EVENT_MAKE_BULLET = pygame.USEREVENT + 2

# 资源类型
IMAGE_EXTS = ('.png', '.jpg', 'bmp')
AUDIO_EXTS = ('.wav', '.ogg', '.mdi')
MUSIC_EXTS = ('.ogg')
