import pygame
import time

# Draw array
def draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array):
    pygame.draw.rect(window, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    start = 0
    for i in range(len(array)):
        pygame.draw.rect(window, (255, 255, 255), (start, SCREEN_HEIGHT - array[i], 5, SCREEN_HEIGHT))
        start += 3

    pygame.display.update()

# Bubble sort
def bubble_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array):
    sorted = False 
    while sorted == False: 
        sorted = True 

        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]: 
                sorted = False 
                array[i], array[i + 1] = array[i + 1], array[i] 

            pygame.event.clear()
            draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)
    return array 

# Insertion sort
def insertion_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array):
    for i in range(1, len(array)):
        while i > 0 and array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i -1], array[i]
            i -= 1
            pygame.event.clear()
            draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)
    return array

# Selection sort
def selection_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array):
    for i in range(len(array) - 1):
        min = i
        draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
                time.sleep(0.01)
                pygame.event.clear()
                draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

        if min != i:
            temp = array[i]
            array[i] = array[min]
            array[min] = temp

        draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)

    return array

# Heap sort
def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i])
        heapify(array, n, largest)

def heap_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        heapify(array, i, 0)
        time.sleep(0.01)
        pygame.event.clear()
        draw_array(window, SCREEN_WIDTH, SCREEN_HEIGHT, array)
    return array

def cocktail_sort(window, SCREEN_WIDTH, SCREEN_HEIGHT, array):
	n = len(array)
	swapped = True
	start = 0
	end = n - 1
    
	while (swapped == True):
		swapped = False

		for i in range (start, end):
			if (array[i] > array[i + 1]):
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True

		if (swapped == False):
			break

		swapped = False
		end = end - 1
          
		for i in range(end - 1, start - 1, -1):
			if (array[i] > array[i + 1]):
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True

		start = start + 1