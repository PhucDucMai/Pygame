import pygame

# HP2 - Bài 8 (Hiển thị text)
def draw_text(screen,text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# HP2 - Bài 3 (hàm có tham số)
def draw_button(screen,text, x, y, width, height, color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    font = pygame.font.Font(None, 30)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)