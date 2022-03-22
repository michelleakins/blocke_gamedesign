import pygame, time
pygame.init()
wind = pygame.display.set_mode((700,700))
pygame.display.set_caption('testing')
#create title

TITLE_FNT= pygame.font.SysFont('helvetica', 80)
MENU_FNT = pygame.font.SysFont('helvetica', 40)
INS_FNT = pygame.font.SysFont('helvetica', 25)

text = TITLE_FNT.render('HELL', 1, (255, 0, 0))
wind.fill((255,255,255))
wind.blit(text,(50,50))
# text = INS_FNT.render("Write y", 1, (0,255,0))
# wind.blit(text(220,220))

pygame.display.update()
pygame.time.delay(100000000)
