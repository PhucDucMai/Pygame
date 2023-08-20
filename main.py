import pygame
# HP 2 - Bài 4: Biết cách sử dụng module
import random
import Draw 

pygame.init()

# Kích thước khung cửa sổ màn hình game (HP4 - Bài 1: tạo cửa sổ trò chơi)
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

img = pygame.image.load("backgroud.jpg")
img_scale = pygame.transform.scale(img, (800, 600)).convert_alpha()

pygame.display.set_caption("Overcoming obstacles")

font = pygame.font.Font(None, 50)

# âm thanh game (HP1 - Bài 5: cách ghi chú)
play_game = pygame.mixer.Sound("background.wav")
stop = pygame.mixer.Sound("stop.mp3")
click = pygame.mixer.Sound('click.mp3')
menu = pygame.mixer.Sound('menu_mp3.mp3')
# HP 4 0- mixer
end = pygame.mixer.Sound('end.mp3')

# Màn hình Menu
Game_Screen_Menu = pygame.display.set_mode((800,600))
img_menu = pygame.image.load('menu.jpg')
img_menu_scale = pygame.transform.scale(img_menu, (800, 600)).convert_alpha()

# Game over
gameOver = pygame.display.set_mode((800, 600)) # sử dụng ảnh (HP4)
img_game_over = pygame.image.load("game_over.jpg").convert_alpha() 
img_game_over_scale = pygame.transform.scale(img_game_over, (800, 600)) # thay đổi kích thước ảnh (HP4)

# Màn hình hướng dẫn
game_screen_guide = pygame.display.set_mode((800,600))
img_backgroud_guide = pygame.image.load("game_guide.jpg")
img_backgroud_guide_scale = pygame.transform.scale(img_backgroud_guide,(800,600))

# điểm số (HP2 - Bài 2: Tìm hiểu về hàm , cú pháp và định nghĩa hàm)

def display_score():
    # HP 1 - Bài 4: Áp dụng toán tử vào tính toán
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    # HP4 - bài 1 (sử dụng màu) , HP2 - Bài 8 (Hiển thị điểm)
    score_surf = font.render(
        f"Your score: {current_time}", False, (64, 64, 64) 
    ).convert_alpha()
    score_rect = score_surf.get_rect(center=(400, 30)) # HP4 - Bài 1: Biết vẽ hình cơ bản
    screen.blit(score_surf, score_rect)
    # HP2 - Bài 3 (Từ khóa return và tác dụng)
    return current_time

start_time = 0


# Người chơi (HP3 - Bài 1: Biết tạo class và dùng class giải quyết vấn đề )
# HP4 - Bài 2: Áp dụng class sprite
class Player(pygame.sprite.Sprite):
    # HP3 - Bài 2:  Phân biệt hàm constructor với hàm thường và biết áp dụng vào lập trình OOP 
    def __init__(self):
        super(Player, self).__init__()
        self.img_player = pygame.image.load("airplane.png")
        self.img_player_scaler = pygame.transform.scale(self.img_player, (60, 60))
        self.surf = self.img_player_scaler.convert_alpha()
        self.rect = self.surf.get_rect()
        
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
    
    def update(self):
        # máy bay di chuyển (HP4 - Bài 6: Lập trình cho nhân vật di chuyển)
        if self.move_up:
            self.rect.move_ip(0, -10)
        if self.move_down:
            self.rect.move_ip(0, 10)
        if self.move_left:
            self.rect.move_ip(-10, 0)
        if self.move_right:
            self.rect.move_ip(10, 0)

        # kiểm soát máy bay không ra khỏi màn hình game (HP4 - Bài 2: Hình khối kì diệu , kiểm soát đối tượng chỉ hoạt động trong màn hình)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


player = Player()


# Chướng ngại vật 
class Enemy(pygame.sprite.Sprite):
    # attriubute: img_fly , surf , rect , speed | method: __init__ , update() , kill() : HP4 - Bài 5
    def __init__(self):
        super(Enemy, self).__init__()
        self.img_fly = pygame.image.load("fl.png")
        self.surf = pygame.transform.flip(self.img_fly, True, False).convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH + 20, WIDTH + 35),
                random.randint(0 + 5, HEIGHT - 5),
            )
        )
        self.speed = random.randint(3, 7)

    # ra khỏi màn hình thì sẽ không xử lý nữa
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Sự kiện thêm đối thủ với set_timer
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

