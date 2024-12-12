import pygame
import sys
from time import sleep
import time
from Game import *
# Initialize pygame
pygame.init()

window_size = 700
grid_size = 7
cell_size = window_size // grid_size

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Game Time Display')

game_instance = Game()
font = pygame.font.Font(None, 27)

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
    pygame.draw.rect(screen, (0, 255, 0), (pixel_pos[0], pixel_pos[1], cell_size, cell_size))


def draw_players():
    """Draw the toddlers and the teacher on the grid."""
    for toddler in game_instance.get_toddlers():
        toddler_pos = toddler.get_position()
        pixel_pos = (toddler_pos[0] * cell_size + cell_size // 2, toddler_pos[1] * cell_size + cell_size // 2)
        pygame.draw.circle(screen, (0, 0, 255), pixel_pos, cell_size // 3)

    teacher = game_instance.get_teacher()
    teacher_pos = teacher.get_position()
    pixel_pos = (teacher_pos[0] * cell_size, teacher_pos[1] * cell_size)
    pygame.draw.rect(screen, (255, 0, 0), (pixel_pos[0], pixel_pos[1], cell_size, cell_size))

def draw_end_game():
    """Draw the end game screen with players' points."""
    screen.fill((255, 255, 255))
    draw_candy()
    draw_player_points()
    draw_players()

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
    while game_instance.get_running():
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

        # draw_resources()
#        draw_player_points()
        draw_players()
        draw_candy()
        # Render the time text
        time_text = font.render(f"Time: {game_instance.get_time()}", True, (0, 0, 0))
        screen.blit(time_text, (10, 10))

        # Update the display
        pygame.display.flip()

    sleep(1)
    draw_end_game()