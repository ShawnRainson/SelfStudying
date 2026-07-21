def movie_catalog():
    movies = {}
    while True:
        try:
            print('Menu:\n' \
            '1. Add movie\n' \
            '2. Show all movies\n' \
            '3. Find movie\n' \
            '4. Delete movie\n' \
            '5. Show best rate movie\n' \
            '6. Show movie by genre\n' \
            '7. Updete movie rating\n' \
            '8. Title part search movie\n' \
            '9. Exit')
            choice = int(input('Choose menu option (1-9): '))
            if choice == 1:
                mov_params = {}
                mov_title = input('Enter movie title: ')
                mov_year = int(input('Enter movie year: '))
                mov_params["year"] = mov_year
                mov_genre = input('Enter movie genre: ')
                mov_params["genre"] = mov_genre
                mov_rating = float(input('Enter movie rate: '))
                mov_params['rating'] = mov_rating
                movies[mov_title] = mov_params
            elif choice == 2:
                if not movies:
                    print('Movie list is empty!')
                else:
                    for mov, op in movies.items():
                        show_movie(mov, op)
            elif choice == 3:
                title = input('Enter movie title for search: ')
                title = title.lower()
                found = False
                for mov, op in movies.items():
                    if title == mov.lower():
                        found = True
                        show_movie(mov, op)
                        break
                if not found:
                    print('Movie not found!')
            elif choice == 4:
                for mov, op in movies.items():
                    show_movie(mov, op)
                delete_mov = input('Choose movie for delete: ')
                if delete_mov not in movies:
                    print('Movie not found')
                else:
                    del movies[delete_mov]
                    print('Movie was delete!')
            elif choice == 5:
                best_rate = -1
                for mov, rate in movies.items():
                    if rate["rating"] > best_rate:
                        best_rate = rate["Rating"]
                        best_mov = mov
                print(f'Title: {best_mov}\nRate: {best_rate}')
            elif choice == 6:
                genre_movie = input('Enter movie genre: ')
                genre_movie = genre_movie.lower()
                found_genre = False
                for mov, genre in movies.items():
                    if genre["genre"].lower() == genre_movie:
                        print(f"Movie: {mov}")
                        found_genre = True
                if not found_genre:
                    print('List has no movie with this genre!')
            elif choice == 7:
                movie_title = input('Enter movie title: ')
                movie_title = movie_title.lower()
                found = False
                for mov_title, old_rating in movies.items():
                    if mov_title.lower() == movie_title:
                        found = True
                        new_rating = float(input(f'Enter new rating for {mov_title}: '))
                        old_rating['rating'] = new_rating
                        print('Rating changes was saved!')
                        break
                if not found:
                    print("Movie not found!") 
            elif choice == 8:
                part_of_title = input('Enter part of title: ')
                part_of_title = part_of_title.lower()
                fount = False
                for title in movies:
                    lower_title = title.lower()
                    if part_of_title in lower_title:
                        print(f'Title: {title}')
                        found = True
                if not found:
                    print("Movie not found!")
            elif choice == 9:
                print('Bye-bye!')
                break
            else:
                print('Invalid option!')
        except ValueError:
            print('Invalid value!')

def show_movie(title, movie):
    print(f'Movie title: {title}')
    print(f'Year: {movie["year"]}\nGenre: {movie["genre"]}\nRating: {movie["rating"]}')

movie_catalog()


   


