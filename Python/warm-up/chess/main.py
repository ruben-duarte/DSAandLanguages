# two players chess game. made with pygame

import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 650
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess game for two players ! ✔♟' )
font = pygame.font.Font('freesansbold.ttf',20)
big_font = pygame.font.Font('freesansbold.ttf', 30)
timer = pygame.time.Clock()
fps = 60

#game variables and images
white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop","knight", "rook",
                           "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                              (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop","knight", "rook",
                           "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                              (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 whites turn no selection :1  whites turn piece selected, 2 black turn no selection, 3 black piece selected
turn_step = 0
selection = 100
valid_moves = []
#load images game piceces (queen, king, rook ,bishop, knight, pawn) x 2
black_queen  = pygame.image.load('images/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (40,100))
black_queen_small = pygame.transform.scale(black_queen, (45,65))
black_rook = pygame.image.load('images/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (40,100))
black_rook_small = pygame.transform.scale(black_rook, (45,65))
black_knight = pygame.image.load('images/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (40,100))
black_knight_small = pygame.transform.scale(black_knight, (45,65))
black_bishop = pygame.image.load('images/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (40,100))
black_bishop_small = pygame.transform.scale(black_bishop, (45,65))
black_king = pygame.image.load('images/black_king.png')
black_king = pygame.transform.scale(black_king, (40,100))
black_king_small = pygame.transform.scale(black_king, (45,65))
black_pawn = pygame.image.load('images/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (40,100))
black_pawn_small = pygame.transform.scale(black_pawn, (30,90))

white_rook = pygame.image.load('images/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (40,100))
white_rook_small = pygame.transform.scale(white_rook, (45,65))
white_knight = pygame.image.load('images/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (40,100))
white_knight_small = pygame.transform.scale(white_knight, (45,65))
white_bishop = pygame.image.load('images/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (40,100))
white_bishop_small = pygame.transform.scale(white_bishop, (45,65))
white_king = pygame.image.load('images/white_king.png')
white_king = pygame.transform.scale(white_king, (40,100))
white_king_small = pygame.transform.scale(white_king, (45,65))
white_queen = pygame.image.load('images/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (40,100))
white_queen_small = pygame.transform.scale(white_queen, (45,65))
white_pawn = pygame.image.load('images/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (40,100))
white_pawn_small = pygame.transform.scale(white_pawn, (30,90))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#draw chess board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray',[420 - (column*140), row*70, 70,70])
        else:
            pygame.draw.rect(screen, 'light gray',[490 - (column*140), row*70, 70, 70])
        pygame.draw.rect(screen, 'gray', [0, 560, WIDTH, 100])
        pygame.draw.rect(screen, '#005e7c', [0, 560, WIDTH, 100], 5)
        pygame.draw.rect(screen, '#005e7c', [560, 0, 440, HEIGHT], 5)
        status_text = ["white: select a piece to move ", "white: select a destination",
                               "black: select a piece to move ", "black: select a destination "]
        screen.blit(big_font.render(status_text[turn_step], True, "black" ), (20, 600))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0,70*i), (560,70*i),2)
            pygame.draw.line(screen, 'black', (70*i,0), (70*i,560),2)

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0]*70 + 18, white_locations[i][1]*70 - 20))
        else:    
            screen.blit(white_images[index], (white_locations[i][0]*70 +14, white_locations[i][1]*70 - 20))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, "#fb8500", [white_locations[i][0]*70 + 1, white_locations[i][1]*70+1, 70, 70], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0]*70 + 18, black_locations[i][1]*70 - 22))
        else:    
            screen.blit(black_images[index], (black_locations[i][0]*70 +18 , black_locations[i][1]*70 - 20))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, "#023047", [black_locations[i][0]*70 + 1, black_locations[i][1]*70+1, 100, 100], 2)

#check all valid options on board
def check_options():
    pass

run = True
while run:
    timer.tick(fps)
    screen.fill('#427aa1')
    draw_board()
    draw_pieces()

#event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 70
            y_coord = event.pos[1] // 70
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] =click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece]) 
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] =click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece]) 
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

    pygame.display.flip()
pygame.quit()


        

