import pygame
import random

# --- Ayarlar ---
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
CARD_WIDTH = 100
CARD_HEIGHT = 140
CARD_SPACING = 20  # Kartlar arası yığın boşluğu
BACKGROUND_COLOR = (0, 100, 0)  # Koyu Yeşil (Masa Rengi)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GRAY = (150, 150, 150)

# Kart Sembolleri ve İsimleri
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Solitaire")
clock = pygame.time.Clock()
font = pygame.font.SysFont('segoeuisymbol', 30)  # Sembolleri destekleyen bir font
small_font = pygame.font.SysFont('arial', 20)

class Card:
    def __init__(self, suit, rank_idx):
        self.suit = suit
        self.rank_idx = rank_idx  # 0-12 (A-K)
        self.rank_str = RANKS[rank_idx]
        self.color = RED if suit in ['♥', '♦'] else BLACK
        self.face_up = False
        self.rect = pygame.Rect(0, 0, CARD_WIDTH, CARD_HEIGHT)
        self.original_pos = (0, 0) # Sürükleme iptal edilirse döneceği yer

    def draw(self, surface, x, y):
        self.rect.topleft = (x, y)
        # Kartın çerçevesi ve arka planı
        pygame.draw.rect(surface, WHITE if self.face_up else (50, 120, 200), self.rect, border_radius=8)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=8)

        if self.face_up:
            # Sol üst köşe
            text = font.render(f"{self.rank_str}{self.suit}", True, self.color)
            surface.blit(text, (x + 5, y + 5))
            # Sağ alt köşe (ters)
            rotated_text = pygame.transform.rotate(text, 180)
            surface.blit(rotated_text, (x + CARD_WIDTH - 35, y + CARD_HEIGHT - 35))
            
            # Ortaya büyük sembol
            center_suit = pygame.font.SysFont('segoeuisymbol', 60).render(self.suit, True, self.color)
            center_rect = center_suit.get_rect(center=self.rect.center)
            surface.blit(center_suit, center_rect)
        else:
            # Kart arkası deseni
            pygame.draw.rect(surface, WHITE, (x + 10, y + 10, CARD_WIDTH - 20, CARD_HEIGHT - 20), 2)
            pygame.draw.line(surface, WHITE, (x, y), (x + CARD_WIDTH, y + CARD_HEIGHT), 1)
            pygame.draw.line(surface, WHITE, (x + CARD_WIDTH, y), (x, y + CARD_HEIGHT), 1)

