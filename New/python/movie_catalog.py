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
            '6. Exit')
            choice = int(input('Choose menu option (1-6): '))
            if choice == 1:
                mov_title = input('Enter movie title: ')
                mov_year = int(input('Enter movie year: '))
                mov_ganre = input('Enter movie ganre: ')
                mov_rate = float(input('Enter movie rate: '))
                movies[mov_title] = [mov_year, mov_ganre, mov_rate]
            elif choice == 2:
                if not movies:
                    print('Movie list is empty!')
                else:
                    for mov, op in movies.items():
                        print(f'Movie title: {mov}')
                        print(f'Year: {op[0]}\nGanre: {op[1]}\nRate: {op[2]}')
            elif choice == 3:
                title = input('Enter movie title for search: ')
                title = title.lower()
                found = False
                for mov, op in movies.items():
                    if title == mov.lower():
                        found = True
                        print(f'Movie title: {mov}')
                        print(f'Year: {op[0]}\nGanre: {op[1]}\nRate: {op[2]}')
                        break
                if not found:
                    print('Movie not found!')
            elif choice == 4:
                for mov, op in movies.items():
                    print(f'Movie title: {mov}')
                    print(f'Year: {op[0]}\nGanre: {op[1]}\nRate: {op[2]}')
                delete_mov = input('Choose movie for delete: ')
                del movies[delete_mov]
                print('Movie was delete!')
            elif choice == 5:
                best_rate = 0.0
                for mov, rate in movies.items():
                    if rate[2] > best_rate:
                        best_rate = rate[2]
                        best_mov = mov
                print(f'Title: {best_mov}\nRate: {best_rate}')
            elif choice == 6:
                print('Bye-bye!')
                break
            else:
                print('Invalid option!')
        except ValueError:
            print('Invalid value!')

movie_catalog()


   


