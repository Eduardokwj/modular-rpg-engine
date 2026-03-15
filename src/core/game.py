import pygame
from src.core.config import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    GAME_TITLE
)
from src.states.gameplay_state import GameplayState

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
        self.current_state = GameplayState()
    
    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
        self.current_state.handle_events(events)


    def update(self):
        self.current_state.update()
    
    def render(self):
        self.current_state.render(self.screen)
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
