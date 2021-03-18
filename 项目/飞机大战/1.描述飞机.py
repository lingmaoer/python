import pygame

hero_rect = pygame.Rect(100,500,120,125)

print(f"英雄原点 {hero_rect.x} {hero_rect.y}")
print(f"英雄尺寸 {hero_rect.width} {hero_rect.height}")
print("%d %d"%hero_rect.size)