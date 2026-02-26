# # import pygame, chess
# # from random import choice
# # from traceback import format_exc
# # from sys import stderr
# # from time import strftime
# # from copy import deepcopy
# # import speech_recognition as sr
# # from gtts import gTTS
# # from playsound import playsound
# # import os

# # pygame.init()

# # SQUARE_SIDE = 80
# # AI_SEARCH_DEPTH = 2

# # RED_CHECK = (240, 150, 150)
# # WHITE = (255, 255, 255)
# # BLUE_LIGHT = (140, 184, 219)
# # BLUE_DARK = (91, 131, 159)
# # GRAY_LIGHT = (240, 240, 240)
# # GRAY_DARK = (200, 200, 200)
# # CHESSWEBSITE_LIGHT = (212, 202, 190)
# # CHESSWEBSITE_DARK = (100, 92, 89)
# # LICHESS_LIGHT = (240, 217, 181)
# # LICHESS_DARK = (181, 136, 99)
# # LICHESS_GRAY_LIGHT = (164, 164, 164)
# # LICHESS_GRAY_DARK = (136, 136, 136)

# # BOARD_COLORS = [(GRAY_LIGHT, GRAY_DARK),
# #                 (BLUE_LIGHT, BLUE_DARK),
# #                 (WHITE, BLUE_LIGHT),
# #                 (CHESSWEBSITE_LIGHT, CHESSWEBSITE_DARK),
# #                 (LICHESS_LIGHT, LICHESS_DARK),
# #                 (LICHESS_GRAY_LIGHT, LICHESS_GRAY_DARK)]
# # BOARD_COLOR = choice(BOARD_COLORS)

# # BLACK_KING = pygame.image.load('images/black_king.png')
# # BLACK_QUEEN = pygame.image.load('images/black_queen.png')
# # BLACK_ROOK = pygame.image.load('images/black_rook.png')
# # BLACK_BISHOP = pygame.image.load('images/black_bishop.png')
# # BLACK_KNIGHT = pygame.image.load('images/black_knight.png')
# # BLACK_PAWN = pygame.image.load('images/black_pawn.png')
# # BLACK_JOKER = pygame.image.load('images/black_joker.png')

# # WHITE_KING = pygame.image.load('images/white_king.png')
# # WHITE_QUEEN = pygame.image.load('images/white_queen.png')
# # WHITE_ROOK = pygame.image.load('images/white_rook.png')
# # WHITE_BISHOP = pygame.image.load('images/white_bishop.png')
# # WHITE_KNIGHT = pygame.image.load('images/white_knight.png')
# # WHITE_PAWN = pygame.image.load('images/white_pawn.png')
# # WHITE_JOKER = pygame.image.load('images/white_joker.png')
# # ONE = pygame.image.load('images/one.png')
# # TWO = pygame.image.load('images/two.png')
# # THREE = pygame.image.load('images/three.png')
# # FOUR = pygame.image.load('images/four.jpg')
# # FIVE = pygame.image.load('images/five.jpg')
# # SIX = pygame.image.load('images/six.jpg')
# # SEVEN = pygame.image.load('images/seven.jpg')
# # EIGHT = pygame.image.load('images/eight.jpg')
# # a = pygame.image.load('images/a.jpg')
# # b = pygame.image.load('images/b.jpg')
# # c = pygame.image.load('images/c.jpg')
# # d = pygame.image.load('images/d.jpg')
# # e = pygame.image.load('images/e.jpg')
# # f = pygame.image.load('images/f.jpg')
# # g = pygame.image.load('images/g.jpg')
# # h = pygame.image.load('images/h.jpg')

# # CLOCK = pygame.time.Clock()
# # CLOCK_TICK = 15

# # SCREEN = pygame.display.set_mode((int(8.5 * SQUARE_SIDE), int(8.5 * SQUARE_SIDE)), pygame.RESIZABLE)
# # SCREEN_TITLE = 'Chess Game'

# # pygame.display.set_icon(pygame.image.load('images/chess_icon.ico'))
# # pygame.display.set_caption(SCREEN_TITLE)


# # def resize_screen(square_side_len):
# #     global SQUARE_SIDE
# #     global SCREEN
# #     SCREEN = pygame.display.set_mode((8 * square_side_len, 8 * square_side_len), pygame.RESIZABLE)
# #     SQUARE_SIDE = square_side_len


# # def print_empty_board():
# #     SCREEN.fill(BOARD_COLOR[0])
# #     paint_dark_squares(BOARD_COLOR[1])


# # def paint_square(square, square_color):
# #     col = chess.FILES.index(square[0])
# #     row = 7 - chess.RANKS.index(square[1])
# #     pygame.draw.rect(SCREEN, square_color, (SQUARE_SIDE * col, SQUARE_SIDE * row, SQUARE_SIDE, SQUARE_SIDE), 0)


# # def paint_dark_squares(square_color):
# #     for position in chess.single_gen(chess.DARK_SQUARES):
# #         paint_square(chess.bb2str(position), square_color)


# # def get_square_rect(square):
# #     col = chess.FILES.index(square[0])
# #     row = 7 - chess.RANKS.index(square[1])
# #     return pygame.Rect((col * SQUARE_SIDE, row * SQUARE_SIDE), (SQUARE_SIDE, SQUARE_SIDE))


# # def coord2str(position, color=chess.WHITE):
# #     # print(position[0],position[1])
# #     if color == chess.WHITE:
# #         file_index = int(position[0] / SQUARE_SIDE)
# #         rank_index = 7 - int(position[1] / SQUARE_SIDE)
# #         return chess.FILES[file_index] + chess.RANKS[rank_index]
# #     if color == chess.BLACK:
# #         file_index = 7 - int(position[0] / SQUARE_SIDE)
# #         rank_index = int(position[1] / SQUARE_SIDE)
# #         return chess.FILES[file_index] + chess.RANKS[rank_index]


# # def print_board(board, color=chess.WHITE):
# #     if color == chess.WHITE:
# #         printed_board = board
# #     if color == chess.BLACK:
# #         printed_board = chess.rotate_board(board)
# #     SQUARE_SIDE1 = int(SQUARE_SIDE / 2)
# #     print_empty_board()
# #     SCREEN.blit(pygame.transform.scale(ONE, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(0.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(TWO, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(1.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(THREE, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(2.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(FOUR, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(3.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(FIVE, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(4.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(SIX, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(5.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(SEVEN, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(6.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(EIGHT, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((8 * SQUARE_SIDE, int(7.25 * SQUARE_SIDE)), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(a, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(0.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(b, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(1.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(c, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(2.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(d, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(3.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(e, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(4.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(f, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(5.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(g, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(6.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))
# #     SCREEN.blit(pygame.transform.scale(h, (SQUARE_SIDE1, SQUARE_SIDE1)),
# #                 pygame.Rect((int(7.25 * SQUARE_SIDE), 8 * SQUARE_SIDE), (SQUARE_SIDE1, SQUARE_SIDE1)))

# #     if chess.is_check(board, chess.WHITE):
# #         paint_square(chess.bb2str(chess.get_king(printed_board, chess.WHITE)), RED_CHECK)
# #     if chess.is_check(board, chess.BLACK):
# #         paint_square(chess.bb2str(chess.get_king(printed_board, chess.BLACK)), RED_CHECK)

# #     for position in chess.colored_piece_gen(printed_board, chess.KING, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_KING, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.QUEEN, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_QUEEN, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.ROOK, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_ROOK, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.BISHOP, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_BISHOP, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.KNIGHT, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_KNIGHT, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.PAWN, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.JOKER, chess.BLACK):
# #         SCREEN.blit(pygame.transform.scale(BLACK_JOKER, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))

# #     for position in chess.colored_piece_gen(printed_board, chess.KING, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_KING, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.QUEEN, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_QUEEN, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.ROOK, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_ROOK, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.BISHOP, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_BISHOP, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.KNIGHT, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_KNIGHT, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.PAWN, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))
# #     for position in chess.colored_piece_gen(printed_board, chess.JOKER, chess.WHITE):
# #         SCREEN.blit(pygame.transform.scale(WHITE_JOKER, (SQUARE_SIDE, SQUARE_SIDE)),
# #                     get_square_rect(chess.bb2str(position)))

# #     pygame.display.flip()


# # def set_title(title):
# #     pygame.display.set_caption(title)
# #     pygame.display.flip()


# # def make_AI_move(game, color):
# #     set_title(SCREEN_TITLE + ' - Calculating move...')
# #     new_game = chess.make_move(game, chess.get_AI_move(game, AI_SEARCH_DEPTH))
# #     set_title(SCREEN_TITLE)
# #     print_board(new_game.board, color)
# #     return new_game


