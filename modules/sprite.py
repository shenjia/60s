import pygame

class Sprite(pygame.sprite.Sprite):

    template = {
        'rect' : pygame.Rect(0, 0, 0, 0),
        'X' : 0,
        'Y' : 0
    }

    def __init__(self, config = {}):
        pygame.sprite.Sprite.__init__(self)
        config = dict(self.template, **config)
        for key in config:
            setattr(self, key, config[key])

    def move(self, position):
        self.X, self.Y = position

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)

    def update(self):
        pygame.sprite.Sprite.update(self)
        self.rect.centerx = self.X
        self.rect.centery = self.Y

    @property
    def position(self):
        return (self.X, self.Y)

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height
