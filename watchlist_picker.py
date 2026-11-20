import pandas as pd
import random

watchlist = pd.read_csv("watchlist.csv")
movie_list = {}
random_movies = []

for movie, year, link in zip(watchlist['Name'], watchlist['Year'], watchlist['Letterboxd URI']):
    movie_list[movie] = year, link

def ask_again():
    while True:
        answer = str(input("Would you like to sort it out again? ")).lower().strip()
        if answer == "no":
            print("Thank you for using Watchlist Random Picker!")
            return False
        elif answer == "yes":
            return True
        else:
            print("Please, answer using 'yes' or 'no'.")

print("Welcome to the Watchlist Random Picker!")
while True:
    value = input("How many movies would you like to sort out of your watchlist? ")
    if not value.isdigit() or not len(list(movie_list.keys())) >= int(value) > 0 :
        print(f"Please enter a number between 1 and {len(list(movie_list.keys()))} (your watchlist length)")
        continue
    random_movies = random.sample(list(movie_list.keys()), k=int(value))

    if int(value) == 1:
        year, link = movie_list[random_movies[0]]
        print(f"Your movie is {random_movies[0]} ({year}) - {link}")
    elif int(value) > 1:
        print(f"Your movies are: ")
        for title in random_movies:
            year, link = movie_list[title]
            print(f"- {title} - ({year}) - {link}")

    if not ask_again():
        break