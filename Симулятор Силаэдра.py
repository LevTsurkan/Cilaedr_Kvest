import pygame
import os
import time
import random

pygame.mixer.init()

from Функции import (
    GameState,
    start_background_music,
    prihogaya, etag1, etag2, etag3, etag4, etag5,
    c105, ohrana, lestnica, zadniy_dvor, dvor,
    uchitelskaya, c207, c401, tualet, boss, stolovaya, c201
)

state = GameState()                       

print('Добро пожаловать в текстовую квест-игру "Симулятор Силаэдра"!')
print('Здесь вы будете перемещаться по комнатам и постепенно прояснять ситуацию. Пока у вас есть только пропуск. Удачи!')
start_background_music()

while state.location != 'end':         
    loc = state.location
    if loc == 'prihogaya':
        prihogaya(state)          
    elif loc == 'etag1':
        etag1(state)
    elif loc == 'etag2':
        etag2(state)
    elif loc == 'etag3':
        etag3(state)
    elif loc == 'etag4':
        etag4(state)
    elif loc == 'etag5':
        etag5(state)
    elif loc == 'c105':
        c105(state)
    elif loc == 'ohrana':
        ohrana(state)
    elif loc == 'lestnica':
        lestnica(state)
    elif loc == 'zadniy_dvor':
        zadniy_dvor(state)
    elif loc == 'dvor':
        dvor(state)
    elif loc == 'uchitelskaya':
        uchitelskaya(state)
    elif loc == 'c207':
        c207(state)
    elif loc == 'c401':
        c401(state)
    elif loc == 'tualet':
        tualet(state)
    elif loc == 'boss':
        boss(state)
    elif loc == 'stolovaya':
        stolovaya(state)
    elif loc == 'c201':
        c201(state)

print("Конец.")
print("Игру написал Лев Цуркань.")
