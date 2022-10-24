import pygame
esc = int(input('Escolha 1 ou 2 para ouvir uma dessas opções: \n 1. Gorillaz Feel Good Inc \n 2. Gorillaz Clint Eastwood \n'))
if esc == 1:
 pygame.init()
 pygame.mixer.music.load('music.mp3')
 pygame.mixer.music.play()
 input()
 pygame.event.wait()
else:
 pygame.init()
 pygame.mixer.music.load('ClintGllz.mp3')
 pygame.mixer.music.play()
 input()
 pygame.event.wait()