# # def try_move(game, attempted_move):
# #     for move in chess.legal_moves(game, game.to_move):
# #         if move == attempted_move:
# #             game = chess.make_move(game, move)
# #     return game


# # def play_as(game, color):
# #     run = True
# #     ongoing = True
# #     joker = 0

# #     try:
# #         while run:
# #             CLOCK.tick(CLOCK_TICK)
# #             print_board(game.board, color)

# #             if chess.game_ended(game):
# #                 set_title(SCREEN_TITLE + ' - ' + chess.get_outcome(game))
# #                 ongoing = False

# #             if ongoing and game.to_move == chess.opposing_color(color):
# #                 game = make_AI_move(game, color)

# #             if chess.game_ended(game):
# #                 set_title(SCREEN_TITLE + ' - ' + chess.get_outcome(game))
# #                 ongoing = False

# #             for event in pygame.event.get():
# #                 if event.type == pygame.QUIT:
# #                     run = False
# #                 myText1 = "make your move"
# #                 if event.type == pygame.MOUSEBUTTONDOWN:

# #                     r = sr.Recognizer()
# #                     print("Please Talk")
# #                     language = 'en'

# #                     output = gTTS(text=myText1, lang=language, slow=False)

# #                     output.save("Output.mp3")
# #                     playsound("Output.mp3")
# #                     os.remove("Output.mp3")
# #                     with sr.Microphone() as source:
# #                         try:
# #                             audio_data = r.record(source, duration=5)
# #                             print("Recognising...")
# #                             text = r.recognize_google(audio_data)
# #                             text = text.replace(" ", "")
# #                             print(text)
# #                         except sr.UnknownValueError:
# #                             language = 'en'
# #                             output = gTTS(text="I didn't get that. Say again", lang=language, slow=False)
# #                             output.save("Output.mp3")
# #                             playsound("Output.mp3")
# #                             os.remove("Output.mp3")
# #                             print("I didn't get that. Say again")
# #                             continue
# #                     l = ['1', '2', '3', '4', '5', '6', '7', '8']
# #                     k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# #                     flag = True
# #                     if len(text)!=4:
# #                         flag = False

# #                     if text[1] not in l:
# #                         flag = False
# #                     if text[-1] not in l:
# #                         flag = False

# #                     text = text.replace("A", "1")
# #                     text = text.replace("a", "1")
# #                     text = text.replace("B", "2")
# #                     text = text.replace("b", "2")
# #                     text = text.replace("C", "3")
# #                     text = text.replace("c", "3")
# #                     text = text.replace("D", "4")
# #                     text = text.replace("d", "4")
# #                     text = text.replace("E", "5")
# #                     text = text.replace("e", "5")
# #                     text = text.replace("F", "6")
# #                     text = text.replace("f", "6")
# #                     text = text.replace("G", "7")
# #                     text = text.replace("g", "7")
# #                     text = text.replace("H", "8")
# #                     text = text.replace("h", "8")


# #                     if flag:
# #                         leaving_square = coord2str(((int(text[0]) - 1) * SQUARE_SIDE, (int(text[1]) - 1) * SQUARE_SIDE),color)
# #                         arriving_square = coord2str(((int(text[-2]) - 1) * SQUARE_SIDE, (int(text[-1]) - 1) * SQUARE_SIDE), color)

# #                     myText = "Please make a valid move"
# #                     if ongoing and game.to_move == color:
# #                         if flag == True and len(text) == 4:
# #                             move = (chess.str2bb(leaving_square), chess.str2bb(arriving_square))
# #                             if move not in chess.legal_moves(game, game.to_move):
# #                                 language = 'en'
# #                                 output = gTTS(text=myText, lang=language, slow=False)
# #                                 output.save("Output.mp3")
# #                                 playsound("Output.mp3")
# #                                 os.remove("Output.mp3")
# #                                 print("Please make a valid move")
# #                             else:
# #                                 game = try_move(game, move)
# #                                 print_board(game.board, color)


# #                         else:
# #                             language = 'en'
# #                             output = gTTS(text=myText, lang=language, slow=False)
# #                             output.save("Output.mp3")
# #                             playsound("Output.mp3")
# #                             os.remove("Output.mp3")
# #                             # print_board(game.board, color)
# #                             print("Please make a valid move")

# #                 if event.type == pygame.KEYDOWN:
# #                     if event.key == pygame.K_ESCAPE or event.key == 113:
# #                         run = False
# #                     if event.key == 104 and ongoing:  # H key
# #                         game = make_AI_move(game, color)
# #                     if event.key == 117:  # U key
# #                         game = chess.unmake_move(game)
# #                         game = chess.unmake_move(game)
# #                         set_title(SCREEN_TITLE)
# #                         print_board(game.board, color)
# #                         ongoing = True
# #                     if event.key == 99:  # C key
# #                         global BOARD_COLOR
# #                         new_colors = deepcopy(BOARD_COLORS)
# #                         new_colors.remove(BOARD_COLOR)
# #                         BOARD_COLOR = choice(new_colors)
# #                         print_board(game.board, color)
# #                     if event.key == 114:
# #                         os.system("start Rulebook.pdf")

# #                     if event.key == 112 or event.key == 100:  # P or D key
# #                         print(game.get_move_list() + '\n')
# #                         print('\n'.join(game.position_history))
# #                     if event.key == 101:  # E key
# #                         print('eval = ' + str(chess.evaluate_game(game) / 100))
# #                     if event.key == 106:  # J key
# #                         joker += 1
# #                         if joker == 13 and chess.get_queen(game.board, color):
# #                             queen_index = chess.bb2index(chess.get_queen(game.board, color))
# #                             game.board[queen_index] = color | chess.JOKER
# #                             print_board(game.board, color)

# #                 if event.type == pygame.VIDEORESIZE:
# #                     if SCREEN.get_height() != event.h:
# #                         resize_screen(int(event.h / 8.0))
# #                     elif SCREEN.get_width() != event.w:
# #                         resize_screen(int(event.w / 8.0))
# #                     print_board(game.board, color)
# #     except:
# #         print(format_exc(), file=stderr)
# #         bug_file = open('bug_report.txt', 'a')
# #         bug_file.write('----- ' + strftime('%x %X') + ' -----\n')
# #         bug_file.write(format_exc())
# #         bug_file.write('\nPlaying as WHITE:\n\t' if color == chess.WHITE else '\nPlaying as BLACK:\n\t')
# #         bug_file.write(game.get_move_list() + '\n\t')
# #         bug_file.write('\n\t'.join(game.position_history))
# #         bug_file.write('\n-----------------------------\n\n')
# #         bug_file.close()


# # def play_as_white(game=chess.Game()):
# #     return play_as(game, chess.WHITE)


# # def play_as_black(game=chess.Game()):
# #     return play_as(game, chess.BLACK)


# # def play_random_color(game=chess.Game()):
# #     color = choice([chess.WHITE, chess.BLACK])
# #     play_as(game, color)


# # # chess.verbose = True
# # play_random_color()











# # gui.py - Full voice-controlled chess GUI (fixed)
# # Requirements:
# #   pip install pygame SpeechRecognition gTTS python-chess
# #
# # Author: ChatGPT (fixed & tuned)
# # Date: 2025-08-13 (updated)

# import os
# import sys
# import time
# import random
# import re
# import tempfile
# import pygame
# import speech_recognition as sr
# from gtts import gTTS
# from dataclasses import dataclass
# from typing import Optional, Tuple, List
# import chess

# # --------------------------
# # USER CONFIG (edit if needed)
# # --------------------------
# MIC_INDEX = None           # None = auto-select a likely microphone; otherwise set to an int you verified
# LISTEN_TIMEOUT = 7         # seconds to wait for speech to start (reduced)
# PHRASE_TIME_LIMIT = 6      # seconds max phrase
# AMBIENT_NOISE_DURATION = 0.5  # shorter calibration for speed
# MAX_VOICE_RETRIES = 3
# ENABLE_KEYBOARD_FALLBACK = True
# AI_THINK_DELAY = 0.45      # shorter AI delay for snappier play

# # GUI sizing
# BOARD_SIZE = 8
# BASE_SQUARE = 88
# MIN_SQUARE = 40

# # Colors / style
# BG_LIGHT = (240, 217, 181)
# BG_DARK  = (181, 136, 99)
# BG_SIDE  = (28, 32, 38)
# TEXT_COL = (230, 232, 235)
# HIGHLIGHT_MOVE = (120, 200, 120)
# HIGHLIGHT_CHECK = (220, 120, 120)

