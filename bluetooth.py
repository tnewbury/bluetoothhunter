#!/usr/bin/python

import pygame
import ConfigParser
import sys
from sys import exit
import os


def ConfigSectionMap(section):
    dict1 = {}
    options = btres.options(section)
    for option in options:
        try:
            dict1[option] = btres.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1




pygame.init()



screen = pygame.display.set_mode((1024,768))

#print ConfigSectionMap("00:00:00:00:00:00")['rssi']


bgcolor = (75,75,255)
circlecolour = (255,255,255)

running=True

while running:

	
	balls = os.system('/home/trev/dev/python/btfix.sh')
	btres = ConfigParser.ConfigParser()
	btres.read("/home/trev/dev/python/bt.txt")


	


	screen.fill(bgcolor)
	
	devices = btres.sections()
	
	for device in range(len(devices)):
		
		size = abs((int(ConfigSectionMap(devices[device])['rssi']))) * 4
		pygame.draw.circle(screen, circlecolour, (550,550), size, 1)
		#pygame.draw.circle(screen, circlecolour, (550,500), '67', 1)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)


