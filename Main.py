import pygame
import sys
from time import sleep
import time
import os
from reportlab.graphics.samples.excelcolors import backgroundGrey

from Game import *

# Initialize pygame
pygame.init()
pygame.mixer.init()

window_size = 900
grid_size = 13
cell_size = window_size // grid_size

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Game Time Display')
bell = pygame.mixer.Sound('Sounds/school-bell.mp3')
punch = pygame.mixer.Sound('Sounds/punch.mp3')
punch.set_volume(2)
coin = pygame.mixer.Sound('Sounds/coin.mp3')
coin.set_volume(0.3)

tod1 = pygame.image.load('Pictures/characters/tod1.png')
tod1w1r = pygame.image.load('Pictures/characters/tod1w1r.png')
tod1w1l = pygame.image.load('Pictures/characters/tod1w1l.png')
tod1w2r = pygame.image.load('Pictures/characters/tod1w2r.png')
tod1w2l = pygame.image.load('Pictures/characters/tod1w2l.png')
tod1w1rc = pygame.image.load('Pictures/characters/tod1w1rc.png')
tod1w1lc = pygame.image.load('Pictures/characters/tod1w1lc.png')
tod1w2rc = pygame.image.load('Pictures/characters/tod1w2rc.png')
tod1w2lc = pygame.image.load('Pictures/characters/tod1w2lc.png')
tod1upc = pygame.image.load('Pictures/characters/tod1upc.png')
tod1down = pygame.image.load('Pictures/characters/tod1down.png')
tod1downc = pygame.image.load('Pictures/characters/tod1downc.png')

tod2 = pygame.image.load('Pictures/characters/tod2.png')
tod2w1r = pygame.image.load('Pictures/characters/tod2w1r.png')
tod2w1l = pygame.image.load('Pictures/characters/tod2w1l.png')
tod2w2r = pygame.image.load('Pictures/characters/tod2w2r.png')
tod2w2l = pygame.image.load('Pictures/characters/tod2w2l.png')
tod2w1rc = pygame.image.load('Pictures/characters/tod2w1rc.png')
tod2w1lc = pygame.image.load('Pictures/characters/tod2w1lc.png')
tod2w2rc = pygame.image.load('Pictures/characters/tod2w2rc.png')
tod2w2lc = pygame.image.load('Pictures/characters/tod2w2lc.png')
tod2upc = pygame.image.load('Pictures/characters/tod2upc.png')
tod2down = pygame.image.load('Pictures/characters/tod2down.png')
tod2downc = pygame.image.load('Pictures/characters/tod2downc.png')

tod3 = pygame.image.load('Pictures/characters/tod3.png')
tod3w1r = pygame.image.load('Pictures/characters/tod3w1r.png')
tod3w1l = pygame.image.load('Pictures/characters/tod3w1l.png')
tod3w2r = pygame.image.load('Pictures/characters/tod3w2r.png')
tod3w2l = pygame.image.load('Pictures/characters/tod3w2l.png')
tod3w1rc = pygame.image.load('Pictures/characters/tod3w1rc.png')
tod3w1lc = pygame.image.load('Pictures/characters/tod3w1lc.png')
tod3w2rc = pygame.image.load('Pictures/characters/tod3w2rc.png')
tod3w2lc = pygame.image.load('Pictures/characters/tod3w2lc.png')
tod3upc = pygame.image.load('Pictures/characters/tod3upc.png')
tod3down = pygame.image.load('Pictures/characters/tod3down.png')
tod3downc = pygame.image.load('Pictures/characters/tod3downc.png')

