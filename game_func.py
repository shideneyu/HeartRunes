import pygame
from pygame.locals import *

def start_game(fenetre,game):
	pygame.display.set_caption("Titre")

	#initiliase une fenetre redimmensionnable avec une largeur et une hauteur
	fenetre = pygame.display.set_mode((800, 650),RESIZABLE)
	#permet de charger une image de fond qui prend la taille de la fenetre
	fond = pygame.image.load("background.jpg").convert()
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
		fenetre.blit(card, (00,550))
		fenetre.blit(card2, (100,350))
		fenetre.blit(card3, (200,350))
		fenetre.blit(card4, (300,350))
		fenetre.blit(card5, (300,150))
		fenetre.blit(card6, (200,150))
		fenetre.blit(card7, (100,150))
		fenetre.blit(bar, (0,480))
		fenetre.blit(bar, (0,100))
		#fenetre.blit(health_bar, (500,30))
		#fenetre.blit(health_bar2, (490,500))
		#fenetre.blit(mana_bar, (500,75))
		#fenetre.blit(mana_bar2, (490,540))
		game.showScores(fenetre)
		pygame.display.flip()


def generate_element(fenetre):
	ump = pygame.image.load("images/ump.jpg").convert()
	fn = pygame.image.load("images/fn.jpg").convert()
	ps = pygame.image.load("images/ps.jpg").convert()
	pc = pygame.image.load("images/pc.png").convert()
	fenetre.blit(ump, (100,100))
	fenetre.blit(fn, (400,100))
	fenetre.blit(ps, (100,350))
	fenetre.blit(pc, (400,350))
	yellow = (255, 255, 0)
	white = (255,255,255)
	myfont = pygame.font.SysFont("Comic Sans MS", 30)
	label = myfont.render("choisir un parti", 1, yellow)
	fenetre.blit(label, (250,10))

def start_player(fenetre,game):
	turn_count = 0
	timer = 15
	history = ""

	yellow = (255, 255, 0)
	white = (255,255,255)
	myfont = pygame.font.SysFont("Comic Sans MS", 30)
	#game.setPlayers()
	#game.showScores()
	#game.startGame()
	pygame.display.set_caption("Titre")

	#initiliase une fenetre redimmensionnable avec une largeur et une hauteur
	fenetre = pygame.display.set_mode((800, 600),RESIZABLE)
	#permet de charger une image de fond qui prend la taille de la fenetre
	fond = pygame.image.load("background.jpg").convert()
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
						start_game(fenetre,game)
