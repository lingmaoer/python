# -*- encoding: utf-8 -*-
# @Time     :2020/11/20 20:24
# @Author   :lingmao
# @File     :贪吃蛇.py
# @Software :PyCharm

import pygame
import random
import sys
from pygame.locals import *

pygame.init()

redColor = pygame.Color(255, 0, 0)  # 食物颜色
blackColor = pygame.Color(0, 0, 0)  # 背景
whiteColor = pygame.Color(255, 255, 255)  # 蛇

snakePosition = [100, 100]  # 蛇位置
snakebody = [[100, 100], [80, 100], [60, 100]]  # 蛇身位置
targetPosition = [300, 300]
targetflage = 1
direction = 'right'
score = 0  # 分数

playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption("贪吃蛇     你的分数：{}".format(score))
while True:
    playSurface.fill(blackColor)
    for poition in snakebody:
        pygame.draw.rect(playSurface, whiteColor, Rect(snakePosition[0], 20, 20))
        pygame.draw.rect(playSurface, redColor, Rect(targetPosition[0], targetPosition[1], 20, 20))
        
