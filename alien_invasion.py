import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # 设置背景色
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视鼠标和键盘事件
            gf.check_events(self.ship)
            self.ship.update()
            gf.update_screen(ai.settings, self.screen, self.ship)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
