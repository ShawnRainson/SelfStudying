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
            '7. Exit')
            choice = int(input('Choose menu option (1-7): '))
            if choice == 1:
                mov_params = {}
                mov_title = input('Enter movie title: ')
                mov_year = int(input('Enter movie year: '))
                mov_params["Year"] = mov_year
                mov_genre = input('Enter movie ganre: ')
                mov_params["Genre"] = mov_genre
                mov_rating = float(input('Enter movie rate: '))
                mov_params['Rating'] = mov_rating
                movies[mov_title] = mov_params
            elif choice == 2:
                if not movies:
                    print('Movie list is empty!')
                else:
                    for mov, op in movies.items():
                        print(f'Movie title: {mov}')
                        print(f'Year: {op["Year"]}\nGenre: {op["Genre"]}\nRating: {op["Rating"]}')
            elif choice == 3:
                title = input('Enter movie title for search: ')
                title = title.lower()
                found = False
                for mov, op in movies.items():
                    if title == mov.lower():
                        found = True
                        print(f'Movie title: {mov}')
                        print(f'Year: {op["Year"]}\nGenre: {op["Genre"]}\nRating: {op["Rating"]}')
                        break
                if not found:
                    print('Movie not found!')
            elif choice == 4:
                for mov, op in movies.items():
                    print(f'Movie title: {mov}')
                    print(f'Year: {op["Year"]}\nGenre: {op["Genre"]}\nRating: {op["Rating"]}')
                delete_mov = input('Choose movie for delete: ')
                if delete_mov not in movies:
                    print('Movie not found')
                else:
                    del movies[delete_mov]
                    print('Movie was delete!')
            elif choice == 5:
                best_rate = 0.0
                for mov, rate in movies.items():
                    if rate["Rating"] > best_rate:
                        best_rate = rate["Rating"]
                        best_mov = mov
                print(f'Title: {best_mov}\nRate: {best_rate}')
            elif choice == 6:
                genre_movie = input('Enter movie genre: ')
                genre_movie = genre_movie.lower()
                found_genre = False
                for mov, genre in movies.items():
                    if genre["Genre"].lower() == genre_movie:
                        print(f"Movie: {mov}")
                        found_genre = True
                if not found_genre:
                    print('List has no movie with this genre!')
            elif choice == 7:
                print('Bye-bye!')
                break
            else:
                print('Invalid option!')
        except ValueError:
            print('Invalid value!')

movie_catalog()


   


