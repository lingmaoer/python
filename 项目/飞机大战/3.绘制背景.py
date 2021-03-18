import pygame

pygame.init()
# 创建窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像
bg = pygame.image.load("./素材/background.png")
# 绘制图像
# screen.blit(bg, (0, 0))
screen.blit(bg, (100, 100))
# 更新屏幕显示
pygame.display.update()

while True:
    pygame.event.get()


pygame.quit()