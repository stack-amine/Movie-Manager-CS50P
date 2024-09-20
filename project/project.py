"""
my edX username: MM_2407_4DVD
my GitHub username: @stack-amine
"""
import csv
import sys
import os
import emoji
from tabulate import tabulate
from fuzzywuzzy import process, fuzz

def main():
    valid_genre = [
        'action', 'adventure', 'comedy', 'drama', 'horror', 'thriller',
        'science fiction', 'sci-fi', 'fantasy', 'romance', 'mistery',
        'animation','documentary','musical', 'crime', 'historical',
        'western', 'war', 'family', 'biography', 'sports'
    ]
    while True:
        print("\n Welcome to the Movie Manager!\n")
        print("1. Load all movies")
        print("2. Add a movie")
        print("3. View top-rated movies")
        print("4. Search movies")
        print("5. Remove a movie")
        print("6. exit\n")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            print("\nAll Movies:\n")
            print(load_movies())

        elif choice == '2':
            while True:
                movie_title = input("Enter movie name: ").strip()
                if movie_title:
                    break
                else:
                    print("Movie name cannot be empty")
            while True:
                movie_genre = input("Enter movie genre: ").strip().lower()
                if movie_genre in valid_genre:
                    break
                else:
                    print(f"Invalid genre, choose a valid genre like: {','.join(valid_genre[:5])}...")
            while True:
                try:
                    movie_rating = float(input("Enter movie rating: ").strip())
                    if 0.0 <= movie_rating <= 5.0:
                        break
                    else:
                        print("Rating must be between 0 and 5")
                except ValueError:
                    print("Invalid input, please enter a number between 0 and 5")
            print(add_movie(movie_title, movie_genre, movie_rating))
        elif choice == '3':
            print("\nTop 5 rated movies\n")
            print(view_top_rated())
        elif choice == '4':
            while True:
                search_criterion = input("Search by title or genre: ").strip().lower()
                if search_criterion in ['title', 'genre']:
                    break
                else:
                    print("\nInvalid option, please choose 'title' or 'genre'\n")
            while True:
                search_term = input(f"Enter {search_criterion} to search for: ").strip().lower()
                if search_term:
                    break
                else:
                    print(f"\n{search_criterion} cannot be empty.\n")
            if search_movies(search_criterion, search_term):
                print(search_movies(search_criterion, search_term))
            else:
                print(f"No matches found for the given {search_criterion}: {search_term}")
        elif choice == '5':
            while True:
                movie_to_remove= input("Enter title to remove: ").strip().lower()
                if movie_to_remove:
                    break
                else:
                    print("Title cannot be empty\n")
            print(remove_movie(movie_to_remove))
        elif choice == '6':
            print(emoji.emojize("\nExiting the program, Goodbye:waving_hand:!\n"))
            sys.exit()
        else:
            print("Invalid choice, please choose a valid option")


def convert_rating_to_stars(rating):
    num_stars = round(float(rating))
    return emoji.emojize(':star:') * num_stars

def load_movies():
    try:
        with open('movie.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            movies = []
            for row in reader:
                if row:
                    row[2] = convert_rating_to_stars(row[2])
                    movies.append(row)

            if not movies:
                return "No movies found"
            else:
                headers = ['Title', 'Genre', 'rating']
                return tabulate(movies, headers=headers, tablefmt="presto")
    except FileNotFoundError:
        return "the CSV does not exist"
    except:
        return "An error occurred while loading the movies"


def add_movie(movie_title, movie_genre, movie_rating):
    try:
        file_exists = os.path.isfile("movie.csv")
        with open("movie.csv", "a", newline='') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["title", "genre", "rating"])

            writer.writerow([movie_title, movie_genre, movie_rating])
            return f"\n{emoji.emojize(f"'{movie_title}' added successfully:partying_face:")}"

    except:
        return "An error occurred while adding the movie"

def view_top_rated():
    try:
        with open("movie.csv", "r") as file:
            reader = csv.reader(file)
            movies = []
            next(reader)

            for row in reader:
                if len(row) < 3:
                    continue
                title, genre, rating = row[0], row[1], float(row[2])
                movies.append({'title': title, 'genre': genre, 'rating': rating})

            if not movies:
                return "No movies found, please add movies first"
            else:
                sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)
                top_movies = sorted_movies[:5]
                headers = ['Title', 'Genre', 'Rating']
                table = []
                for movie in top_movies:
                    stars = convert_rating_to_stars(movie['rating'])
                    table.append([movie['title'], movie['genre'], stars])
                return tabulate(table, headers=headers, tablefmt="presto")
    except FileNotFoundError:
        return "the CSV file does not exist"
    except:
        return "An error occured while viewing movies"

def search_movies(search_criterion, search_term):
    try:
        with open("movie.csv", "r") as file:
            reader = csv.reader(file)
            movies = []
            header = next(reader)

            for row in reader:
                if row:
                    title, genre, rating = row[0], row[1], float(row[2])

                    if search_criterion == 'title':
                        match = fuzz.partial_ratio(search_term, title.lower())
                    else:
                        match = fuzz.partial_ratio(search_term, genre.lower())

                    if match > 80:

                        stars = convert_rating_to_stars(rating)
                        movies.append({'title': title, 'genre': genre, 'rating': stars})

            if not movies:
                return None
            else:
                headers = ['Title', 'Genre', 'Rating']
                table = [[movie['title'], movie['genre'], movie['rating']] for movie in movies]
                return f"\n{tabulate(table, headers=headers, tablefmt='presto')}"

    except FileNotFoundError:
        return "the CSV file does not exist"
    except:
        return "An error occured while searching movies"


def remove_movie(movie_to_remove):
    try:
        movies = []
        movie_found = True
        with open("movie.csv", 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if row and row[0].strip().lower() != movie_to_remove:
                    movies.append(row)
                else:
                    movie_found = True

        if not movie_found:
            print(f'Movie "{movie_to_remove}" not found')
        else:
            with open("movie.csv", 'w') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(movies)

            return f"\n{movie_to_remove} has been removed!\n"

    except FileNotFoundError:
        return "The CSV file does not exist"
    except:
        return "An error occurred while removing the movie"


if __name__ == "__main__":
    main()
