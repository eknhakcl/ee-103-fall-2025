import pygame
import random
import os

# --- Oyun Ayarları ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Renkler (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (165, 3, 52)
GREEN = (0, 255, 0)
BLUE = (255, 0, 255)
YELLOW = (255, 255, 0)

# --- Pygame Başlatma ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("90'lar Arcade Uzay Nişancısı")
clock = pygame.time.Clock()

# --- Varlık Yükleme (Basit Çizimler Kullanıyoruz, İstersen Resim Ekleyebilirsin) ---

# Oyuncu
player_width = 50
player_height = 50
player_image = pygame.Surface((player_width, player_height))
player_image.fill(BLUE) # Oyuncuyu mavi kare olarak çiziyoruz
player_speed = 5

# Düşman
enemy_width = 40
enemy_height = 40
enemy_image = pygame.Surface((enemy_width, enemy_height))
enemy_image.fill(RED) # Düşmanları kırmızı kare olarak çiziyoruz
enemy_speed = 3

# Mermi
bullet_width = 10
bullet_height = 20
bullet_image = pygame.Surface((bullet_width, bullet_height))
bullet_image.fill(YELLOW) # Mermileri sarı dikdörtgen olarak çiziyoruz
bullet_speed = -10 # Y ekseninde yukarı doğru hareket edeceği için eksi değer

# Font
font_name = pygame.font.match_font('arial') # Varsayılan font

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# --- Sınıflar ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -player_speed
        if keystate[pygame.K_RIGHT]:
            self.speedx = player_speed
        self.rect.x += self.speedx
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40) # Ekranın üstünden başlar
        self.speedy = random.randrange(1, enemy_speed + 2) # Daha hızlı düşmanlar için
        self.speedx = random.randrange(-1, 1) # Yana doğru hafif hareket

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 25:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, enemy_speed + 2)
            self.speedx = random.randrange(-1, 1)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = bullet_speed

    def update(self):
        self.rect.y += self.speedy
        # Eğer ekran dışına çıkarsa sil
        if self.rect.bottom < 0:
            self.kill()

# --- Oyun Döngüsü ---
def show_go_screen():
    screen.blit(pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0)) # Arka planı karart
    draw_text(screen, "90'lar Uzay Nişancısı!", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    draw_text(screen, "Ok tuşları ile hareket et, Boşluk ile ateş et", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    draw_text(screen, "Oyuna başlamak için bir tuşa bas", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP: # Bir tuşa basıldığında oyuna başla
                waiting = False

game_over = True
running = True
score = 0

while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8): # Başlangıçta 8 düşman
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)
        score = 0

    clock.tick(FPS)
    # --- Olay İşleme ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # --- Güncelleme ---
    all_sprites.update()

    # Düşman-Mermi Çarpışmaları
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 10 # Her vuruşta puan
        e = Enemy() # Vurulan düşman yerine yenisi
        all_sprites.add(e)
        enemies.add(e)

    # Oyuncu-Düşman Çarpışmaları
    hits = pygame.sprite.spritecollide(player, enemies, True) # Oyuncu ve düşman çarpışırsa düşman silinir
    if hits:
        game_over = True # Oyun biter

    # --- Çizim ---
    screen.fill(BLACK) # Arka planı siyah yap
    all_sprites.draw(screen) # Tüm sprite'ları çiz

    draw_text(screen, f"Puan: {score}", 18, SCREEN_WIDTH / 2, 10) # Skoru göster

    # --- Ekranı Güncelle ---
    pygame.display.flip()

pygame.quit()