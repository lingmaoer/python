import pygame

pygame.init()
# 创建窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像
bg = pygame.image.load("./素材/background.png")
# 绘制图像
screen.blit(bg, (0, 0))
# screen.blit(bg, (100, 100))
# 更新屏幕显示
# pygame.display.update()

hero = bg = pygame.image.load("./素材/me1.png")

screen.blit(bg, (200, 500))

# 更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

while True:
    #可以指定循环体内部的代码执行的频率
    clock.tick(60)
    pygame.event.get()


pygame.quit()