# # --------------------------
# # INITIALIZE PYGAME & FONTS
# # --------------------------
# pygame.init()
# pygame.display.set_caption("Voice-Controlled Chess")
# clock = pygame.time.Clock()

# def choose_font(size):
#     for name in ["Segoe UI Symbol", "DejaVu Sans", "Arial Unicode MS", None]:
#         try:
#             return pygame.font.SysFont(name, size)
#         except Exception:
#             continue
#     return pygame.font.Font(None, size)

# font_piece = choose_font(int(BASE_SQUARE * 0.72))
# font_side  = choose_font(18)
# font_big   = choose_font(24)

# # Unicode piece glyphs
# PIECE_GLYPHS = {
#     chess.PAWN:   ("♙", "♟"),
#     chess.KNIGHT: ("♘", "♞"),
#     chess.BISHOP: ("♗", "♝"),
#     chess.ROOK:   ("♖", "♜"),
#     chess.QUEEN:  ("♕", "♛"),
#     chess.KING:   ("♔", "♚"),
# }

# # --------------------------
# # SPEECH-RECOGNITION SETUP
# # --------------------------
# recognizer = sr.Recognizer()
# recognizer.calibrated = False

# def list_microphones():
#     try:
#         names = sr.Microphone.list_microphone_names()
#         print("Available microphones:")
#         for i, n in enumerate(names):
#             print(f"  {i}: {n}")
#         return names
#     except Exception as e:
#         print("[Mic] Could not list microphones:", e)
#         return []

# def calibrate_once(mic_index: Optional[int]):
#     """
#     Calibrate ambient noise once; afterwards sets a fixed energy threshold.
#     """
#     try:
#         with sr.Microphone(device_index=mic_index, sample_rate=16000, chunk_size=1024) as src:
#             print("[Voice] Calibrating ambient noise for", AMBIENT_NOISE_DURATION, "seconds...")
#             recognizer.dynamic_energy_threshold = True
#             recognizer.adjust_for_ambient_noise(src, duration=AMBIENT_NOISE_DURATION)
#             suggested = max(120, int(recognizer.energy_threshold * 0.6)) if recognizer.energy_threshold else 250
#             recognizer.dynamic_energy_threshold = False
#             recognizer.energy_threshold = suggested
#             recognizer.calibrated = True
#             print(f"[Voice] Calibration complete. energy_threshold={recognizer.energy_threshold}")
#             return True
#     except Exception as e:
#         print("[Voice] Calibration failed:", e)
#         # fallback defaults
#         recognizer.dynamic_energy_threshold = False
#         recognizer.energy_threshold = 300
#         recognizer.calibrated = True
#         return False

# def listen_once(mic_index: Optional[int]) -> Optional[str]:
#     """
#     Listen for a single utterance and return recognized text (or None).
#     """
#     try:
#         with sr.Microphone(device_index=mic_index, sample_rate=16000, chunk_size=1024) as source:
#             if not getattr(recognizer, "calibrated", False):
#                 calibrate_once(mic_index)
#             print("[Voice] Please speak now...")
#             audio = recognizer.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=PHRASE_TIME_LIMIT)
#         print("[Voice] Recognizing...")
#         try:
#             text = recognizer.recognize_google(audio)
#             print("[Voice] Raw:", text)
#             return text
#         except sr.UnknownValueError:
#             print("[Voice] Could not understand audio.")
#             return None
#         except sr.RequestError as e:
#             print("[Voice] Recognition service error:", e)
#             return None
#     except sr.WaitTimeoutError:
#         print("[Voice] No speech detected (timeout).")
#         return None
#     except Exception as e:
#         print("[Voice] Microphone/listen error:", e)
#         return None

# # --------------------------
# # TTS using gTTS + pygame.mixer (safe temp file)
# # --------------------------
# def speak(text: str, block=True):
#     """
#     Synthesize text -> save to temp mp3 -> play via pygame.mixer -> delete file.
#     block=True waits until playback completes.
#     """
#     try:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
#             tmpname = tf.name
#         tts = gTTS(text=text, lang="en")
#         tts.save(tmpname)
#         try:
#             if not pygame.mixer.get_init():
#                 pygame.mixer.init()
#         except Exception as e:
#             print("[TTS] mixer init:", e)
#         try:
#             pygame.mixer.music.load(tmpname)
#             pygame.mixer.music.play()
#             if block:
#                 while pygame.mixer.music.get_busy():
#                     for ev in pygame.event.get():
#                         if ev.type == pygame.QUIT:
#                             pygame.mixer.music.stop()
#                             raise KeyboardInterrupt
#                     pygame.time.wait(20)
#             pygame.mixer.music.stop()
#             try:
#                 pygame.mixer.music.unload()
#             except Exception:
#                 pass
#         except Exception as e:
#             print("[TTS] Playback error:", e)
#         finally:
#             try:
#                 os.remove(tmpname)
#             except Exception as e:
#                 print("[TTS] Could not remove tmp file:", e)
#     except KeyboardInterrupt:
#         raise
#     except Exception as e:
#         print("[TTS] Error:", e)

# # --------------------------
# # Speech normalization → move parser
# # --------------------------
# _NUM_WORDS = {
#     "one": "1", "two": "2", "three": "3", "four": "4", "for": "4",
#     "five": "5", "six": "6", "seven": "7", "eight": "8", "ate": "8",
# }
# _FILE_WORDS = {
#     "alpha":"a","a":"a","bravo":"b","b":"b","charlie":"c","c":"c","delta":"d","d":"d",
#     "echo":"e","e":"e","foxtrot":"f","f":"f","golf":"g","g":"g","hotel":"h","h":"h"
# }
# _PIECE_WORDS = {"pawn":"P","knight":"N","night":"N","bishop":"B","rook":"R","queen":"Q","king":"K"}

# def normalize_spoken_text(text: str) -> Optional[str]:
#     """
#     Convert recognized speech into:
#       - UCI-style 'e2e4'
#       - SAN-like 'Nf3', 'e4'
#       - O-O or O-O-O for castling
#     """
#     if not text:
#         return None
#     t = text.lower().strip()
#     t = t.replace('-', ' ').replace(' to ', ' ').replace('–',' ')
#     t = re.sub(r'\s+', ' ', t).strip()

#     # castle variants
#     if "castle long" in t or "queen side" in t or t.count("o") >= 3 or t.count("zero") >= 3:
#         return "O-O-O"
#     if "castle" in t or "king side" in t or t in ("o o","o-o","oo","0 0"):
#         return "O-O"

#     # tokenize
#     tokens = re.findall(r"[A-Za-z]+|\d+", t)
#     norm = []
#     for tok in tokens:
#         if tok in _FILE_WORDS:
#             norm.append(_FILE_WORDS[tok])
#         elif tok in _NUM_WORDS:
#             norm.append(_NUM_WORDS[tok])
#         elif len(tok) == 1 and tok in "abcdefgh":
#             norm.append(tok)
#         elif tok.isdigit() and tok in "12345678":
#             norm.append(tok)
#         elif tok in _PIECE_WORDS:
#             norm.append(_PIECE_WORDS[tok])
#         else:
#             if tok and tok[0] in "abcdefgh":
#                 norm.append(tok[0])
#             else:
#                 norm.append(tok)

#     # try to extract two squares in sequence
#     squares = []
#     i = 0
#     while i < len(norm):
#         if i + 1 < len(norm) and norm[i] in list("abcdefgh") and norm[i+1] in list("12345678"):
#             squares.append(norm[i] + norm[i+1])
#             i += 2
#         else:
#             i += 1
#     if len(squares) >= 2:
#         return squares[0] + squares[1]  # uci-like e2e4

#     # piece + square (N f3)
#     for idx, tok in enumerate(norm):
#         if tok in ("P","N","B","R","Q","K"):
#             if idx + 2 < len(norm) and norm[idx+1] in list("abcdefgh") and norm[idx+2] in list("12345678"):
#                 return tok + norm[idx+1] + norm[idx+2]  # Nf3
#             if idx + 1 < len(norm) and re.fullmatch(r"[a-h][1-8]", "".join(norm[idx+1:idx+3])):
#                 return tok + "".join(norm[idx+1:idx+3])

#     # try compact original (remove spaces)
#     compact = re.sub(r'\s+','',t)
#     if re.fullmatch(r'[a-h][1-8][a-h][1-8][qrbn]?', compact):
#         return compact

#     # single square (pawn move or SAN)
#     for i in range(len(norm)-1):
#         if norm[i] in list("abcdefgh") and norm[i+1] in list("12345678"):
#             return norm[i] + norm[i+1]

#     return None

