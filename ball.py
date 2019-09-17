import  pygame

from pygame.sprite import Sprite

class ball1(Sprite):
    def __init__(self, ai_settings, screen, kunkun):

        super(ball1, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('pic/basketball.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = kunkun.rect.centerx
        self.rect.top = kunkun.rect.top

        self.y = float(self.rect.y)

        # self.color = ai_settings.ball_color

        self.speed_factor = ai_settings.ball_speed_factor

    def update(self):

        self.y -= self.speed_factor

        self.rect.y = self.y

    def draw_ball(self):
         self.screen.blit(self.image, self.rect)

