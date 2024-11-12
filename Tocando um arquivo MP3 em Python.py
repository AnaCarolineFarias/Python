import pygame
import os

print("Diretório de trabalho atual:", os.getcwd())
pygame.mixer.init()
pygame.mixer.music.load('C:\Users\ana.farias\Desktop\Python Projetos\LP.mp3')
pygame.mixer.music.play()

input("Aperte Espaço para parar a reprodução...")
pygame.mixer.music.stop()
