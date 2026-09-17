import pygame
import os
import time
import random

pygame.mixer.init()

from Функции import (
    GameState, play_background_music, get_choice,
    entrance_hall, floor1, floor2, floor3, floor4, floor5,
    room_105, guard_room, stairs, backyard, courtyard,
    teachers_room, room_207, room_401, bathroom,
    boss_fight, cafeteria, room_201,
    LOCATIONS,
)

state = GameState()

print('Добро пожаловать в текстовую квест-игру "Симулятор Силаэдра"!')
print('Здесь вы будете перемещаться по комнатам и постепенно прояснять ситуацию. Пока у вас есть только пропуск. Удачи!')
play_background_music()

while state.location != "end":
    handler = LOCATIONS.get(state.location)
    if handler:
        handler(state)
    else:
        print("Неизвестная локация. Игра завершается.")
        state.location = "end"

print("Конец.")
print("Игру написал Лев Цуркань.")