tod4 = pygame.image.load('Pictures/characters/tod4.png')
tod4w1r = pygame.image.load('Pictures/characters/tod4w1r.png')
tod4w1l = pygame.image.load('Pictures/characters/tod4w1l.png')
tod4w2r = pygame.image.load('Pictures/characters/tod4w2r.png')
tod4w2l = pygame.image.load('Pictures/characters/tod4w2l.png')
tod4w1rc = pygame.image.load('Pictures/characters/tod4w1rc.png')
tod4w1lc = pygame.image.load('Pictures/characters/tod4w1lc.png')
tod4w2rc = pygame.image.load('Pictures/characters/tod4w2rc.png')
tod4w2lc = pygame.image.load('Pictures/characters/tod4w2lc.png')
tod4upc = pygame.image.load('Pictures/characters/tod4upc.png')
tod4down = pygame.image.load('Pictures/characters/tod4down.png')
tod4downc = pygame.image.load('Pictures/characters/tod4downc.png')

tod5 = pygame.image.load('Pictures/characters/tod5.png')
tod5w1r = pygame.image.load('Pictures/characters/tod5w1r.png')
tod5w1l = pygame.image.load('Pictures/characters/tod5w1l.png')
tod5w2r = pygame.image.load('Pictures/characters/tod5w2r.png')
tod5w2l = pygame.image.load('Pictures/characters/tod5w2l.png')
tod5w1rc = pygame.image.load('Pictures/characters/tod5w1rc.png')
tod5w1lc = pygame.image.load('Pictures/characters/tod5w1lc.png')
tod5w2rc = pygame.image.load('Pictures/characters/tod5w2rc.png')
tod5w2lc = pygame.image.load('Pictures/characters/tod5w2lc.png')
tod5upc = pygame.image.load('Pictures/characters/tod5upc.png')
tod5down = pygame.image.load('Pictures/characters/tod5down.png')
tod5downc = pygame.image.load('Pictures/characters/tod5downc.png')

tod6 = pygame.image.load('Pictures/characters/tod6.png')
tod6w1r = pygame.image.load('Pictures/characters/tod6w1r.png')
tod6w1l = pygame.image.load('Pictures/characters/tod6w1l.png')
tod6w2r = pygame.image.load('Pictures/characters/tod6w2r.png')
tod6w2l = pygame.image.load('Pictures/characters/tod6w2l.png')
tod6w1rc = pygame.image.load('Pictures/characters/tod6w1rc.png')
tod6w1lc = pygame.image.load('Pictures/characters/tod6w1lc.png')
tod6w2rc = pygame.image.load('Pictures/characters/tod6w2rc.png')
tod6w2lc = pygame.image.load('Pictures/characters/tod6w2lc.png')
tod6upc = pygame.image.load('Pictures/characters/tod6upc.png')
tod6down = pygame.image.load('Pictures/characters/tod6down.png')
tod6downc = pygame.image.load('Pictures/characters/tod6downc.png')


toddlersPic = [[tod1, tod1w1r, tod1w1l, tod1w2r, tod1w2l, tod1w1rc, tod1w1lc, tod1w2rc, tod1w2lc,tod1upc,tod1down,tod1downc],
               [tod2, tod2w1r, tod2w1l, tod2w2r, tod2w2l, tod2w1rc, tod2w1lc, tod2w2rc, tod2w2lc,tod2upc,tod2down, tod2downc],
               [tod3, tod3w1r, tod3w1l, tod3w2r, tod3w2l, tod3w1rc, tod3w1lc, tod3w2rc, tod3w2lc,tod3upc, tod3down, tod3downc],
               [tod4, tod4w1r, tod4w1l, tod4w2r, tod4w2l, tod4w1rc, tod4w1lc, tod4w2rc, tod4w2lc,tod4upc, tod4down, tod4downc],
               [tod5, tod5w1r, tod5w1l, tod5w2r, tod5w2l, tod5w1rc, tod5w1lc, tod5w2rc, tod5w2lc,tod5upc,tod5down,tod5downc],
               [tod6, tod6w1r, tod6w1l, tod6w2r, tod6w2l, tod6w1rc, tod6w1lc, tod6w2rc, tod6w2lc,tod6upc,tod6down,tod6downc]]


