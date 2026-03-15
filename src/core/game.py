import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen_width =800
        self.screen_height = 600
        self.title = "Modular RPG Engine"

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.is_running = True
        self.fps = 60
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass
    
    def render(self):
        self.screen.fill((30,30,30))
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
