import sqlite3
DATABASE = 'Games.db'
password = 'qwer1234'

#function
'''print details of all the game in the games table nicely'''
def print_all_game_details():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM game'
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[1;32m%s\033[0m' % f'id          game_name                                           series               maker            genre')
    for game in results:
        print(f'{game[0]:<10}{game[1]:<50}{game[2]:<25}{game[3]:<20}{game[4]:<10}')
    db.close()
    input('\033[1;34;40m%s\033[0m' % 'Press enter to continue.')
    print()

'''print details of genre table'''
def print_genre_table():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM game_genre;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[1;32m%s\033[0m' % f'id      genre_name')
    for genre in results:
        print(f'{genre[0]:<10}{genre[1]:<50}')
    db.close()
    input('\033[1;34;40m%s\033[0m' % 'Press enter to continue.')
    print()

'''print games details of one game 2'''
def print_details_of_one_game():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT id, game_name FROM game;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[1;32m%s\033[0m' % f'id            game_name')
    for search in results:
        print(f'{search[0]:<10}{search[1]:<10}')
    while True:
        # To avoid value error stop the programme
        try:
            id = int(input('\033[1;36;40m%s\033[0m' % 'Please enter the id of the game which you want to search: '))
            sql = 'SELECT * FROM game WHERE id = ?;'
            cursor.execute(sql, (id, ))
            game = cursor.fetchone()
            break
        except ValueError:
            print('\033[1;31;40m%s\033[0m' % 'Invalid enter.')
            cont = input('\033[1;33;40m%s\033[0m' % 'Do you want to continue?(yes/no)') 
            if cont != 'yes':
                break         
    
    if game:
        print(f'Details of the game:')
        print(f'game name: {game[1]}')
        print(f'game maker: {game[2]}')
        print(f'game series: {game[3]}')
        print(f'game genre: {game[4]}')
    db.close()
    input('\033[1;34;40m%s\033[0m' % 'Press enter to continue.')
    print()

def must_contain_number(string):
    return any(letter.isalpha() for letter in string)
def add_other_games():
    while True:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        print_genre_table()
        while True:
            try:
                #To avoid value error stop the programme and make input can't be null
                game_name = input('\033[1;33;40m%s\033[0m' % 'Please enter the name of the game: ')
                if not game_name or not must_contain_number(game_name):
                    print('\033[1;31;40m%s\033[0m' % 'Please enter a valid game name')
                    continue
                game_maker = input('\033[1;33;40m%s\033[0m' % 'Please enter the maker of the game: ')
                if not game_maker or not must_contain_number(game_maker):
                    print('\033[1;31;40m%s\033[0m' % 'Please enter a valid game maker')
                    continue
                game_series = input('\033[1;33;40m%s\033[0m' % 'Please enter the series of the game: ')
                if not game_series or not must_contain_number(game_series):
                    print('\033[1;31;40m%s\033[0m' % 'Please enter a valid game series')
                    continue
                genre_id = input('\033[1;33;40m%s\033[0m' % 'Please enter the genre_id of the game: ')
                try:
                    int(genre_id)
                    if not genre_id:
                        print('\033[1;31;40m%s\033[0m' % 'Please enter genre_id')
                        continue
                except ValueError:
                    print('Please enter a number for id')
                    continue
                #change the data of database
                sql = 'INSERT INTO game (game_name, maker, series, genre_id) VALUES (?, ?, ?, ?);'
                cursor.execute(sql, (game_name, game_maker, game_series, genre_id))
                db.commit()
                print('\033[1;32;40m%s\033[0m' % 'Game added successfully')
                print()
                break  
            except sqlite3.Error:
                break  
        continu = input('\033[1;34;40m%s\033[0m' % 'Do you want to add another game? (yes/no): ')
        if continu.lower() != 'yes':
            break
    db.close()
    input('\033[1;34;40m%s\033[0m' % 'Press enter to continue.')
    print()

def delete_one_game():
    while True:
        print("Don't delete a game unless the data is wrong.")
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = 'SELECT id, game_name FROM game;'
        cursor.execute(sql)
        results = cursor.fetchall()
        print('\033[1;32m%s\033[0m' % f'id            game_name')
        for search in results:
            print(f'{search[0]:<10}{search[1]:<10}')
        try:
            delete = int(input('Please enter the id of the game: '))
            sql = 'DELETE FROM game where id = ?;'
            cursor.execute(sql, (delete,))
            db.commit()
            print('Game deleted successfully!')
            continu = input('\033[1;34m%s\033[0m' % 'Do you want to delete another game?(yes/no) ')
            if continu != 'yes':
               break
            else:
                continue
        except ValueError:
            print('\033[1;34m%s\033[0m' % 'Please enter a number')
            answer = input('Do you want to continue?(yes/no)')   
            if answer != 'yes':
                break         
    db.close()
    input('\033[1;34;40m%s\033[0m' % 'Press enter to continue.')
    print()

def show_games_have_same_series_or_makers(maker_series):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    if maker_series == 'maker':
        choice_maker = input('\033[1;33;40m%s\033[0m' % 'Please enter the maker: ')
        sql = 'SELECT * FROM game WHERE maker = ?;'
        cursor.execute(sql, (choice_maker,))
    if maker_series == 'series':
        choice_series = input('\033[1;33;40m%s\033[0m' % 'Please enter the series: ')
        sql = 'SELECT * FROM game WHERE series = ?;'
        cursor.execute(sql, (choice_series,))
    results = cursor.fetchall()
    if results:
        print('\033[1;32m%s\033[0m' % f'id          game_name                                   maker             series')
        for game in results:
            print(f'{game[0]:<10}{game[1]:<45}{game[2]:<20}{game[3]:<30}')
    else:
        print('\033[1;31m%s\033[0m' % 'No games found.')
    db.close()
    input('\033[1;34m%s\033[0m' % 'Press enter to continue.')
    print()   

'''add a new genre'''
def add_genre():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            genre_name = input('\033[1;33m%s\033[0m' % 'Please enter the name of the genre: ')
            if not genre_name or not must_contain_number(genre_name):
                print('Please enter a genre name')
                continue
        except ValueError:
            print('\033[1;31m%s\033[0m' % 'Invalid input')
        sql = 'INSERT INTO game_genre (genre_name) VALUEs (?);'
        cursor.execute(sql, (genre_name,))
        db.commit()
        print('\033[1;34m%s\033[0m' % 'Genre added succcessfully!')
        answer3 = input('\033[1;34m%s\033[0m' % 'Do you want to continue?(yes/no)')
        if answer3 != 'yes':
            break
        
        input('\033[1;34m%s\033[0m' % 'Press enter to continue.')
        print()
    db.close()

def delete_genre():
    while True:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = 'SELECT genre_id, genre_name FROM game_genre;'
        cursor.execute(sql)
        results = cursor.fetchall()
        change_color5 = f'id            genre'
        print('\033[1;32m%s\033[0m' % change_color5)
        for search in results:
            print(f'{search[0]:<10}{search[1]:<10}')
        try:
            delete = int(input('\033[1;33m%s\033[0m' % 'Please enter the id of the genre: '))
            sql = 'DELETE FROM game_genre where genre_id = ?;'
            cursor.execute(sql, (delete,))
            db.commit()
            print('\033[1;32m%s\033[0m' % 'Genre deleted successfully!')
            continu = input('\033[1;34m%s\033[0m' % 'Do you want to delete another genre?(yes/no) ')
            if continu != 'yes':
               break
            else:
                continue
        except ValueError:
            print('\033[1;31m%s\033[0m' % 'Please enter a number')
            answer = input('\033[1;34m%s\033[0m' % 'Do you want to continue?(yes/no)')   
            if answer != 'yes':
                break         
    db.close()

#main code
while True:
    color_change3 = 'Please enter the password: '
    answer2 = input('\033[1;36;40m%s\033[0m' % color_change3)
    if answer2 == password:
        break
    else:
        print('\033[1;36m%s\033[0m' % 'Please enter the right password')
        
while True:
    change_color4 = '''
Which function do you want to use?
1.Print Table games 
2.Print details of one game
3.Add other games
4.Delete games
5.Print data by makers
6.Print data by series
7.Print Table genre
8.Add a genre
9.Delete a genre
10.Break
Please enter the number
'''
    try:
        answer = int(input('\033[1;36;40m%s\033[0m' % change_color4))
        print()
        if answer == 1:
            print_all_game_details()
        if answer == 2:
            print_details_of_one_game()
        if answer == 3:
            add_other_games()
        if answer == 4:
            delete_one_game()
        if answer == 5:
            show_games_have_same_series_or_makers('maker')
        if answer == 6:
            show_games_have_same_series_or_makers('series')
        if answer == 7:
            print_genre_table()
        if answer == 8:
            add_genre()
        if answer == 9:
            delete_genre()
        if answer == 10:
            break
    except ValueError:
        print('\033[1;31m%s\033[0m' % 'Please enter a number between 1 and 10')
        conti = input('\033[1;32;40m%s\033[0m' % 'Press enter to continue.')
