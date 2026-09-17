import pygame
import os
import time
import random
from Функции import (location, propusk, key35O, start_background_music, prihogaya, etag1, etag2, etag3, etag4, etag5, c105, ohrana, lestnica, zadniy_dvor, dvor, uchitelskaya, c207, c401, tualet, boss, stolovaya, c201)
pygame.mixer.init()
print('Добро пожаловать в текстовую квест-игру "Симулятор Силаэдра"!')
print('Здесь вы будете перемещаться по комнатам и постепенно прояснять ситуацию. Пока у вас есть только пропуск. Удачи!')
start_background_music()
while location != 'end':
    if location=='prihogaya':
        prihogaya()
    if location=='etag1':
        etag1()
    if location=='etag2':
        etag2()
    if location=='etag3':
        etag3()
    if location=='etag4':
        etag4()
    if location=='etag5':
        etag5()
    if location=='c105':
        c105()
    if location=='ohrana':
        ohrana()
    if location=='lestnica':
        lestnica()
    if location=='zadniy_dvor':
        zadniy_dvor()
    if location=='dvor':
        dvor()
    if location=='uchitelskaya':
        uchitelskaya()
    if location=='c207':
        c207()
    if location=='c401':
        c401()
    if location=='tualet':
        tualet()
    if location=='boss':
        boss()
    if location=='stolovaya':
        stolovaya()
    if location=='c201':
        c201()
print("Конец.")
print("Игру написал Лев Цуркань.")

