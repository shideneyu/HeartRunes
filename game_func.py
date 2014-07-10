import pygame
from pygame.locals import *
from hand import Hand
from deck import Deck
from player import Player

def start_game(fenetre,game,player):
	pygame.display.set_caption("Titre")
	board = {'enemy0' : 'empty', 'enemy1' : 'empty', 'enemy2' : 'empty', 'enemy3' : 'empty', 'enemy4' : 'empty', 'player0' : 'empty', 'player1' : 'empty', 'player2' : 'empty', 'player3' : 'empty', 'player4' : 'empty'}
    
	#initiliase une fenetre redimmensionnable avec une largeur et une hauteur
	fenetre = pygame.display.set_mode((800, 650),RESIZABLE)

	#permet de charger une image de fond qui prend la taille de la fenetre
	fond = pygame.image.load("images/background2.jpg").convert()
	fenetre.blit(fond, (0,0))
	card = pygame.image.load("images/placecard.png").convert()
	#.convert_alpha() pour la transparence
	card2 = pygame.image.load("card.jpg").convert()
	card3 = pygame.image.load("card.jpg").convert()
	card4 = pygame.image.load("card.jpg").convert()
	card5 = pygame.image.load("card.jpg").convert()
	card6 = pygame.image.load("card.jpg").convert()
	card7 = pygame.image.load("card.jpg").convert()
	bar = pygame.image.load("images/bar.png").convert()
	health_bar = pygame.image.load("images/healthbar.png").convert()
	health_bar2 = pygame.image.load("images/healthbar.png").convert()
	mana_bar = pygame.image.load("images/manabar.png").convert()
	mana_bar2 = pygame.image.load("images/manabar.png").convert()
	deck = Deck(player)
	hand = Hand(deck)
	#hand.getHand()
	#place l'image
	card_x = 0
	card_y = 0
	#fenetre.blit(card, (card_x,card_y))
	fenetre.blit(card2, (200,300))
	game.showScores(fenetre)

	#game.startGame()
	#rafraichi la fenetre
	pygame.display.flip()
	continuer =1
	while continuer:
		for event in pygame.event.get(): #parcours la liste de tous les evenements
			if event.type == QUIT:
				continuer = 0
			#if event.type == VIDEORESIZE:#gere le redimensionnement de la fenetre
				#if event.w > 500 or event.h > 500:
			if event.type == KEYDOWN and event.key == K_SPACE:
				print("Espace")
			if event.type == MOUSEBUTTONDOWN:
				print("text")
				#if event.button == 1:
					#card_x = event.pos[0]
					#card_y = event.pos[1]
		fenetre.blit(fond, (0,0))
		#fenetre.blit(card, (00,550))
		fenetre.blit(bar, (0,480))
		fenetre.blit(bar, (0,100))
		display_board(fenetre, board)
		hand.getHandGraphic(fenetre)
		#fenetre.blit(health_bar, (500,30))
		#fenetre.blit(health_bar2, (490,500))
		#fenetre.blit(mana_bar, (500,75))
		#fenetre.blit(mana_bar2, (490,540))
		game.showScores(fenetre)
		




		#game.startGame(fenetre)
		pygame.display.flip()


def generate_element(fenetre):
	ump = pygame.image.load("images/ump.jpg").convert()
	fn = pygame.image.load("images/fn.jpg").convert()
	ps = pygame.image.load("images/ps.png").convert()
	pc = pygame.image.load("images/pc.png").convert()
	fenetre.blit(ump, (100,100))
	fenetre.blit(fn, (400,100))
	fenetre.blit(ps, (100,350))
	fenetre.blit(pc, (400,350))
	yellow = (0, 0, 0)
	white = (255,255,255)
	myfont = pygame.font.SysFont("Arial", 30)
	label = myfont.render("Veuillez choisir un parti", 1, yellow)
	fenetre.blit(label, (250,10))