class Game:
    def __init__(self):
        self.deck = []
        self.piles = [[] for _ in range(7)] # 7 Tableau sütunu
        self.foundations = [[] for _ in range(4)] # 4 Hedef yuvası
        self.stock = [] # Çekme destesi
        self.waste = [] # Açılan kartlar
        
        self.dragging_cards = [] # Şu an sürüklenen kart grubu
        self.drag_start_pos = (0, 0) # Mouse'un ilk tıkladığı yer
        self.source_pile = None # Kartın geldiği yer

        self.create_deck()
        self.deal()

    def create_deck(self):
        for suit in SUITS:
            for i in range(13):
                self.deck.append(Card(suit, i))
        random.shuffle(self.deck)

    def deal(self):
        # 7 Sütuna dağıt
        for i in range(7):
            for j in range(i + 1):
                card = self.deck.pop()
                if j == i:
                    card.face_up = True
                self.piles[i].append(card)
        
        # Geri kalanı stoğa koy
        self.stock = self.deck[:]
        self.deck = []

    def get_pile_at_pos(self, pos):
        # Mouse pozisyonuna göre hangi yığında olduğumuzu bulur
        x, y = pos
        
        # Waste (Açık deste)
        if 130 < x < 130 + CARD_WIDTH and 20 < y < 20 + CARD_HEIGHT:
            return "waste", self.waste

        # Foundations (Hedefler)
        for i in range(4):
            fx = 350 + (i * (CARD_WIDTH + 20))
            if fx < x < fx + CARD_WIDTH and 20 < y < 20 + CARD_HEIGHT:
                return "foundation", self.foundations[i]

        # Tableau (Oyun alanı)
        for i in range(7):
            px = 20 + (i * (CARD_WIDTH + 20))
            # Sütunun en altındaki kartın alanını kontrol et (kabaca)
            if px < x < px + CARD_WIDTH and 180 < y < SCREEN_HEIGHT:
                return "tableau", self.piles[i], i
        
        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        # --- Arayüz Alanları ---
        # Stock (Kapalı deste)
        pygame.draw.rect(screen, (0, 80, 0), (20, 20, CARD_WIDTH, CARD_HEIGHT), 2)
        if self.stock:
            self.stock[-1].draw(screen, 20, 20)
        else:
            # Yenile butonu gibi boş yuvarlak
            pygame.draw.circle(screen, (0, 150, 0), (20 + CARD_WIDTH//2, 20 + CARD_HEIGHT//2), 20, 2)

        # Waste (Açık deste)
        if self.waste:
            self.waste[-1].draw(screen, 140, 20)

        # Foundations (Hedefler)
        for i in range(4):
            x = 350 + (i * (CARD_WIDTH + 20))
            pygame.draw.rect(screen, (0, 80, 0), (x, 20, CARD_WIDTH, CARD_HEIGHT), 2)
            if self.foundations[i]:
                self.foundations[i][-1].draw(screen, x, 20)

        # Tableau (Oyun alanı)
        for i in range(7):
            x = 20 + (i * (CARD_WIDTH + 20))
            y = 180
            if not self.piles[i]:
                 pygame.draw.rect(screen, (0, 80, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)
            
            for idx, card in enumerate(self.piles[i]):
                # Sürüklenen kartları burada çizme, en son çizeceğiz
                if card not in self.dragging_cards:
                    card.draw(screen, x, y)
                y += 30 if card.face_up else 10

        # Sürüklenen Kartlar (En üstte görünsün diye en son çiziyoruz)
        for idx, card in enumerate(self.dragging_cards):
            card.draw(screen, card.rect.x, card.rect.y)

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Sol tık
                mx, my = pygame.mouse.get_pos()
                
                # 1. Stoktan Kart Çekme
                if 20 < mx < 20 + CARD_WIDTH and 20 < my < 20 + CARD_HEIGHT:
                    if self.stock:
                        card = self.stock.pop()
                        card.face_up = True
                        self.waste.append(card)
                    elif self.waste: # Stok boşsa Waste'i geri yükle
                        self.stock = self.waste[::-1] # Tersten koy
                        for c in self.stock: c.face_up = False
                        self.waste = []
                    return

                # 2. Kart Tutma İşlemi
                # Tableau kontrolü
                for i, pile in enumerate(self.piles):
                    start_y = 180
                    for idx, card in enumerate(pile):
                        card_y = start_y + (idx * (30 if idx > 0 and pile[idx-1].face_up else 10)) # Basit hesaplama
                        # Eğer bu kartın üzerindeyse
                        # (Gerçekçi hitbox için alttaki kartların üst kısımlarını hesaba katmak lazım ama basit tutuyoruz)
                        if card.face_up and card.rect.collidepoint(mx, my):
                            # Bu kartı ve altındakileri al
                            self.dragging_cards = pile[idx:]
                            # Orijinal listeyi güncelle
                            self.piles[i] = pile[:idx]
                            self.source_pile = ("tableau", i)
                            self.drag_start_pos = (mx, my)
                            # Kartların orijinal pozisyonlarını kaydet
                            for c in self.dragging_cards:
                                c.original_pos = c.rect.topleft
                            return
                        # Kapalı karta tıklandıysa ve en üstteyse aç
                        if not card.face_up and idx == len(pile)-1 and card.rect.collidepoint(mx, my):
                            card.face_up = True
                            return
                        
                        # Çizimdeki y kaymasını takip etmek zor, basitçe en üsttekini tutmayı deneyelim
                        # (Daha gelişmiş versiyonda burası rect listesiyle yapılır)
                        
                # Waste'den tutma
                if self.waste and self.waste[-1].rect.collidepoint(mx, my):
                    self.dragging_cards = [self.waste.pop()]
                    self.source_pile = ("waste", 0)
                    self.drag_start_pos = (mx, my)
                    self.dragging_cards[0].original_pos = self.dragging_cards[0].rect.topleft

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragging_cards:
                # Kartı Bırakma
                dropped = False
                mx, my = pygame.mouse.get_pos()
                lead_card = self.dragging_cards[0]

                # Hedef: Tableau
                for i in range(7):
                    x = 20 + (i * (CARD_WIDTH + 20))
                    # Sütun boşsa sadece Papaz (K) gelebilir
                    if not self.piles[i]:
                        if lead_card.rank_idx == 12 and x < mx < x + CARD_WIDTH and 180 < my < 300:
                            self.piles[i].extend(self.dragging_cards)
                            dropped = True
                            break
                    else:
                        top_card = self.piles[i][-1]
                        # Mesafe kontrolü ve Kural kontrolü (Zıt renk, 1 küçük sayı)
                        if top_card.rect.colliderect(lead_card.rect):
                            if top_card.color != lead_card.color and top_card.rank_idx == lead_card.rank_idx + 1:
                                self.piles[i].extend(self.dragging_cards)
                                dropped = True
                                break
                
                # Hedef: Foundation (Sadece tek kart ise)
                if not dropped and len(self.dragging_cards) == 1:
                    for i in range(4):
                        x = 350 + (i * (CARD_WIDTH + 20))
                        rect = pygame.Rect(x, 20, CARD_WIDTH, CARD_HEIGHT)
                        if rect.colliderect(lead_card.rect):
                            if not self.foundations[i]:
                                if lead_card.rank_idx == 0: # As (A)
                                    self.foundations[i].append(lead_card)
                                    dropped = True
                            else:
                                top_card = self.foundations[i][-1]
                                if top_card.suit == lead_card.suit and top_card.rank_idx == lead_card.rank_idx - 1:
                                    self.foundations[i].append(lead_card)
                                    dropped = True
                            break

                # Eğer geçerli bir yere bırakılmadıysa geri dön
                if not dropped:
                    if self.source_pile[0] == "tableau":
                        self.piles[self.source_pile[1]].extend(self.dragging_cards)
                    elif self.source_pile[0] == "waste":
                        self.waste.append(self.dragging_cards[0])
                    
                    # Görsel olarak geri ışınla
                    for c in self.dragging_cards:
                        c.rect.topleft = c.original_pos

                self.dragging_cards = []

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_cards:
                mx, my = pygame.mouse.get_pos()
                dx = mx - self.drag_start_pos[0]
                dy = my - self.drag_start_pos[1]
                
                for idx, card in enumerate(self.dragging_cards):
                    ox, oy = card.original_pos
                    card.rect.x = ox + dx
                    card.rect.y = oy + dy + (idx * 30) # Yığın halinde taşı

game = Game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.handle_input(event)

    game.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()