for pic in toddlersPic:
    for i in range(12):
        pic[i] = pygame.transform.scale(pic[i], (cell_size*1.2, cell_size*1.2))

teach = pygame.image.load('Pictures/characters/teach.png')
teach = pygame.transform.scale(teach, (cell_size*1.4, cell_size*1.4))


candy = pygame.image.load('Pictures/bonbons.png')
table = pygame.image.load('Pictures/table2.png')
candy = pygame.transform.scale(candy, (cell_size*0.8, cell_size*0.8))
table = pygame.transform.scale(table, (cell_size*1.5, cell_size*1.5))



background=pygame.image.load('Pictures/classroom3.png')
background_image = pygame.transform.scale(background, (window_size, window_size))

game_instance = Game(grid_size)
font = pygame.font.Font(None, 27)

catch_detector = 0
candy_detector = 0

def draw_text_with_contour(text, font, text_color, contour_color, x, y):
    """Draw text with a contour."""
    base_text = font.render(text, True, contour_color)
    text_rect = base_text.get_rect(center=(x, y))

    # Draw contour
    screen.blit(base_text, text_rect.move(-1, -1))
    screen.blit(base_text, text_rect.move(1, -1))
    screen.blit(base_text, text_rect.move(-1, 1))
    screen.blit(base_text, text_rect.move(1, 1))

    # Draw main text
    main_text = font.render(text, True, text_color)
    screen.blit(main_text, text_rect)

