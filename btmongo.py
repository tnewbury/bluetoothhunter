#!/usr/bin/python

import pymongo
import ConfigParser
import sys
from sys import exit
import os
from pymongo import MongoClient
import datetime
import subprocess
from subprocess import call


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



#database shonk
client = MongoClient('192.168.1.149', 27017)
db = client.bt_db
collection = db.bt_db
posts = db.posts
post = {} #dictionary init




#print ConfigSectionMap("00:00:00:00:00:00")['rssi']


running=True



while running:

#read bluetooth stuff	
	balls = os.system('/home/trev/dev/python/btfix.sh')
	btres = ConfigParser.ConfigParser()
	btres.read("/home/trev/dev/python/bt.txt")
	localadd = os.popen("bluez-test-adapter address").read()
	#print localadd
	
	
#do the result into array, loop array and draw circle
	devices = btres.sections()

	
	for device in range(len(devices)):
		

		key = {'who': ConfigSectionMap(devices[device])['address'], 'node': localadd}
		data = {"$set": {'rssi': ConfigSectionMap(devices[device])['rssi'], 'node': localadd}}
		posts.update(key, data, True)
		
		size = abs((int(ConfigSectionMap(devices[device])['rssi']))) * 4
		





