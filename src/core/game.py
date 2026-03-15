import pygame
from src.core.config import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    GAME_TITLE,
    BACKGROUND_COLOR
)

class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.title = GAME_TITLE

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.is_running = True
        self.fps = FPS
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass
    
    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

        self.quit()

    def quit(self):
        pygame.quit()
