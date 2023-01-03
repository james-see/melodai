
Twinkle_List = ['c4','c4','g4','g4','a4','a4','g4',
				'f4','f4','e4','e4','d4','d4','c4',
				'g5','g5','f4','f4','e4','e4','d4',
				'g5','g5','f4','f4','e4','e4','d4',
				'c4','c4','g4','g4','a4','a4','g4',
				'f4','f4','e4','e4','d4','d4','c4'
    ]

letterarray = ["a", "c", "d", "e", "g"]
numberarray = ["1", "2", "3", "4", "5", "6", "7"]



from threading import Thread
import pygame as pg 
import time
import os
import random


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


def select_wav(count=3):
    i = 0
    filenames = []
    while i < count:
        filenames.append(f"{random.choice(letterarray)}{random.choice(numberarray)}.wav")
        i = i + 1
    return filenames

# seed a set of 5 chords to use in song
notesdict = {}
i = 0
while i < 5:
    notesdict[i] = select_wav(3)
    i = i + 1

# make a random length song with random sustain of each chord from seed chords
res = random.sample(range(1, 50), random.choice(range(5, 20)))
print(f"length of song: {len(res)}")
for samp in res:
    notes = notesdict[random.choice(range(0, len(notesdict)))]
    for i, item in enumerate(notes):
        print(f"Note: {item.split('.')[0]}")
        pg.mixer.Channel(i).play(load_sound(item, "Sounds"))
    pg.time.wait(random.choice(range(100, 4000)))
