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

hero = pygame.image.load("./素材/me1.png")

screen.blit(hero, (150, 300))

# 更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

#记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            print("退出游戏")
            # 卸载所有模块
            pygame.quit()

            # 终止程序
            exit()


    # 修改飞机位置
    hero_rect.y -= 3

    # 判断飞机位置
    if hero_rect.y <= -126:

        hero_rect.y = 700

    # 重新绘制屏幕
    screen.blit(bg, (0, 0))

    # 绘制图像
    screen.blit(hero, hero_rect)

    # 更新屏幕
    pygame.display.update ()

pygame.quit()