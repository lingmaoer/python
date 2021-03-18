import pygame

# 屏幕大小常量
SCREENT_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRANME_PER_SEC = 60

class Gamesprite(pygame.sprite.Sprite):
    # 飞机大战精灵
    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向移动
        self.rect.y +=self.speed

class Background(Gamesprite):
    # 游戏背景
    def update(self):

        # 调用父类的方法实现
        super().update()
        # 判断是否移除屏幕 是，移动到上面
        if self.rect.y >= SCREENT_RECT.y:
            self.rect.y = -SCREENT_RECT.height



class PlaneGame(object):
    # 飞机大战主有戏
    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREENT_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法,精灵，精灵组
        self.__creat_eprites()


    def __creat_eprites(self):
        bg1 = Background("./素材/background.png")
        bg2 = Background("./素材/background.png")
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)

    def start_game(self):
        print("游戏开始")
        while True:
            # 设置刷新频率
            self.clock.tick(FRANME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__updata_sprites()
            # 更新显示
            pygame.display.update()

            pass
    def __event_handler(self):
        for event in pygame.event.get():
            #判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __updata_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 游戏开始
    game.start_game()


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

# 创建敌机的精灵
enemy = Gamesprite("./素材/enemy1.png")
enemy1 = Gamesprite("./素材/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

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
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y <= -126:

        hero_rect.y = 700

    # 重新绘制屏幕
    screen.blit(bg, (0, 0))

    # 绘制图像
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # updata-- 让组内所有精灵更新位置
    enemy_group.update()
    # draw 在screen 显示精灵组
    enemy_group.draw(screen)


    # 更新屏幕
    pygame.display.update ()

pygame.quit()
