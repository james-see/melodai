
Twinkle_List = ['c4','c4','g4','g4','a4','a4','g4',
				'f4','f4','e4','e4','d4','d4','c4',
				'g5','g5','f4','f4','e4','e4','d4',
				'g5','g5','f4','f4','e4','e4','d4',
				'c4','c4','g4','g4','a4','a4','g4',
				'f4','f4','e4','e4','d4','d4','c4'
    ]

from threading import Thread
import pygame as pg 
import time
import os


from threading import Thread
import pygame as pg 
import time 

pg.mixer.init()
pg.init()
pg.mixer.set_num_channels(len(Twinkle_List))


def play_notes(notePath,duration):
	time.sleep(duration) # make a pause 
	pg.mixer.Sound(notePath).play()
	time.sleep(duration) # Let the sound play 
	print(notePath) # To see which note is now playing


path  = 'Sounds/'

cnt =1	# A counter to delay once a line is finished as there
# are 6 total lines
th = {}


# for t in Twinkle_List:
# 	th[t] = Thread(target = play_notes,args = (path+'{}.wav'.format(t),0.3))
# 	# These are arguments (path+'{}.wav'.format(t),0.3)
# 	# Lets start the thread
# 	th[t].start()
# 	th[t].join()
# 	if cnt%7==0:
# 		print("---Long Pause---")
# 		time.sleep(1) # Let the sound play for the last note of each line
		
# 	cnt+=1


def load_sound(sound_filename, directory):
    """load the sound file from the given directory"""
    fullname = os.path.join(directory, sound_filename)
    sound = pg.mixer.Sound(fullname)
    return sound

e = load_sound("e4.wav", 'Sounds/')
c = load_sound("c4.wav", 'Sounds/')
g = load_sound("g4.wav", 'Sounds/')
pg.mixer.Channel(0).play(c)
pg.mixer.Channel(1).play(g)
pg.mixer.Channel(2).play(e)
pg.time.wait(3000)
