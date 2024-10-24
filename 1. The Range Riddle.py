
# Task 1: Your Mood Today 

import random

moods = ["happy", "said", "energetic", " calm" ]

the_week_days = ["Monday","Tusday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for day in the_week_days :
    mood = random.choice(moods)
    print (f"on {day}, you were feeling {mood}.")

