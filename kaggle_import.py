import csv
import psycopg2

username = 'postgres'
password = '111'
database = 'archer_DB_lab#3'

INPUT_CSV_FILE = 'steam.csv'

delete_all = '''
DELETE FROM gamegenres;
DELETE FROM rating;
DELETE FROM game;
'''

query_game = '''
INSERT INTO game (game_id, name_game ,developer, release_date ,  price_for_game)  VALUES (%s, %s, %s, %s, %s)
'''

query_gamegenres = '''
INSERT INTO gamegenres (game_id, genres_name) VALUES (%s, %s)
'''

query_rating = '''
INSERT INTO rating (game_id,date_rating, positive_rating, negative_rating) VALUES (%s, %s, %s, %s)
'''


conn = psycopg2.connect(user=username, password=password, dbname=database)

def find_count(s):
    word_list = s.split()
    for i in word_list:
        if i.isnumeric():
            return i
    return 0


def gamegenres_insert(local_game_id, local_row, local_cur):
    local_genres = local_row.split(';')
    for j in range(0, len(local_genres)):
        local_cur.execute(query_gamegenres, (local_game_id, local_genres[j].strip()))


def game_insert(local_game_id, local_name, local_developer, local_relis_data, price, local_cur):
    local_cur.execute(query_game, (local_game_id, local_name, local_developer, local_relis_data, price))


def rating_insert(local_game_id, local_positive_rating, local_negative_rating, local_cur):
    local_cur.execute(query_rating, (local_game_id, "25.12.2022", local_positive_rating,local_negative_rating))


with conn:
    cur = conn.cursor()
    cur.execute(delete_all)
    with open(INPUT_CSV_FILE, 'r',encoding="UTF-8") as ret:
        reader = csv.DictReader(ret)
        for idx, row in enumerate(reader):
            game_insert(row['appid'], row['name'], row['developer'], row['release_date'], row['price'], cur)
            gamegenres_insert(row['appid'], row['genres'], cur)
            rating_insert(row['appid'], row['negative_ratings'], row['positive_ratings'], cur)
        print("Succesful!!")
    conn.commit()