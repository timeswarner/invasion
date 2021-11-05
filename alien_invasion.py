import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        # 创建一个设置类
        self.settings = Settings()

        # 创建屏幕，设置屏幕的宽度和高度 设置屏幕的标题
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        # 创建飞船
        self.ship = Ship(self.settings, self)
        
        # 创建用于存储子弹的分组
        self.bullets = pygame.sprite.Group()

        # 设置背景色
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            
            # 监视鼠标和键盘事件
            gf._check_events(self)
            
            # 更新飞船
            self.ship.update()            
            
            # 更新子弹
            gf._update_bullets(self)
            
            # 更新屏幕
            gf.update_screen(self)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
