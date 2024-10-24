
# Task 1: Your Mood Tracker

import random

moods = ["happy", "said", "energetic", " calm" ]

the_week_days = ["Monday","Tusday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

time_of_the_day = ["Morning","Afternoon", "Evening"]


for day in the_week_days :
    for time in time_of_the_day : 
        mood = random.choice(moods)
        time = random.choice(time_of_the_day)
    print (f"on {day} {time}, you were feeling {mood}.")
