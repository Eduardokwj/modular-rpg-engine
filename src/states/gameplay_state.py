from src.states.base_state import BaseState
from src.core.config import BACKGROUND_COLOR

class GameplayState(BaseState):
    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill(BACKGROUND_COLOR)

        