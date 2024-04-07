import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((590, 800))
bg = [
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/image/ironman2.jpg',
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/image/fuel.jpg',
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/image/wwry.jpg',
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/image/bohemian_rhapsody.jpg',
]

songs = [
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/mp3/AC:DC - Back in Black.mp3',
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/mp3/Metallica - Fuel.mp3',
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/mp3/Queens - We will rock you.mp3',
    '/Users/Suleimmen/Desktop/PP 2 lab. works/lab 7/ex2/mp3/Queens - Bohemian Raphsody.mp3',
]

bg_index = 0
bg_image = pygame.image.load(bg[bg_index]).convert()
converted_bg = pygame.transform.scale(bg_image, (590, 800))
pygame.mixer.music.load(songs[bg_index])
pygame.mixer.music.play()
play = False
finish = False

while not finish:
    screen.blit(converted_bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if bg_index == 3:
                    bg_index = 0
                else:
                    bg_index = bg_index + 1
                bg_image = pygame.image.load(bg[bg_index]).convert()
                converted_bg = pygame.transform.scale(bg_image, (590, 800))
                pygame.mixer.music.load(songs[bg_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                if bg_index == 0:
                    bg_index = 3
                else:
                    bg_index = bg_index - 1
                bg_image = pygame.image.load(bg[bg_index]).convert()
                converted_bg = pygame.transform.scale(bg_image, (590, 800))
                pygame.mixer.music.load(songs[bg_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                play = not play
                if play:
                    pygame.mixer.unpause()
                else:
                    pygame.mixer.music.pause()
    pygame.display.flip()
