#!/usr/bin/python

import pygame
import pymongo
import sys
from sys import exit
import os

from pymongo import MongoClient


#####db stuff
client = MongoClient('192.168.1.149', 27017)
db = client.bt_db
collection = db.bt_db
posts = db.posts
prenode = ""

####screen init

screen = pygame.display.set_mode((1024,768))
pygame.init()
bgcolor = (75,75,255)
circlecolour = (255,255,255)


print posts.find().count()
running = True



while running:
		screen.fill(bgcolor)
		devlist = posts.find()
		
		for devices in devlist:
			locy = 400
			size = abs(int(devices['rssi'])) * 4
			#print devices['node']
			
			if devices['node'] != prenode :
				locx = 500
				circlecolour = (255,100,100)
			else:
				locx = 500 - int(noderssi) * 4
				circlecolour = (100,255,100)
		
			pygame.draw.circle(screen, circlecolour, (locx,locy), size,1)
		
		pygame.display.update()
		prenode = devices['node']
		noderssi = devices['rssi']

		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
		
		
