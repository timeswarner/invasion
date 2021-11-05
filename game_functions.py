import sys 
import pygame
from bullet import Bullet

def _check_keydown_events(self, event):
    """相应按键"""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        _fire_bullet(self)

def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    if event.key == pygame.K_LEFT:
        self.ship.moving_left = False

def _fire_bullet(self):
    """创建一颗子弹，并将其加入编组bullets中。"""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

def _check_events(self):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(self, event)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(self, event)

def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

def update_screen(self):
    """更新屏幕上的图像，并切换到新屏幕"""
    self.screen.fill(self.settings.bg_color)

    # 每次循环时都要重绘飞船
    self.ship.blitme()

    # 重绘组里面的子弹
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()