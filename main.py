import sys
from main2 import mach_coor
import requests
import os
import pygame


def map(zoom):
    toponym_to_find = " ".join(sys.argv[1:])
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=mach_coor(json_response, zoom))

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


zoom = 16
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map(zoom)), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                zoom += 1
                if zoom >= 21:
                    zoom = 20
            if event.key == pygame.K_PAGEDOWN:
                zoom -= 1
                if zoom <= 10:
                    zoom = 10
    screen.blit(pygame.image.load(map(zoom)), (0, 0))
    pygame.display.flip()
pygame.quit()
os.remove(map(zoom))
