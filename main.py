import psycopg2

username = 'postgres'
password = '111'
database = 'archer_DB_lab#3'

query_1 = '''
SELECT trim(game.name_game)as game_name, rating.positive_rating,rating.negative_rating from game,rating
where game.game_id = rating.game_id and game.game_id<1000
'''

query_2 = '''
SELECT TRIM(genres_name) as gamegenres, 
COUNT(genres_name) FROM gamegenres
JOIN game USING(game_id) 
GROUP BY genres_name
'''

query_3 = '''
SELECT trim(name_game),price_for_game from game
WHERE price_for_game>20
'''

conn = psycopg2.connect(user = username, password = password, dbname = database)

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    print('1.\n')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('2.\n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('3.\n')
    cur.execute(query_3)
    for row in cur:
        print(row)