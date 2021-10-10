import pygame
import sys
import numpy
from dijkstra import create_graph_from_matrix, find_path, dijkstra
import time
import random

pygame.init()
width = 720
height = 720
screen = pygame.display.set_mode((width, height))


def create_screen(size):
    for j in range(size):
        for i in range(size):
            pygame.draw.rect(screen, (0, 0, 0),
                             (int(i * width / size), int(j * height / size), int(width / size), int(height / size)), 1)


def make_border(size):
    squares = []
    for j in range(size):
        for i in range(size):
            squares.append(
                pygame.Rect(int(i * width / size) + 1, int(j * height / size) + 1, int(width / size) - 2,
                            int(height / size) - 2))
    return squares


def random_borders(squares, matrix):
    for i in range(len(squares)):
        r = random.randint(0, 1)
        if r == 1:
            pygame.draw.rect(screen, (0, 0, 0), squares[i])
            matrix[i] = 1
    return matrix


def left_pressed(squares, mx, my, matrix):
    for i in range(len(squares)):
        if squares[i].collidepoint(mx, my):
            pygame.draw.rect(screen, (0, 0, 0), squares[i])
            matrix[i] = 1
    return matrix


def right_pressed(squares, mx, my, begin, end, fs):
    for i in range(len(squares)):
        if squares[i].collidepoint(mx, my) and fs == 0:
            pygame.draw.rect(screen, (84, 240, 178), squares[i])
            begin = i
            fs = 1
        elif squares[i].collidepoint(mx, my) and fs == 1:
            pygame.draw.rect(screen, (242, 105, 105), squares[i])
            end = i
            fs = 2
    return begin, end, fs


def draw_path(squares, path):
    for i in path:
        time.sleep(2 / len(path))
        pygame.draw.rect(screen, (84, 240, 178), squares[i])
        pygame.display.flip()


def main():
    size = 16
    screen.fill((255, 255, 255))
    create_screen(size)
    squares = make_border(size)
    matrix = numpy.zeros(size ** 2)
    matrix = random_borders(squares, matrix)
    begin = 0
    end = 0
    fs = 0

    while True:

        mx, my = pygame.mouse.get_pos()
        event = pygame.event.poll()

        if fs == 2:
            graph = create_graph_from_matrix(size, matrix)
            visits, path = dijkstra(graph, begin)
            draw_path(squares, find_path(path, begin, end))
            fs = 0

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            matrix = left_pressed(squares, mx, my, matrix)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            begin, end, fs = right_pressed(squares, mx, my, begin, end, fs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)

        pygame.display.flip()


main()