# def spell_for_feedback(move_text: str) -> str:
#     s = move_text.upper()
#     if s in ("O-O","0-0"):
#         return "castle"
#     if s in ("O-O-O","0-0-0"):
#         return "castle long"
#     return " ".join(list(s))

# # --------------------------
# # Chess GUI helpers
# # --------------------------
# @dataclass
# class DrawState:
#     w: int
#     h: int
#     square: int
#     margin: int

# def compute_draw_state(screen_size: Tuple[int,int]) -> DrawState:
#     w,h = screen_size
#     margin = max(int(w * 0.12), 220)
#     board_pixels = min(h, w - margin)
#     square = max(MIN_SQUARE, board_pixels // 8)
#     return DrawState(w=w, h=h, square=square, margin=w - board_pixels)

# def board_to_rect(ds: DrawState, file: int, rank: int) -> pygame.Rect:
#     x = file * ds.square
#     y = (7 - rank) * ds.square
#     return pygame.Rect(x, y, ds.square, ds.square)

# def draw_board(screen: pygame.Surface, board: chess.Board, last_move: Optional[chess.Move], ds: DrawState):
#     for r in range(8):
#         for f in range(8):
#             rect = board_to_rect(ds, f, r)
#             color = BG_LIGHT if (f + r) % 2 == 0 else BG_DARK
#             pygame.draw.rect(screen, color, rect)
#     if last_move:
#         for sq in (last_move.from_square, last_move.to_square):
#             f = chess.square_file(sq); r = chess.square_rank(sq)
#             rect = board_to_rect(ds, f, r)
#             s = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
#             s.fill((*HIGHLIGHT_MOVE, 90))
#             screen.blit(s, rect.topleft)
#     if board.is_check():
#         king_sq = board.king(board.turn)
#         if king_sq is not None:
#             f = chess.square_file(king_sq); r = chess.square_rank(king_sq)
#             rect = board_to_rect(ds, f, r)
#             s = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
#             s.fill((*HIGHLIGHT_CHECK, 110))
#             screen.blit(s, rect.topleft)

# def draw_pieces(screen: pygame.Surface, board: chess.Board, ds: DrawState):
#     for sq in chess.SQUARES:
#         piece = board.piece_at(sq)
#         if not piece:
#             continue
#         f = chess.square_file(sq); r = chess.square_rank(sq)
#         rect = board_to_rect(ds, f, r)
#         glyph = PIECE_GLYPHS[piece.piece_type][0 if piece.color == chess.WHITE else 1]
#         surf = font_piece.render(glyph, True, (30,30,30))
#         tw,th = surf.get_size()
#         screen.blit(surf, (rect.x + (rect.w - tw)//2, rect.y + (rect.h - th)//2))

# def draw_sidebar(screen: pygame.Surface, ds: DrawState, board: chess.Board, info: List[str]):
#     x0 = ds.square * 8
#     pygame.draw.rect(screen, BG_SIDE, (x0, 0, ds.margin, ds.h))
#     title = font_big.render("Voice Chess", True, TEXT_COL)
#     screen.blit(title, (x0 + 12, 10))
#     turn = "White" if board.turn == chess.WHITE else "Black"
#     screen.blit(font_side.render(f"Turn: {turn}", True, TEXT_COL), (x0 + 12, 48))
#     lines = [
#         "Speak moves like:",
#         "  E2 to E4   (or)  Echo two to Echo four",
#         "  Knight to F3",
#         "  pawn to e4",
#         "  castle / castle long",
#         "",
#         "Keyboard:",
#         "  T = type move, U = undo, R = AI move, Esc = quit",
#         "",
#         f"Mic index: {MIC_INDEX if MIC_INDEX is not None else 'auto'}",
#         "",
#         "Recent:"
#     ]
#     y = 120
#     for line in lines:
#         screen.blit(font_side.render(line, True, TEXT_COL), (x0 + 12, y))
#         y += 22
#     y += 6
#     for line in info[-10:]:
#         screen.blit(font_side.render(line, True, TEXT_COL), (x0 + 12, y))
#         y += 20

# # --------------------------
# # Move helpers & AI
# # --------------------------
# def uci_from_san_or_uci(txt: str, board: chess.Board) -> Optional[chess.Move]:
#     txt = txt.strip()
#     if re.fullmatch(r"[a-h][1-8][a-h][1-8][qrbn]?", txt.lower()):
#         try:
#             mv = chess.Move.from_uci(txt.lower())
#             if mv in board.legal_moves:
#                 return mv
#         except Exception:
#             return None
#         return None
#     try:
#         mv = board.parse_san(txt)
#         if mv in board.legal_moves:
#             return mv
#     except Exception:
#         return None
#     return None

# def infer_from_piece_to_square(san_like: str, board: chess.Board) -> Optional[chess.Move]:
#     try:
#         mv = board.parse_san(san_like)
#         if mv in board.legal_moves:
#             return mv
#     except Exception:
#         return None
#     return None

# def random_ai_move(board: chess.Board) -> Optional[chess.Move]:
#     moves = list(board.legal_moves)
#     return random.choice(moves) if moves else None

# def say_san_for_tts(san: str) -> str:
#     s = san.replace("+", " check").replace("#", " checkmate")
#     if s in ("O-O","0-0"):
#         return "castle"
#     if s in ("O-O-O","0-0-0"):
#         return "castle long"
#     s = s.replace("K","King ").replace("Q","Queen ").replace("R","Rook ").replace("B","Bishop ").replace("N","Knight ")
#     s = s.replace("x"," takes ")
#     s = re.sub(r"([a-h])([1-8])", lambda m: f"{m.group(1).upper()} { {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight'}[m.group(2)] }", s)
#     return s

# # --------------------------
# # Typing prompt overlay
# # --------------------------
# def prompt_type_move(screen: pygame.Surface, ds: DrawState) -> Optional[str]:
#     buffer = ""
#     while True:
#         for ev in pygame.event.get():
#             if ev.type == pygame.QUIT:
#                 return None
#             if ev.type == pygame.KEYDOWN:
#                 if ev.key == pygame.K_RETURN:
#                     return buffer.strip()
#                 if ev.key == pygame.K_ESCAPE:
#                     return None
#                 if ev.key == pygame.K_BACKSPACE:
#                     buffer = buffer[:-1]
#                 else:
#                     ch = ev.unicode
#                     if ch and ch.isprintable():
#                         buffer += ch
#         overlay = pygame.Surface((ds.w, ds.h), pygame.SRCALPHA)
#         overlay.fill((0,0,0,180))
#         screen.blit(overlay, (0,0))
#         box = pygame.Rect(ds.w//2 - 260, ds.h//2 - 40, 520, 80)
#         pygame.draw.rect(screen, (34,39,46), box, border_radius=10)
#         label = font_big.render("Type move (e.g. e2e4 or Nf3). Enter to submit.", True, (230,230,230))
#         screen.blit(label, (box.x + 12, box.y + 8))
#         textsurf = font_big.render(buffer or " ", True, (240,240,240))
#         screen.blit(textsurf, (box.x + 12, box.y + 44))
#         pygame.display.flip()
#         clock.tick(30)

# # --------------------------
# # Main game loop
# # --------------------------
# def main():
#     init_w = BASE_SQUARE * 8 + 260
#     init_h = BASE_SQUARE * 8
#     screen = pygame.display.set_mode((init_w, init_h), pygame.RESIZABLE)
#     pygame.display.set_caption("Voice-Controlled Chess")

#     mic_names = list_microphones()
#     selected_mic = MIC_INDEX
#     if selected_mic is None:
#         # auto-select a likely mic (avoid Microsoft Sound Mapper index 0 if possible)
#         chosen = None
#         for i,name in enumerate(mic_names):
#             low = (name or "").lower()
#             if i == 0 and "microsoft sound mapper" in low:
#                 continue
#             if "microphone" in low or "headset" in low or "input" in low:
#                 chosen = i
#                 break
#         if chosen is None:
#             chosen = 1 if len(mic_names) > 1 else (0 if mic_names else None)
#         selected_mic = chosen
#     print(f"Selected MIC_INDEX = {selected_mic} ({mic_names[selected_mic] if mic_names and selected_mic is not None and selected_mic < len(mic_names) else 'unknown'})")

#     # one-time calibration
#     calibrate_once(selected_mic)

#     board = chess.Board()
#     last_move = None
#     info_lines: List[str] = []
#     info_lines.append("Say moves, or press T to type. Press Esc to quit.")
#     human_color = chess.WHITE

