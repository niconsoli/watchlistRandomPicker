import pandas as pd
import random

watchlist = pd.read_csv("watchlist.csv")
movie_list = []
random_movies = []

# VERSION USING ARRAYS INSTEAD OF DICTIONARIES
# Does not show year nor link

for movie in watchlist['Name']:
    movie_list.append(movie)

def ask_again():
    while True:
        answer = str(input("Would you like to sort it out again? ")).lower().strip()
        if answer == "no":
            print("Thank you for using Watchlist Random Picker!")
            return False
        elif answer == "yes":
            random_movies.clear()
            return True
        else:
            print("Please, answer using 'yes' or 'no'.")

while True:
    value = input("How many movies would you like to sort out of your watchlist? ")

    if not value.isdigit() or not len(watchlist) > int(value) > 0 :
        print(f"Please enter a number between 1 and {len(movie_list)} (your watchlist length)")
        continue
    if int(value) > 1:
        random_movies = random.sample(movie_list, k=int(value))
    elif int(value) == 1:
        random_movies.append(random.choice(movie_list))
    elif int(value) <= 0:
        print("Please, enter a valid value.")

    if int(value) == 1:
        print(f"Your movie is {random_movies[0]}")
    elif int(value) > 1:
        print(f"Your movies are: ")
        for i in range(len(random_movies)):
            print(f"- {random_movies[i]}")

    if not ask_again():
        break