# xóa mọi đối thủ khỏi màn hình
EMPTY_ENEMIES = pygame.USEREVENT + 2

# Xử dụng sprite group (HP4 - )
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

# game speed
clock = pygame.time.Clock()

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

# Màn hình hướng dẫn
def game_guide():
    # HP2 - Bài 3 (Phạm vi biến trong hàm)
    global game_screen
    game_screen_guide.blit(img_backgroud_guide_scale,(0,0))
    Draw.draw_text(game_screen_guide,'Game Guide: Overcoming obstacles' , 60 , green , 35 , 50)
    Draw.draw_text(game_screen_guide,'1: You need to control the plane away from the birds' , 30 , (13, 12, 12) , 10 , 150)
    Draw.draw_text(game_screen_guide,'2: Use the arrow buttons to control the plane' , 30 , (13, 12, 12) , 10 , 200)
    Draw.draw_text(game_screen_guide,'3: At Menu click on Play to play game' , 30 , (13, 12, 12) , 10 , 250)
    Draw.draw_text(game_screen_guide,'4: At the end screen (game over):' , 30 , (13, 12, 12) , 10 , 300)
    Draw.draw_text(game_screen_guide,'+) Click continue to play the game' , 30 , (13, 12, 12) , 30 , 330)
    Draw.draw_text(game_screen_guide,'+) Click on the menu to return to the main menu' , 30 , (13, 12, 12) , 30 , 360)
    Draw.draw_text(game_screen_guide,'5: At the game screen, press space to pause the game:' , 30 , (13, 12, 12) , 10 , 410)
    Draw.draw_text(game_screen_guide,'Have fun playing the game' , 60 , green , 100 , 450)
    # HP4 - Bài 1: Biết cách sử dụng màu để vẽ hình khối
    Draw.draw_button(game_screen_guide,"Press space to return to Menu",450,520,320,50,black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # HP4 - Bài 2: hàm tương tác phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_screen = "menu"
                game_menu()

# Màn hình hiển thị Menu    
def game_menu():
    # menu.play()
    menu.set_volume(0.005)
    global game_screen
    global active_game
    Game_Screen_Menu.fill(color="black")
    Game_Screen_Menu.blit(img_menu_scale,(0,0))
    play_button_rect = pygame.Rect(300, 200, 200, 50)
    Draw.draw_button(Game_Screen_Menu,"Play", 300, 200, 200, 50, green)
    help_button_rect = pygame.Rect(300, 300, 200, 50)
    Draw.draw_button(Game_Screen_Menu,"Guide", 300, 300, 200, 50, green)
    quit_button_rect = pygame.Rect(300, 400, 200, 50)
    Draw.draw_button(Game_Screen_Menu,"Quit", 300, 400, 200, 50, red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
             # HP3 - Bài 4: Xử lý sự kiện click vào button
            if play_button_rect.collidepoint(mouse_pos):
                menu.stop()
                # click.play()
                pygame.time.delay(800)
                start_new_game()  
            elif help_button_rect.collidepoint(mouse_pos):
                menu.stop()
                # click.play()
                game_screen = "guide"
                game_guide()
            elif quit_button_rect.collidepoint(mouse_pos):
                menu.stop()
                # click.play()
                pygame.time.delay(800)
                pygame.quit()

# Màn hình chơi game
def game_playing():
    global active_game
    global game_screen
    global score
    global is_paused
    global pause_startTime
    if is_paused == True:
        Draw.draw_text(screen,"Game Pause (Press enter to continue playing)",40,(255, 0, 0), 80, 300)
    else:
        # Màu nền
        screen.fill((135, 206, 250))
        # Ảnh nền
        screen.blit(img_scale, (0, 0))
        # Vẽ người chơi : HP4 - surface
        screen.blit(player.surf, player.rect)
        # Thêm chướng ngại vật lên màn hình game
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            
        enemies.update()
        
        if active_game:
            # play_game.play()
            play_game.set_volume(0.005)
            score = display_score()
            # Sử dụng sprite để xử lý va chạm
            if pygame.sprite.spritecollideany(player, enemies):
                player.kill()
                play_game.stop()
                # stop.play()
                stop.set_volume(0.005)
                game_screen = "game_over"
                active_game = False
        else:
            screen_game_over()

# Màn hình game over       
def screen_game_over():
    global active_game
    global score
    global game_screen
    global start_time
    play_game.stop()
    # end.play()
    end.set_volume(0.005)
    gameOver.fill((135, 206, 250))
    gameOver.blit(img_game_over_scale, (0, 0))
    score_display = font.render(f'Your Score: {score}', False, (50, 168, 104)).convert_alpha()
    score_display_rect = score_display.get_rect(center=(400, 150))
    gameOver.blit(score_display, score_display_rect)

    continue_button = pygame.Rect(300, 400, 200, 50)
    Draw.draw_button(gameOver,"Continue", 300, 400, 200, 50, green)

    menu_button = pygame.Rect(300, 500, 200, 50)
    Draw.draw_button(gameOver,"Menu", 300, 500, 200, 50, green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # HP4 - Bài 4: Dùng hàm để xử lý va chạm
            if continue_button.collidepoint(mouse_pos):
                # click.play()
                end.stop()
                pygame.time.delay(800)
                game_screen = "new_game"
                active_game = True
                start_time = int(pygame.time.get_ticks() / 1000)
                enemies.empty()  
                all_sprites.empty()  
                start_new_game()
    
            elif menu_button.collidepoint(mouse_pos):
                # click.play()
                end.stop()
                pygame.time.delay(800)
                game_screen = "menu"
                active_game = True
                start_time = int(pygame.time.get_ticks() / 1000)  
                enemies.empty()  
                all_sprites.empty() 
                game_menu()
                
        # HP 4 - Bài 2 (Tương tác với phím)        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up = True
            elif event.key == pygame.K_DOWN:
                player.move_down = True
            elif event.key == pygame.K_LEFT:
                player.move_left = True
            elif event.key == pygame.K_RIGHT:
                player.move_right = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.move_up = False
            elif event.key == pygame.K_DOWN:
                player.move_down = False
            elif event.key == pygame.K_LEFT:
                player.move_left = False
            elif event.key == pygame.K_RIGHT:
                player.move_right = False

# Màn hình new game: HP 2 - bài 2: dùng hàm
def start_new_game():
    menu.stop()
    global active_game
    global game_screen
    global score
    global start_time
    active_game = True  
    game_screen = "playing"
    all_sprites.add(player)
    player.rect.topleft = (5,random.randint(10,30))  
    player.alive()  
    score = 0 
    start_time = int(pygame.time.get_ticks() / 1000)
    # play_game.play() 
    play_game.set_volume(0.009)
    pygame.time.set_timer(ADDENEMY, 500)   

# Biến lưu trạng thái màn hình , trạng thái game , trạng thái dừng và trạng thái của vòng lặp while
# HP1 - Bài 4: các kiểu dữ liệu , đặt tên biến 
game_screen = "menu"

active_game = True

is_paused = False

running = True

# HP1 - Bài 5 (Vòng lặp while)
while running:
    if game_screen == "menu":
        game_menu()
    
    elif game_screen == "playing":
        game_playing()
        
    elif game_screen == "game_over":
        screen_game_over()
    
    elif game_screen == "new_game":
        start_new_game()
    
    elif game_screen == "guide":
        game_guide()
    # HP1 - Bài 6: Vòng lặp for
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # HP1 - Bài 7: Cú pháp if - elif - else lồng nhau
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_paused = True
                # HP1 - Bài 3
                print("Bạn vừa nhấn vào phím SPACE")
            elif event.key == pygame.K_RETURN:
                print("Bạn vừa nhấn vào phím Enter")
                is_paused = False
            # Sự kiện điều khiển máy bay lên xuống
            if event.key == pygame.K_UP:
                player.move_up = True
            elif event.key == pygame.K_DOWN:
                player.move_down = True
            elif event.key == pygame.K_LEFT:
                player.move_left = True
            elif event.key == pygame.K_RIGHT:
                player.move_right = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.move_up = False
            elif event.key == pygame.K_DOWN:
                player.move_down = False
            elif event.key == pygame.K_LEFT:
                player.move_left = False
            elif event.key == pygame.K_RIGHT:
                player.move_right = False
        
        player.update()
        
        if event.type == ADDENEMY:
            # thêm chướng ngại vật mới
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
        if event.type == EMPTY_ENEMIES:
            # xóa chướng ngại vật
            enemies.empty()
            all_sprites.empty()
            enemies.update()

    # Khung hình / giây
    clock.tick(60)

    # Cập nhật thay đổi
    pygame.display.flip()

    pygame.display.update()
    
pygame.quit()
