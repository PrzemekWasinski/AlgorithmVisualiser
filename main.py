import pygame
from pygame.locals import *
import random
import os
from functions import draw_array, bubble_sort, insertion_sort, selection_sort, heap_sort, cocktail_sort

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load(os.path.join("textures", "icon.png")) 
pygame.display.set_icon(icon)
pygame.display.set_caption("Algorithm Visualiser")

array = []
for i in range(1, 321):
     array.append(i)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))
text_font = pygame.font.SysFont("Calibri",14)

shuffle_rect = pygame.image.load(os.path.join("textures", "shuffle.png"))
bubble_sort_rect = pygame.image.load(os.path.join("textures", "bubble_sort.png"))
insertion_sort_rect = pygame.image.load(os.path.join("textures", "insertion_sort.png"))
heap_sort_rect = pygame.image.load(os.path.join("textures", "heap_sort.png"))
selection_sort_rect = pygame.image.load(os.path.join("textures", "selection_sort.png"))

shuffle_image = shuffle_rect.get_rect(topleft=(15, 15))
bubble_sort_image = bubble_sort_rect.get_rect(topleft=(130, 15))
insertion_sort_image = insertion_sort_rect.get_rect(topleft=(245, 15))
heap_sort_image = heap_sort_rect.get_rect(topleft=(360, 15))
selection_sort_image = selection_sort_rect.get_rect(topleft=(475, 15))

algorithms = ["Bubble sort", "Insertion sort", "Selection sort", "Heap sort"]

run = True
while run:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    window.blit(shuffle_rect, (shuffle_image))
    window.blit(bubble_sort_rect, (bubble_sort_image))
    window.blit(insertion_sort_rect, (insertion_sort_image))
    window.blit(heap_sort_rect, (heap_sort_image))
    window.blit(selection_sort_rect, (selection_sort_image))

    start = 0
    for i in range(len(array)):
        pygame.draw.rect(window, (255, 255, 255), (start, SCREEN_HEIGHT - array[i], 3, SCREEN_HEIGHT))
        start += 3
    pygame.display.update()

    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            run = False

        elif event.type == MOUSEBUTTONDOWN:
            if mouse_x > 15 and mouse_y > 15 and mouse_x < 115 and mouse_y < 45:
                random.shuffle(array)
                draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

            elif mouse_x > 130 and mouse_y > 15 and mouse_x < 230 and mouse_y < 45:
                bubble_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

            elif mouse_x > 245 and mouse_y > 15 and mouse_x < 345 and mouse_y < 45:
                insertion_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)
            
            elif mouse_x > 360 and mouse_y > 15 and mouse_x < 460 and mouse_y < 45:
                heap_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

            elif mouse_x > 475 and mouse_y > 15 and mouse_x < 575 and mouse_y < 45:
                selection_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

    pygame.display.update()

pygame.quit()