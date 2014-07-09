from game_func import *
from game import Game

def main():
    pygame.init()
    print("bonjour monde")
    pygame.display.set_caption("Menu")
    fenetre = pygame.display.set_mode((960, 720)) 
    next =1
    font = pygame.image.load("images/background.jpg").convert()
    play = pygame.image.load("images/start.png").convert()
    quit = pygame.image.load("images/quit.png").convert()
    fenetre.blit(font,(0,0))
    fenetre.blit(play,(418,173))
    fenetre.blit(quit, (418,369))
    pygame.display.flip()
    quit_r = quit.get_rect()
    quit_r.x, quit_r.y = 418, 369
    game = Game()
    while next:
        for event in pygame.event.get():
            if event.type == QUIT:
                next = 0
            if event.type == MOUSEBUTTONDOWN:
                print("text")
                x, y = event.pos
                if ( x in range(418,543)) and (y in range(369,398)):
                    next = 0
                elif ( x in range(418,543)) and (y in range (173,202)):
                    start_player(fenetre,game)        

    pygame.quit()

if __name__ == "__main__":
    main()