#     running = True
#     while running:
#         clock.tick(30)
#         ds = compute_draw_state(screen.get_size())
#         screen.fill((0,0,0))
#         draw_board(screen, board, last_move, ds)
#         draw_pieces(screen, board, ds)
#         draw_sidebar(screen, ds, board, info_lines)
#         pygame.display.flip()

#         if board.is_game_over():
#             res = board.result()
#             if board.is_checkmate():
#                 winner = "Black" if board.turn == chess.WHITE else "White"
#                 msg = f"Checkmate. {winner} wins."
#             elif board.is_stalemate():
#                 msg = "Draw by stalemate."
#             elif board.is_insufficient_material():
#                 msg = "Draw by insufficient material."
#             elif board.can_claim_threefold_repetition():
#                 msg = "Draw by repetition."
#             else:
#                 msg = f"Game over: {res}."
#             info_lines.append(msg)
#             # no voice intro; but we can announce game over
#             speak(msg + " Press Escape to exit.", block=False)
#             while True:
#                 for ev in pygame.event.get():
#                     if ev.type == pygame.QUIT:
#                         running = False; break
#                     if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
#                         running = False; break
#                 if not running:
#                     break
#                 clock.tick(30)
#             continue

#         # Player turn
#         if board.turn == human_color:
#             info_lines.append("Your turn — listening...")
#             heard = None
#             for attempt in range(1, MAX_VOICE_RETRIES+1):
#                 info_lines.append(f"[Voice] Attempt {attempt}/{MAX_VOICE_RETRIES}")
#                 pygame.display.flip()
#                 raw = listen_once(selected_mic)
#                 if raw:
#                     norm = normalize_spoken_text(raw)
#                     if norm:
#                         heard = norm
#                         # confirm briefly (non-blocking)
#                         try:
#                             speak(f"I heard {spell_for_feedback(heard)}", block=False)
#                         except Exception:
#                             pass
#                         break
#                     else:
#                         speak("I heard you, but couldn't parse a move. Please try again.", block=False)
#                 else:
#                     speak("I didn't catch that. Please speak again.", block=False)
#             if not heard and ENABLE_KEYBOARD_FALLBACK:
#                 speak("Voice failed. Press T to type your move.", block=False)
#                 info_lines.append("Voice failed — press T to type or continue speaking.")
#                 waiting = True
#                 start = time.time()
#                 while waiting and time.time() - start < 6:
#                     for ev in pygame.event.get():
#                         if ev.type == pygame.QUIT:
#                             running = False; waiting = False; break
#                         if ev.type == pygame.KEYDOWN:
#                             if ev.key == pygame.K_t:
#                                 typed = prompt_type_move(screen, ds)
#                                 if typed:
#                                     heard = typed
#                                 waiting = False; break
#                             if ev.key == pygame.K_u:
#                                 if board.move_stack:
#                                     board.pop()
#                                 if board.move_stack:
#                                     board.pop()
#                                 info_lines.append("Undid last full move.")
#                                 waiting = False; break
#                             if ev.key == pygame.K_r:
#                                 mv = random_ai_move(board)
#                                 if mv and mv in board.legal_moves:
#                                     san_ai = board.san(mv)  # compute SAN before push
#                                     board.push(mv)
#                                     last_move = mv
#                                     info_lines.append("AI (forced) moved " + san_ai)
#                                     speak("AI played " + say_san_for_tts(san_ai), block=False)
#                                 waiting = False; break
#                             if ev.key == pygame.K_ESCAPE:
#                                 running = False; waiting = False; break
#                     clock.tick(30)
#             if not heard:
#                 continue

#             # interpret heard into Move
#             mvobj = None
#             if re.fullmatch(r'[a-h][1-8][a-h][1-8][qrbn]?', heard):
#                 try:
#                     m = chess.Move.from_uci(heard)
#                     if m in board.legal_moves:
#                         mvobj = m
#                 except Exception:
#                     mvobj = None
#             else:
#                 # try SAN parse
#                 try:
#                     m = board.parse_san(heard)
#                     if m in board.legal_moves:
#                         mvobj = m
#                 except Exception:
#                     # maybe single destination like 'e4' - pick a legal move to that square
#                     if re.fullmatch(r'[a-h][1-8]', heard):
#                         candidates = [mv for mv in board.legal_moves if chess.square_name(mv.to_square) == heard]
#                         if len(candidates) == 1:
#                             mvobj = candidates[0]
#                         elif candidates:
#                             mvobj = candidates[0]  # best-effort
#             if not mvobj:
#                 info_lines.append("Unrecognized or illegal move: " + str(heard))
#                 speak("That move is illegal or could not be parsed. Please try again.", block=False)
#                 continue

#             # get SAN before push (safe)
#             try:
#                 san = board.san(mvobj)
#             except Exception:
#                 # fallback: if for some reason san fails, push only if legal
#                 if mvobj in board.legal_moves:
#                     board.push(mvobj)
#                     last_move = mvobj
#                     info_lines.append("You played (unknown SAN): " + str(mvobj))
#                     speak("You played a move", block=False)
#                 else:
#                     info_lines.append("Illegal move attempted.")
#                     speak("Illegal move, please try again.", block=False)
#                 continue

#             board.push(mvobj)
#             last_move = mvobj
#             info_lines.append("You played: " + san)
#             speak("You played " + say_san_for_tts(san), block=False)

#         # AI move (after player's move; if human already moved)
#         pygame.time.wait(int(AI_THINK_DELAY * 1000))
#         if not board.is_game_over():
#             ai_mv = random_ai_move(board)
#             if ai_mv and ai_mv in board.legal_moves:
#                 # compute SAN before pushing to avoid san() assert
#                 try:
#                     san_ai = board.san(ai_mv)
#                 except Exception:
#                     # if san fails for some reason, fallback to UCI string
#                     san_ai = ai_mv.uci()
#                 board.push(ai_mv)
#                 last_move = ai_mv
#                 info_lines.append("AI played: " + san_ai)
#                 speak("AI played " + say_san_for_tts(san_ai), block=False)
#             else:
#                 # If AI failed to provide a legal move, skip and continue
#                 info_lines.append("AI could not find a legal move (skipping).")

#         # handle events (hotkeys for undo/quit while not listening)
#         for ev in pygame.event.get():
#             if ev.type == pygame.QUIT:
#                 running = False
#             if ev.type == pygame.VIDEORESIZE:
#                 screen = pygame.display.set_mode(ev.size, pygame.RESIZABLE)
#             if ev.type == pygame.KEYDOWN:
#                 if ev.key == pygame.K_ESCAPE:
#                     running = False
#                 if ev.key == pygame.K_u:
#                     if board.move_stack:
#                         board.pop()
#                     if board.move_stack:
#                         board.pop()
#                     info_lines.append("Undid last full move.")
#                     last_move = board.move_stack[-1] if board.move_stack else None
#                 if ev.key == pygame.K_t and ENABLE_KEYBOARD_FALLBACK:
#                     typed = prompt_type_move(screen, ds)
#                     if typed:
#                         try:
#                             if re.fullmatch(r'[a-h][1-8][a-h][1-8][qrbn]?', typed):
#                                 m = chess.Move.from_uci(typed)
#                                 if m in board.legal_moves:
#                                     san_t = board.san(m)
#                                     board.push(m)
#                                     last_move = m
#                                     info_lines.append("Typed move: " + san_t)
#                                     speak("You played " + say_san_for_tts(san_t), block=False)
#                             else:
#                                 m = board.parse_san(typed)
#                                 if m in board.legal_moves:
#                                     san_t = board.san(m)
#                                     board.push(m)
#                                     last_move = m
#                                     info_lines.append("Typed SAN: " + san_t)
#                                     speak("You played " + say_san_for_tts(san_t), block=False)
#                         except Exception as e:
#                             info_lines.append("Typed move invalid.")
#     pygame.quit()
#     print("Exiting.")

# # --------------------------
# # Start
# # --------------------------
# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("Interrupted. Exiting.")
#         pygame.quit()
#         sys.exit(0)









# gui.py - Voice + typing chess GUI with improved recognition & robust TTS
# Requirements:
#   pip install pygame SpeechRecognition pyttsx3 python-chess pyaudio
#
# Author: ChatGPT (updated)
# Date: 2025-08-13 (voice recognition tuned)

import os
import sys
import time
import random
import re
import threading
import queue
from dataclasses import dataclass
from typing import Optional, Tuple, List

import pygame
import chess
import speech_recognition as sr
import pyttsx3