#
def start_player(fenetre,game):
	turn_count = 0
	timer = 15
	history = ""

	yellow = (0, 0, 0)
	white = (255,255,255)
	myfont = pygame.font.SysFont("Arial", 30)
	#game.setPlayers()
	#game.showScores()
	#game.startGame()
	pygame.display.set_caption("Titre")

	#initiliase une fenetre redimmensionnable avec une largeur et une hauteur
	fenetre = pygame.display.set_mode((900, 600),RESIZABLE)
	#permet de charger une image de fond qui prend la taille de la fenetre
	fond = pygame.image.load("images/background2.jpg").convert()
	fenetre.blit(fond, (0,0))
	play = pygame.image.load("images/start.png").convert()
	generate_element(fenetre)
	cpt=0#nombre de tour
	flagump = 0#savoir quel parti a deja ete cliquer
	flagps = 0
	flagpc =0
	flagfn=0
	#rafraichi la fenetre
	pygame.display.flip()
	continuer =1
	while continuer:
		for event in pygame.event.get(): #parcours la liste de tous les evenements
			if event.type == QUIT:
				continuer = 0
			#if event.type == VIDEORESIZE:#gere le redimensionnement de la fenetre
				#if event.w > 500 or event.h > 500:
			if event.type == KEYDOWN and event.key == K_SPACE:
				print("Espace")
			if event.type == MOUSEBUTTONDOWN:
				x, y = event.pos
				if ( x in range(100,300)) and (y in range(100,300)):
					cpt+=1
					flagump+=1
					if(flagump==1 and cpt<3):
						if(cpt==1):
							print("rty")
							currentPlayer=Player("ump")
						currentPlayer=Player("ump")
						label2 = myfont.render("Player"+str(cpt)+" Vous avez choisi le parti ump", 1, yellow)
						if (cpt==2):
							#fenetre.subsurface(250, 500, 364, 64).fill(white)
							#pygame.display.update(250,500, 364, 64)
							fenetre.blit(fond,(0,0))
							fenetre.blit(play,(320,560))
							pygame.display.update(0, 0, 800, 350)
						generate_element(fenetre)
						fenetre.blit(label2, (100,500))
						pygame.display.flip()
						player = 0
						game.setPlayers(cpt-1,player)
						
				elif ( x in range(400,650)) and (y in range (100,300)):
					cpt+=1
					flagfn+=1
					if(flagfn==1 and cpt<3):
						if(cpt==1):
							currentPlayer=Player("fn")
						currentPlayer=Player("fn")


						label2 = myfont.render("Player"+str(cpt)+" Vous avez choisi le parti front national", 1, yellow)

						if (cpt==2):
							fenetre.blit(fond,(0,0))
							fenetre.blit(play,(320,560))
							pygame.display.update(0, 0, 800, 350)
						generate_element(fenetre)
						fenetre.blit(label2, (100,500))
						pygame.display.flip()
						print("fn")
						player = 1
						game.setPlayers(cpt-1,player)
						
				elif ( x in range(100,350)) and (y in range (350,550)):
					cpt+=1
					flagps+=1
					if(flagps==1 and cpt<3):
						if(cpt==1):
							currentPlayer=Player("ps")
						currentPlayer=Player("ps")
						label2 = myfont.render("Player"+str(cpt)+" Vous avez choisi le parti socialiste", 1, yellow)
						if (cpt==2):
							fenetre.blit(fond,(0,0))
							fenetre.blit(play,(320,560))
							pygame.display.update(0, 0, 800, 350)
						generate_element(fenetre)
						fenetre.blit(label2, (100,500))
						pygame.display.flip()
						print("ps")
						player = 2
						game.setPlayers(cpt-1,player)
						
				elif ( x in range(400,600)) and (y in range (350,550)):
					cpt+=1
					flagpc+=1
					if(flagpc==1 and cpt<3):
						if(cpt==1):
							currentPlayer=Player("communistes")
						currentPlayer=Player("communistes")
						label2 = myfont.render("Player"+str(cpt) +" Vous avez choisi le parti communiste", 1, yellow)
						if (cpt==2):
							fenetre.blit(fond,(0,0))
							fenetre.blit(play,(320,560))
							pygame.display.update(0, 0, 800, 350)
						generate_element(fenetre)
						fenetre.blit(label2, (100,500))
						pygame.display.flip()
						print("pc")
						player = 3
						game.setPlayers(cpt-1,player)

						
		

				elif ( x in range(320,600)) and (y in range (560,800)):
						print(currentPlayer.name)
						start_game(fenetre,game,currentPlayer)


def display_board(fenetre, board):
    font = pygame.font.Font(None, 20)
    font_name = pygame.font.Font(None, 15)
    board_case_empty = pygame.image.load("images/card_drop_green.jpg").convert()
    board_case_full = pygame.image.load("images/card_drop_red.jpg").convert()
    for i in range(0,3):
        if board['enemy'+str(i)] == 'empty':
            fenetre.blit(board_case_empty, (50 +(i*150),145))
        else:
            fenetre.blit(board_case_full, (50 +(i*150),145))
            model_card_front = pygame.image.load("images/card_model_hand.png").convert_alpha()
            temp_image = pygame.image.load("decks/img/"+str(board['enemy'+str(i)]['name'])+".png").convert()
            fenetre.blit(temp_image, (168+(i*150),150))
            fenetre.blit(model_card_front, (150+(i*150),150))   
            
            name = font_name.render(str(board['enemy'+str(i)]['name']), 1, (255, 255, 255))
            cost = font.render(str(board['enemy'+str(i)]['Cost']), 1, (255, 255, 255))
            health = font.render(str(board['enemy'+str(i)]['Health']), 1, (255, 255, 255))
            attack = font.render(str(board['enemy'+str(i)]['Attack']), 1, (255, 255, 255))
            if len(str(board['enemy'+str(i)]['name']))>6:
                fenetre.blit(name, (160+(i*150),197))
            else:
                fenetre.blit(name, (175+(i*150),197))
            fenetre.blit(cost, (155+(i*150),154))
            fenetre.blit(health, (207+(i*150),227))
            fenetre.blit(attack, (155+(i*150),227))
    for i in range(0,3):
        if board['player'+str(i)] == 'empty':
            fenetre.blit(board_case_empty, (50 +(i*150),345))
        else:
            fenetre.blit(board_case_full, (50 +(i*150),345))
            model_card_front = pygame.image.load("images/card_model_hand.png").convert_alpha()
            temp_image = pygame.image.load("decks/img/"+str(board['player'+str(i)]['name'])+".png").convert()
            fenetre.blit(temp_image, (168+(i*150),350))
            fenetre.blit(model_card_front, (150+(i*150),350))  
            
            name = font_name.render(str(board['player'+str(i)]['name']), 1, (255, 255, 255))
            cost = font.render(str(board['player'+str(i)]['Cost']), 1, (255, 255, 255))
            health = font.render(str(board['player'+str(i)]['Health']), 1, (255, 255, 255))
            attack = font.render(str(board['player'+str(i)]['Attack']), 1, (255, 255, 255))
            if len(str(board['player'+str(i)]['name']))>6:
                fenetre.blit(name, (160+(i*150),397))
            else:
                fenetre.blit(name, (175+(i*150),397))
            fenetre.blit(cost, (155+(i*150),354))
            fenetre.blit(health, (207+(i*150),427))
            fenetre.blit(attack, (155+(i*150),427))