def draw_player_points():
    y_offset = 40
    for toddler in game_instance.get_toddlers():
        points_text = f"Toddler {toddler.get_id()} Points: {toddler.get_points()}"
        draw_text_with_contour(points_text, font, (0, 0, 0), (255, 255, 255), 10 + font.size(points_text)[0] // 2, y_offset)
        y_offset += 30

def draw_candy():
    """Draw the candy on the grid."""
    candy_pos = game_instance.get_candy()
    pixel_pos = (candy_pos[0] * cell_size, candy_pos[1] * cell_size)
    screen.blit(candy, (pixel_pos[0], pixel_pos[1]))




def draw_players():
    """Draw the toddlers and the teacher on the grid."""
    initial_positions = game_instance.get_initial_positions()
    toddlers = game_instance.get_toddlers()
    for t in toddlers:
        pos = t.get_pos_table()
        pixel_pos = (pos[0] * cell_size, pos[1] * cell_size)
        screen.blit(table, (pixel_pos[0], pixel_pos[1]))

    teacher_initial_pos = game_instance.get_teacher().get_pos_table()
    pixel_pos = (teacher_initial_pos[0] * cell_size, teacher_initial_pos[1] * cell_size)
    screen.blit(table, (pixel_pos[0], pixel_pos[1]))

    for toddler in game_instance.get_toddlers():
        toddler_pos = toddler.get_position()
        pixel_pos = (toddler_pos[0] * cell_size, toddler_pos[1] * cell_size)
        index = toddler.TYPE

        if toddler.get_table() or (toddler.get_direction() == "up" and not toddler.get_has_candy()):
            image = toddlersPic[index][0]
        else:
            if toddler.get_direction() == 'right':
                if not toddler.get_has_candy():
                    image = toddlersPic[index][1] if toddler_pos[0] % 2 == 0 else toddlersPic[index][3]
                else:
                    image = toddlersPic[index][5] if toddler_pos[0] % 2 == 0 else toddlersPic[index][7]
            elif toddler.get_direction() == 'left':
                if not toddler.get_has_candy():
                    image = toddlersPic[index][2] if toddler_pos[0] % 2 == 0 else toddlersPic[index][4]
                else:
                    image = toddlersPic[index][6] if toddler_pos[0] % 2 == 0 else toddlersPic[index][8]
            elif toddler.get_direction() == 'up':
                image = toddlersPic[index][9]
            else:
                if not toddler.get_has_candy():
                    image = toddlersPic[index][10]
                else:
                    image = toddlersPic[index][11]
        screen.blit(image, (pixel_pos[0], pixel_pos[1]))

        # Draw the number of candies on the initial position only if the toddler is at its initial position
        if toddler_pos == toddler.get_pos_table():
            initial_pos = toddler.get_pos_table()
            pixel_pos = (initial_pos[0] * cell_size, initial_pos[1] * cell_size)
            candies_text = font.render(str(toddler.get_candies()), True, (0, 0, 0))
            screen.blit(candies_text, (pixel_pos[0], pixel_pos[1]))

    teacher = game_instance.get_teacher()
    teacher_pos = teacher.get_position()
    pixel_pos = (teacher_pos[0] * cell_size, teacher_pos[1] * cell_size)
    screen.blit(teach, (pixel_pos[0], pixel_pos[1]))

    # Draw the number of caught toddlers on the teacher's initial position
    nb_caught_text = font.render(str(teacher.get_nb_caught()), True, (0, 0, 0))
    screen.blit(nb_caught_text, (teacher_initial_pos[0] * cell_size, teacher_initial_pos[1] * cell_size))



def draw_end_game():
    """Draw the end game screen with players' points."""
    screen.blit(background_image, (0, 0))  # Draw the background image first

    # Load all crying images
    crying_images = []
    for filename in os.listdir('Pictures/crying'):
        if filename.endswith('.png'):
            image = pygame.image.load(os.path.join('Pictures/crying', filename))
            image = pygame.transform.scale(image, (cell_size, cell_size))
            crying_images.append(image)

    # Calculate the total width of all images combined
    total_width = len(crying_images) * cell_size
    start_x = (window_size - total_width) // 2

    # Blit all crying images in a line centered at the top
    for i, image in enumerate(crying_images):
        screen.blit(image, (start_x + i * cell_size, 0))

    # Load and scale the angry teacher image
    library = pygame.image.load('Pictures/angry_teacher.png')
    library = pygame.transform.scale(library, (cell_size * 3, cell_size * 3))

    # Calculate the position to center the image at the bottom
    library_x = (window_size - library.get_width()) // 2
    library_y = window_size - library.get_height()

    # Blit the angry teacher image centered at the bottom
    screen.blit(library, (library_x, library_y))
    total_candy = 0
    y_offset = 100
    for toddler in game_instance.get_toddlers():
        points_text = f"Toddler {toddler.get_id()} Points: {toddler.get_points()}"
        draw_text_with_contour(points_text, font, (0, 0, 0), (255, 255, 255), window_size // 2, y_offset)
        y_offset += 30

    nb_tours_text = f"Total Turns: {game_instance.get_time()}"
    draw_text_with_contour(nb_tours_text, font, (0, 0, 0), (255, 255, 255), window_size // 2, y_offset + 100)

    pygame.display.flip()


last_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game_instance.stop_game()
    while game_instance.get_running():
        if game_instance.get_time() == 0 or game_instance.get_time() == 32:
            bell.play()
        elif game_instance.get_time()==33:
            game_instance.stop_game()

        if game_instance.get_teacher().get_nb_caught() != catch_detector:
            punch.play()
            catch_detector = game_instance.get_teacher().get_nb_caught()

        s=0
        for toddler in game_instance.get_toddlers():
            s+=toddler.get_candies()
        if s != candy_detector:
            coin.play()
            candy_detector = s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_instance.stop_game()

        current_time = time.time()


        if current_time - last_time >= 1:
            game_instance.increment_time()
            game_instance.action()
            last_time = current_time

        screen.fill((255, 255, 255))

        for x in range(0, window_size, cell_size):
            for y in range(0, window_size, cell_size):
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)

        screen.blit(background_image, (0, 0))
        draw_players()
        draw_candy()

        # Render the time text
        time_text = font.render(f"Time: {game_instance.get_time()}", True, (0, 0, 0))
        screen.blit(time_text, (10, 10))

        # Update the display
        pygame.display.flip()

    sleep(1)
    draw_end_game()