# --------------------------
# USER CONFIG (edit if needed)
# --------------------------
MIC_INDEX = None              # None = auto-detect. Use M key to cycle if needed
LISTEN_TIMEOUT = 6            # seconds to wait for speech to start
PHRASE_TIME_LIMIT = 6         # seconds max phrase
AMBIENT_NOISE_DURATION = 1.0  # longer calibration for better thresholds
MAX_VOICE_RETRIES = 2         # attempts per human turn (kept small: press V to try again)
ENABLE_KEYBOARD_FALLBACK = True
AI_THINK_DELAY = 0.45         # seconds, cosmetic delay

# GUI sizing
BASE_SQUARE = 88
MIN_SQUARE = 42

# Colors / style
BG_LIGHT = (240, 217, 181)
BG_DARK  = (181, 136, 99)
BG_SIDE  = (28, 32, 38)
TEXT_COL = (230, 232, 235)
# RGBA values (used with SRCALPHA surfaces)
HIGHLIGHT_MOVE = (120, 200, 120, 110)
HIGHLIGHT_CHECK = (220, 120, 120, 125)
OVERLAY_BG = (35, 40, 46)

# --------------------------
# Initialize pygame
# --------------------------
pygame.init()
pygame.display.set_caption("Voice-Controlled Chess")
clock = pygame.time.Clock()

def choose_font(size):
    for name in ["Segoe UI Symbol", "DejaVu Sans", "Arial Unicode MS", None]:
        try:
            return pygame.font.SysFont(name, size)
        except Exception:
            continue
    return pygame.font.Font(None, size)

font_piece = choose_font(int(BASE_SQUARE * 0.72))
font_side  = choose_font(18)
font_big   = choose_font(24)
font_huge  = choose_font(36)

# Unicode piece glyphs
PIECE_GLYPHS = {
    chess.PAWN:   ("♙", "♟"),
    chess.KNIGHT: ("♘", "♞"),
    chess.BISHOP: ("♗", "♝"),
    chess.ROOK:   ("♖", "♜"),
    chess.QUEEN:  ("♕", "♛"),
    chess.KING:   ("♔", "♚"),
}

# --------------------------
# Voice queue + single worker thread (pyttsx3)
# --------------------------
_voice_queue: "queue.Queue[Optional[str]]" = queue.Queue()
_tts_engine = pyttsx3.init()
try:
    _tts_engine.setProperty("rate", 170)
    _tts_engine.setProperty("volume", 1.0)
except Exception:
    pass

_voice_thread_stop = threading.Event()

def _voice_worker_loop():
    while not _voice_thread_stop.is_set():
        try:
            text = _voice_queue.get(timeout=0.2)
        except queue.Empty:
            continue
        if text is None:
            _voice_queue.task_done()
            break
        try:
            _tts_engine.say(text)
            _tts_engine.runAndWait()
        except Exception as e:
            print("[TTS] speak error:", e)
        finally:
            _voice_queue.task_done()

_voice_thread = threading.Thread(target=_voice_worker_loop, daemon=True)
_voice_thread.start()

def speak(text: str, block: bool = False):
    if not text:
        return
    _voice_queue.put(text)
    if block:
        while not _voice_queue.empty():
            time.sleep(0.02)

# --------------------------
# Speech-Recognition setup
# --------------------------
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.calibrated = False

def list_microphones() -> List[str]:
    try:
        names = sr.Microphone.list_microphone_names()
        print("Available microphones:")
        for i, n in enumerate(names):
            print(f"  {i}: {n}")
        return names
    except Exception as e:
        print("[Mic] Could not list microphones:", e)
        return []

def calibrate_once(mic_index: Optional[int]):
    try:
        with sr.Microphone(device_index=mic_index, sample_rate=16000, chunk_size=1024) as src:
            print("[Voice] Calibrating ambient noise for", AMBIENT_NOISE_DURATION, "seconds...")
            recognizer.dynamic_energy_threshold = True
            recognizer.adjust_for_ambient_noise(src, duration=AMBIENT_NOISE_DURATION)
            # fix energy threshold for stable detection
            suggested = max(110, int(recognizer.energy_threshold * 0.7)) if recognizer.energy_threshold else 300
            recognizer.dynamic_energy_threshold = False
            recognizer.energy_threshold = suggested
            recognizer.calibrated = True
            print(f"[Voice] Calibration complete. energy_threshold={recognizer.energy_threshold}")
            return True
    except Exception as e:
        print("[Voice] Calibration failed:", e)
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 400
        recognizer.calibrated = True
        return False

def _sanitize_raw_text_for_chess(raw: str) -> str:
    """Sanitize raw recognized text to increase chance of parsing:
       - Remove punctuation,
       - Fix repeated digits like e22 -> e2,
       - Remove stray numbers before squares (e.g. '822 e4' -> 'e4'),
       - Keep letters and digits only separated by spaces where helpful.
    """
    if not raw:
        return ""
    r = raw.lower()
    # replace common filler words
    r = r.replace(" to ", " ").replace("–", " ").replace("-", " ").replace("x", "x")
    # remove punctuation but keep letters/digits and 'o' for castle
    r = re.sub(r"[^a-z0-9\s]", " ", r)
    # collapse whitespace
    r = re.sub(r"\s+", " ", r).strip()

    # Fix tokens like e22 -> e2 (if a digit repeated or too long)
    def fix_token(tok):
        # common misrecognitions like "e22" or "b22"
        m = re.fullmatch(r"([a-h])([1-8]{2,})", tok)
        if m:
            return m.group(1) + m.group(2)[0]
        # tokens like '822' or '122' alone: drop them
        if re.fullmatch(r"\d{2,}", tok):
            return ""
        # tokens like '8e4' -> try to reorder if possible
        m2 = re.fullmatch(r"(\d)([a-h][1-8])", tok)
        if m2:
            return m2.group(2)
        # keep token as-is
        return tok

    parts = [fix_token(p) for p in r.split()]
    parts = [p for p in parts if p]  # drop empty
    return " ".join(parts)

def listen_once(mic_index: Optional[int]) -> Optional[str]:
    try:
        with sr.Microphone(device_index=mic_index, sample_rate=16000, chunk_size=1024) as source:
            if not getattr(recognizer, "calibrated", False):
                calibrate_once(mic_index)
            print("[Voice] Please speak now... (or press V to trigger manually)")
            audio = recognizer.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=PHRASE_TIME_LIMIT)
        print("[Voice] Recognizing...")
        try:
            text = recognizer.recognize_google(audio)
            print("[Voice] Raw:", text)
            sanitized = _sanitize_raw_text_for_chess(text)
            print("[Voice] Sanitized:", sanitized)
            return sanitized
        except sr.UnknownValueError:
            print("[Voice] Could not understand audio.")
            return None
        except sr.RequestError as e:
            print("[Voice] Recognition service error:", e)
            return None
    except sr.WaitTimeoutError:
        print("[Voice] No speech detected (timeout).")
        return None
    except Exception as e:
        print("[Voice] Microphone/listen error:", e)
        return None

class VoiceWorker(threading.Thread):
    def __init__(self, mic_index: Optional[int], gen_id: int):
        super().__init__(daemon=True)
        self.mic_index = mic_index
        self.gen_id = gen_id
        self.result_norm: Optional[str] = None
        self.finished = False

    def run(self):
        raw = listen_once(self.mic_index)
        if raw:
            # normalize recognized spoken text into move-like tokens
            self.result_norm = normalize_spoken_text(raw)
        self.finished = True

# --------------------------
# Speech normalization → move parser
# --------------------------
_NUM_WORDS = {
    "one": "1", "two": "2", "three": "3", "four": "4", "for": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "ate": "8",
}
_FILE_WORDS = {
    "alpha":"a","a":"a","bravo":"b","b":"b","charlie":"c","c":"c","delta":"d","d":"d",
    "echo":"e","e":"e","foxtrot":"f","f":"f","golf":"g","g":"g","hotel":"h","h":"h"
}
_PIECE_WORDS = {"pawn":"P","knight":"N","night":"N","bishop":"B","rook":"R","queen":"Q","king":"K"}

