import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((1920, 768))
done = False
bg_img = pygame.image.load('/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex1/images/main-clock.png')
sec_img = pygame.image.load('/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex1/images/left-hand.png')
min_img = pygame.image.load('/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex1/images/right-hand.png')
rect = bg_img.get_rect(center=(415, 418))

while not done:
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = nsec_img.get_rect(center = rect.center)
    screen.blit(nsec_img, sec_rect.topleft)

    min_angle = -(time.minute * 6)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center = rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()
