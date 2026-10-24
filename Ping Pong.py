#Gerekli Kütüphanelerin İmport Edilmesi
import pygame , sys

#Gerekli Değişkenler
YESİL = (0, 255, 0)
MAVİ = (0, 0, 255)
KIRMIZI = (255, 0, 0)
BEYAZ = (255, 255, 255)
SİYAH = (0, 0, 0)
EKRAN_GENISLIK = 1280
EKRAN_YUKSEKLIK = 720
RAKET_GENISLIK = 15
RAKET_YUKSEKLİK = 100
TOP_BOYUT = 20
RAKET_HIZ = 8
TOP_HIZ_X = 7
TOP_HIZ_Y = 7
oyuncu1_skor = 0
oyuncu2_skor = 0
oyuncu1_raket = pygame.Rect(30, EKRAN_YUKSEKLIK // 2 - RAKET_YUKSEKLİK // 2, RAKET_GENISLIK, RAKET_YUKSEKLİK)
oyuncu2_raket = pygame.Rect(EKRAN_GENISLIK - 30 - RAKET_GENISLIK, EKRAN_YUKSEKLIK // 2 - RAKET_YUKSEKLİK // 2, RAKET_GENISLIK, RAKET_YUKSEKLİK)
top = pygame.Rect(EKRAN_GENISLIK // 2 - TOP_BOYUT // 2, EKRAN_YUKSEKLIK // 2 - TOP_BOYUT // 2, TOP_BOYUT, TOP_BOYUT)

#Pygamenin Başlatılması Ve Oyun İçin Gerekli OLan Değişkenlerin Hazırlanması
pygame.init()
screen = pygame.display.set_mode((EKRAN_GENISLIK, EKRAN_YUKSEKLIK))
pygame.display.set_caption("PİNGPONG OYUNU")
FPS = pygame.time.Clock()
top_vurus_sesi = pygame.mixer.Sound("Assests/ball hit.wav")
gol_yeme_sesi = pygame.mixer.Sound("Assests/loose.wav")

#Ana Döngü
while True:
    #Kapatma Tuşuna Basıldığında Oyunun Kapanması
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Hareket İçin Tuş Atamaları
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_w] and oyuncu1_raket.top > 0:
        oyuncu1_raket.y -= RAKET_HIZ
    if tuslar[pygame.K_s] and oyuncu1_raket.bottom < EKRAN_YUKSEKLIK:
        oyuncu1_raket.y += RAKET_HIZ
    if tuslar[pygame.K_UP] and oyuncu2_raket.top > 0:
        oyuncu2_raket.y -= RAKET_HIZ
    if tuslar[pygame.K_DOWN] and oyuncu2_raket.bottom < EKRAN_YUKSEKLIK:
        oyuncu2_raket.y += RAKET_HIZ

    #Topun Hızı
    top.x += TOP_HIZ_X
    top.y += TOP_HIZ_Y

    #Eğer Top Pencerenin Kenarına Gelirse Sekmesi
    if top.top <= 0 or top.bottom >= EKRAN_YUKSEKLIK:
        TOP_HIZ_Y =- TOP_HIZ_Y
        top_vurus_sesi.play()

    #Top Rakete Değerse Sekmesi
    if top.colliderect(oyuncu1_raket) or top.colliderect(oyuncu2_raket):
        TOP_HIZ_X =- TOP_HIZ_X
        top_vurus_sesi.play()

    #Oyuncu1 Topu Tutamazsa Oyuncu2 Ye Puan Verilmesi Ve Topun Ortadan Başlaması
    if top.left <= 0:
        oyuncu2_skor += 1
        top.x = EKRAN_GENISLIK // 2 - TOP_BOYUT // 2
        top.y = EKRAN_YUKSEKLIK // 2 - TOP_BOYUT // 2
        TOP_HIZ_X =- TOP_HIZ_X
        gol_yeme_sesi.play()

    #Bu Durumun Oyuncu1 Hali
    if top.right >= EKRAN_GENISLIK:
        oyuncu1_skor += 1
        top.x = EKRAN_GENISLIK // 2 - TOP_BOYUT // 2
        top.y = EKRAN_YUKSEKLIK // 2 - TOP_BOYUT // 2
        TOP_HIZ_X =- TOP_HIZ_X
        gol_yeme_sesi.play()

    #Ekranı Siyaha Boyayıp Önceden Kalan Artıkları Temizler
    screen.fill(SİYAH)

    #Top Raket Ve Çizgilerin Çizilmesi
    pygame.draw.rect(screen,KIRMIZI, oyuncu1_raket)
    pygame.draw.rect(screen, MAVİ, oyuncu2_raket)
    pygame.draw.circle(screen,BEYAZ,(EKRAN_GENISLIK//2,EKRAN_YUKSEKLIK//2),130,1)
    pygame.draw.ellipse(screen, YESİL, top)
    pygame.draw.aaline(screen, BEYAZ, (EKRAN_GENISLIK // 2, 0), (EKRAN_GENISLIK // 2, EKRAN_YUKSEKLIK))

    #Skor Bilgisi Yazılması
    font = pygame.font.Font(None, 74)
    text = font.render(str(oyuncu1_skor), True, BEYAZ)
    screen.blit(text, (EKRAN_GENISLIK // 4, 10))
    text = font.render(str(oyuncu2_skor), True, BEYAZ)
    screen.blit(text, (EKRAN_GENISLIK * 3 // 4, 10))

    #Ekranı Tazelemesi
    pygame.display.update()
    
    #Oyun FPS si
    FPS.tick(60)