def normalize_spoken_text(text: str) -> Optional[str]:
    if not text:
        return None
    t = text.lower().strip()
    # accept already-sanitized 'e2e4' etc
    t = re.sub(r'[^\w\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()

    # castle
    if "castle long" in t or "queen side" in t or re.search(r"o\s*o\s*o", t):
        return "O-O-O"
    if "castle" in t or "king side" in t or re.search(r"o\s*o", t):
        return "O-O"

    tokens = re.findall(r"[A-Za-z]+|\d+", t)
    norm = []
    for tok in tokens:
        if tok in _FILE_WORDS:
            norm.append(_FILE_WORDS[tok])
        elif tok in _NUM_WORDS:
            norm.append(_NUM_WORDS[tok])
        elif len(tok) == 1 and tok in "abcdefgh":
            norm.append(tok)
        elif tok.isdigit() and tok in "12345678":
            norm.append(tok)
        elif tok in _PIECE_WORDS:
            norm.append(_PIECE_WORDS[tok])
        else:
            # if token like 'e2e4' collapse into letters+digits
            m = re.findall(r'[a-h]\d', tok)
            if m and len(m) >= 2:
                return "".join(m[:2])
            if tok and tok[0] in "abcdefgh":
                norm.append(tok[0])
            else:
                norm.append(tok)

    # attempt two squares in a row
    squares = []
    i = 0
    while i < len(norm):
        if i + 1 < len(norm) and norm[i] in list("abcdefgh") and norm[i+1] in list("12345678"):
            squares.append(norm[i] + norm[i+1])
            i += 2
        else:
            i += 1
    if len(squares) >= 2:
        return squares[0] + squares[1]

    # piece + square e.g. N f3
    for idx, tok in enumerate(norm):
        if tok in ("P","N","B","R","Q","K"):
            if idx + 2 < len(norm) and norm[idx+1] in list("abcdefgh") and norm[idx+2] in list("12345678"):
                return tok + norm[idx+1] + norm[idx+2]
            if idx + 1 < len(norm) and re.fullmatch(r"[a-h][1-8]", "".join(norm[idx+1:idx+3])):
                return tok + "".join(norm[idx+1:idx+3])

    # compact original (uci)
    compact = re.sub(r'\s+','',t)
    if re.fullmatch(r'[a-h][1-8][a-h][1-8][qrbn]?', compact):
        return compact

    # single square like e4
    for i in range(len(norm)-1):
        if norm[i] in list("abcdefgh") and norm[i+1] in list("12345678"):
            return norm[i] + norm[i+1]

    return None

# --------------------------
# Chess GUI helpers (drawing etc)
# --------------------------
@dataclass
class DrawState:
    w: int
    h: int
    square: int
    margin: int

def compute_draw_state(screen_size: Tuple[int,int]) -> DrawState:
    w,h = screen_size
    margin = max(int(w * 0.12), 240)
    board_pixels = min(h, w - margin)
    square = max(MIN_SQUARE, board_pixels // 8)
    return DrawState(w=w, h=h, square=square, margin=w - board_pixels)

def board_to_rect(ds: DrawState, file: int, rank: int) -> pygame.Rect:
    x = file * ds.square
    y = (7 - rank) * ds.square
    return pygame.Rect(x, y, ds.square, ds.square)

def draw_board(screen: pygame.Surface, board: chess.Board, last_move: Optional[chess.Move], ds: DrawState):
    for r in range(8):
        for f in range(8):
            rect = board_to_rect(ds, f, r)
            color = BG_LIGHT if (f + r) % 2 == 0 else BG_DARK
            pygame.draw.rect(screen, color, rect)
    if last_move:
        for sq in (last_move.from_square, last_move.to_square):
            f = chess.square_file(sq); r = chess.square_rank(sq)
            rect = board_to_rect(ds, f, r)
            s = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
            s.fill(HIGHLIGHT_MOVE)
            screen.blit(s, rect.topleft)
    if board.is_check():
        king_sq = board.king(board.turn)
        if king_sq is not None:
            f = chess.square_file(king_sq); r = chess.square_rank(king_sq)
            rect = board_to_rect(ds, f, r)
            s = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
            s.fill(HIGHLIGHT_CHECK)
            screen.blit(s, rect.topleft)

def draw_pieces(screen: pygame.Surface, board: chess.Board, ds: DrawState):
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if not piece:
            continue
        f = chess.square_file(sq); r = chess.square_rank(sq)
        rect = board_to_rect(ds, f, r)
        glyph = PIECE_GLYPHS[piece.piece_type][0 if piece.color == chess.WHITE else 1]
        surf = font_piece.render(glyph, True, (30,30,30))
        tw,th = surf.get_size()
        screen.blit(surf, (rect.x + (rect.w - tw)//2, rect.y + (rect.h - th)//2))

def draw_sidebar(screen: pygame.Surface, ds: DrawState, board: chess.Board, info: List[str], mic_names: List[str], selected_mic: Optional[int]):
    x0 = ds.square * 8
    pygame.draw.rect(screen, BG_SIDE, (x0, 0, ds.margin, ds.h))
    title = font_big.render("Voice Chess", True, TEXT_COL)
    screen.blit(title, (x0 + 12, 10))
    turn = "White" if board.turn == chess.WHITE else "Black"
    screen.blit(font_side.render(f"Turn: {turn}", True, TEXT_COL), (x0 + 12, 48))

    lines = [
        "Speak examples:",
        "  E2 to E4  /  Echo two to Echo four",
        "  Knight to F3",
        "  pawn to e4, castle, castle long",
        "",
        "Controls:",
        "  V = listen now (voice capture)",
        "  M = cycle microphone",
        "  T = type move (overlay)",
        "  U = undo last full move",
        "  R = AI moves now",
        "  Esc = quit",
        "",
        f"Mic index: {selected_mic if selected_mic is not None else 'auto'}",
        ""
    ]
    y = 120
    for line in lines:
        screen.blit(font_side.render(line, True, TEXT_COL), (x0 + 12, y))
        y += 22

    # show mic list (abbreviated)
    if mic_names:
        screen.blit(font_side.render("Available mics (press M to cycle):", True, TEXT_COL), (x0 + 12, y))
        y += 20
        for i, m in enumerate(mic_names[:6]):
            label = f"{i}: {m}" if i < len(mic_names) else ""
            screen.blit(font_side.render(label, True, TEXT_COL), (x0 + 12, y))
            y += 18
        y += 6

    # recent log lines
    screen.blit(font_side.render("Recent:", True, TEXT_COL), (x0 + 12, y))
    y += 22
    for line in info[-8:]:
        screen.blit(font_side.render(line, True, TEXT_COL), (x0 + 12, y))
        y += 18

def draw_center_hint(screen: pygame.Surface, ds: DrawState, text: str, blink: bool):
    if blink:
        overlay = pygame.Surface((ds.w, ds.h), pygame.SRCALPHA)
        overlay.fill((0,0,0,140))
        screen.blit(overlay, (0,0))
        box = pygame.Rect(ds.w//2 - 360, ds.h//2 - 55, 720, 110)
        pygame.draw.rect(screen, OVERLAY_BG, box, border_radius=16)
        label = font_huge.render(text, True, (240,240,240))
        lw, lh = label.get_size()
        screen.blit(label, (box.x + (box.w - lw)//2, box.y + (box.h - lh)//2))

def prompt_type_move(screen: pygame.Surface, ds: DrawState) -> Optional[str]:
    buffer = ""
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return None
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    return buffer.strip()
                if ev.key == pygame.K_ESCAPE:
                    return None
                if ev.key == pygame.K_BACKSPACE:
                    buffer = buffer[:-1]
                else:
                    ch = ev.unicode
                    if ch and ch.isprintable():
                        buffer += ch

        overlay = pygame.Surface((ds.w, ds.h), pygame.SRCALPHA)
        overlay.fill((0,0,0,180))
        screen.blit(overlay, (0,0))
        box = pygame.Rect(ds.w//2 - 320, ds.h//2 - 50, 640, 100)
        pygame.draw.rect(screen, OVERLAY_BG, box, border_radius=14)
        label = font_big.render("Type move (e.g. e2e4 or Nf3). Enter submits.", True, (230,230,230))
        screen.blit(label, (box.x + 12, box.y + 10))
        textsurf = font_big.render(buffer or " ", True, (240,240,240))
        screen.blit(textsurf, (box.x + 12, box.y + 56))
        pygame.display.flip()
        clock.tick(60)

# --------------------------
# AI
# --------------------------
def random_ai_move(board: chess.Board) -> Optional[chess.Move]:
    moves = list(board.legal_moves)
    return random.choice(moves) if moves else None

# --------------------------
# Main
# --------------------------
def main():
    init_w = BASE_SQUARE * 8 + 320
    init_h = BASE_SQUARE * 8
    screen = pygame.display.set_mode((init_w, init_h), pygame.RESIZABLE)
    pygame.display.set_caption("Voice-Controlled Chess")

    mic_names = list_microphones()
    selected_mic = MIC_INDEX
    # auto-select
    if selected_mic is None:
        chosen = None
        for i, name in enumerate(mic_names):
            low = (name or "").lower()
            if i == 0 and "microsoft sound mapper" in low:
                continue
            if "microphone" in low or "headset" in low or "input" in low:
                chosen = i
                break
        if chosen is None:
            chosen = 1 if len(mic_names) > 1 else (0 if mic_names else None)
        selected_mic = chosen

    print(f"Selected MIC_INDEX = {selected_mic} ({mic_names[selected_mic] if mic_names and selected_mic is not None and selected_mic < len(mic_names) else 'unknown'})")
    calibrate_once(selected_mic)

    board = chess.Board()
    last_move: Optional[chess.Move] = None
    info_lines: List[str] = []
    info_lines.append("Say moves, or press T to type. Press Esc to quit.")

    # greeting
    greeting_msg = "Welcome to Voice Controlled Chess. Press V to speak when ready, M to change mic."
    speak(greeting_msg)
    info_lines.append("Greetings: " + greeting_msg)

    human_color = chess.WHITE
    running = True

    # voice state for background auto-capture (we still rely on manual V for best UX)
    voice_gen = 0
    voice_worker: Optional[VoiceWorker] = None

    show_type_hint_until = 0.0

    while running:
        clock.tick(60)
        ds = compute_draw_state(screen.get_size())
        screen.fill((0,0,0))
        draw_board(screen, board, last_move, ds)
        draw_pieces(screen, board, ds)
        draw_sidebar(screen, ds, board, info_lines, mic_names, selected_mic)
        now = time.time()
        if now < show_type_hint_until:
            blink = int(now * 2) % 2 == 0
            draw_center_hint(screen, ds, "Press T to TYPE your move", blink)
        pygame.display.flip()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(ev.size, pygame.RESIZABLE)
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False

                # Manual voice capture
                elif ev.key == pygame.K_v:
                    info_lines.append("[Voice] Manual capture (V pressed)")
                    speak("Listening for your move now.")
                    raw = listen_once(selected_mic)
                    if raw:
                        heard = normalize_spoken_text(raw)
                        info_lines.append("Heard: " + (heard or "<none>"))
                        if heard:
                            try:
                                speak(f"I heard {spell_for_feedback(heard)}")
                            except Exception:
                                pass
                            mv = parse_text_to_move(board, heard)
                            if mv:
                                san = board.san(mv)
                                board.push(mv)
                                last_move = mv
                                info_lines.append("You played: " + san)
                                speak("You played " + say_san_for_tts(san))
                                announce_position_status(board)
                                # AI reply
                                if not board.is_game_over():
                                    time.sleep(AI_THINK_DELAY)
                                    ai_mv = random_ai_move(board)
                                    if ai_mv and ai_mv in board.legal_moves:
                                        try:
                                            san_ai = board.san(ai_mv)
                                        except Exception:
                                            san_ai = ai_mv.uci()
                                        board.push(ai_mv)
                                        last_move = ai_mv
                                        info_lines.append("AI played: " + san_ai)
                                        speak("AI played " + say_san_for_tts(san_ai))
                                        announce_position_status(board)
                            else:
                                info_lines.append("Heard but invalid/illegal: " + heard)
                                speak("That move couldn't be parsed or is illegal. Try again.")
                        else:
                            info_lines.append("Voice: nothing recognized.")
                            speak("I didn't hear a move. Try again or press T to type.")
                    else:
                        info_lines.append("Voice: capture returned None.")
                        speak("No speech detected or recognition failed.")
                    # end manual voice

                # cycle microphone list
                elif ev.key == pygame.K_m:
                    if mic_names:
                        if selected_mic is None:
                            selected_mic = 0
                        else:
                            selected_mic = (selected_mic + 1) % len(mic_names)
                        info_lines.append(f"Selected mic index {selected_mic}: {mic_names[selected_mic]}")
                        speak(f"Selected microphone {selected_mic}")
                        calibrate_once(selected_mic)
                    else:
                        info_lines.append("No microphones found.")
                        speak("No microphones available.")

                elif ev.key == pygame.K_t and ENABLE_KEYBOARD_FALLBACK:
                    typed = prompt_type_move(screen, ds)
                    if typed:
                        mv = parse_text_to_move(board, typed)
                        if mv:
                            san_t = board.san(mv)
                            board.push(mv)
                            last_move = mv
                            info_lines.append("You typed: " + san_t)
                            speak("You played " + say_san_for_tts(san_t))
                            announce_position_status(board)
                            # AI reply
                            if not board.is_game_over():
                                time.sleep(AI_THINK_DELAY)
                                ai_mv = random_ai_move(board)
                                if ai_mv and ai_mv in board.legal_moves:
                                    try:
                                        san_ai = board.san(ai_mv)
                                    except Exception:
                                        san_ai = ai_mv.uci()
                                    board.push(ai_mv)
                                    last_move = ai_mv
                                    info_lines.append("AI played: " + san_ai)
                                    speak("AI played " + say_san_for_tts(san_ai))
                                    announce_position_status(board)
                        else:
                            info_lines.append("Typed move invalid or illegal.")
                            speak("That typed move is illegal or invalid.")

                elif ev.key == pygame.K_u:
                    if board.move_stack:
                        board.pop()
                    if board.move_stack:
                        board.pop()
                    last_move = board.move_stack[-1] if board.move_stack else None
                    info_lines.append("Undid last full move.")
                    speak("Undid last full move.")

                elif ev.key == pygame.K_r:
                    mv = random_ai_move(board)
                    if mv and mv in board.legal_moves:
                        try:
                            san_ai = board.san(mv)
                        except Exception:
                            san_ai = mv.uci()
                        board.push(mv)
                        last_move = mv
                        info_lines.append("AI (forced) played: " + san_ai)
                        speak("AI played " + say_san_for_tts(san_ai))
                        announce_position_status(board)

        # If game over, announce once
        if board.is_game_over():
            res = board.result()
            if board.is_checkmate():
                winner = "Black" if board.turn == chess.WHITE else "White"
                msg = f"Checkmate. {winner} wins."
            elif board.is_stalemate():
                msg = "Draw by stalemate."
            elif board.is_insufficient_material():
                msg = "Draw by insufficient material."
            elif board.can_claim_threefold_repetition():
                msg = "Draw by repetition."
            else:
                msg = f"Game over: {res}."
            if not info_lines or info_lines[-1] != msg:
                info_lines.append(msg)
                speak(msg + " Press Escape to exit.")
            continue

    # Shutdown voice thread cleanly
    try:
        _voice_queue.put(None)
        _voice_thread.join(timeout=2.0)
    except Exception:
        pass

    pygame.quit()
    print("Exiting.")

def parse_text_to_move(board: chess.Board, text: str) -> Optional[chess.Move]:
    if not text:
        return None
    t = text.strip()
    if re.fullmatch(r'[a-h][1-8][a-h][1-8][qrbn]?', t.lower()):
        try:
            m = chess.Move.from_uci(t.lower())
            return m if m in board.legal_moves else None
        except Exception:
            return None
    try:
        m = board.parse_san(t)
        return m if m in board.legal_moves else None
    except Exception:
        pass
    if re.fullmatch(r'[a-h][1-8]', t.lower()):
        dest = t.lower()
        cands = [mv for mv in board.legal_moves if chess.square_name(mv.to_square) == dest]
        if len(cands) == 1:
            return cands[0]
        elif cands:
            return cands[0]
    return None

def say_san_for_tts(san: str) -> str:
    s = san.replace("+", " check").replace("#", " checkmate")
    if s in ("O-O","0-0"):
        return "castle"
    if s in ("O-O-O","0-0-0"):
        return "castle long"
    s = s.replace("K","King ").replace("Q","Queen ").replace("R","Rook ").replace("B","Bishop ").replace("N","Knight ")
    s = s.replace("x"," takes ")
    s = re.sub(
        r"([a-h])([1-8])",
        lambda m: f"{m.group(1).upper()} " + {
            '1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight'
        }[m.group(2)],
        s
    )
    return s

def announce_position_status(board: chess.Board):
    if board.is_checkmate():
        winner = "Black" if board.turn == chess.WHITE else "White"
        speak(f"Checkmate. {winner} wins.")
    elif board.is_stalemate():
        speak("Draw by stalemate.")
    elif board.is_insufficient_material():
        speak("Draw by insufficient material.")
    elif board.can_claim_threefold_repetition():
        speak("Draw by repetition.")
    elif board.is_check():
        speak("Check.")

def spell_for_feedback(move_text: str) -> str:
    s = move_text.upper()
    if s in ("O-O","0-0"):
        return "castle"
    if s in ("O-O-O","0-0-0"):
        return "castle long"
    return " ".join(list(s))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted. Exiting.")
        try:
            _voice_queue.put(None)
            _voice_thread.join(timeout=1.0)
        except Exception:
            pass
        pygame.quit()
        sys.exit(0)
