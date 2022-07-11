
import numpy as np
import pygame
import math
import sys

#constant--
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
BG_COLOR=(28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
LINE_COLORX = (66, 66, 66)
CROSS_WIDTH = 25
SPACE = 55
WIN_LINE_WIDTH = 15

# Board
BOARD_ROWS = 3
BOARD_COLS = 3
player=1
Game_Over=False

pygame.init()
pygame.display.set_caption("TIC TAC TOE")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BG_COLOR)

# ---------
# Functions
# ---------
def draw_lines():
	pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), 10)
	pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), 10)
	pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), 10)
	pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), 10)

draw_lines()


def draw_figures():
  for row in range(BOARD_ROWS):
   for colm in range (BOARD_COLS):
       if board[row][colm]==1:
        pygame.draw.circle(screen,CIRCLE_COLOR,(int(colm*200+100),int(row*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
       elif  board[row][colm]==2:
        pygame.draw.line(screen,LINE_COLORX,(colm*200+SPACE,row*200+200-SPACE),(colm*200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
        pygame.draw.line(screen,LINE_COLORX,(colm*200+SPACE,row*200+SPACE),(colm*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)



def available_square(row, col):
   if board[row][col] == 0:
    return True
   else:
    return False 


def mark_square(row, col, player):
	board[row][col] = player



def is_Bord_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
          if board[row][col] ==0:
            return False
          else:
            return True 

def check_win(player):
	# vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * 200 + 200//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = LINE_COLORX

	pygame.draw.line( screen, color, (posX, 15), (posX, SCREEN_HEIGHT - 15), 15 )

def draw_horizontal_winning_line(row, player):
	posY = row * 200 + 200//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = LINE_COLORX

	pygame.draw.line( screen, color, (15, posY), (SCREEN_WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = LINE_COLORX

	pygame.draw.line( screen, color, (15, SCREEN_HEIGHT - 15), (SCREEN_WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = LINE_COLORX

	pygame.draw.line( screen, color, (15, 15), (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15), WIN_LINE_WIDTH )

def restar():
  pass

#--------------    
# Console board
# -------------
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# --------
# Update()
# --------
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN and not Game_Over: # to komnw if we click the screen
                MouseX=event.pos[0] #x
                MouseY= event.pos[1] #y

                clicked_row=int(MouseY//200)
                clicked_clon=int(MouseX//200)


                if available_square(clicked_row,clicked_clon):
                  if player ==1:
                     mark_square(clicked_row,clicked_clon,1)
                     if check_win(player):
                        Game_Over=True
                     player=2
                  elif player==2:
                     mark_square(clicked_row,clicked_clon,2)
                     if check_win(player):
                      Game_Over=True
                     player=1
                  draw_figures()
        pygame.display.update()        