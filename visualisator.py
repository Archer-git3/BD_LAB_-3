import psycopg2
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

username = 'postgres'
password = '111'
database = 'archer_DB_lab#3'


query_1 = '''
SELECT trim(game.name_game)as game_name, rating.positive_rating,rating.negative_rating from game,rating
where game.game_id = rating.game_id
'''

query_2 = '''
SELECT TRIM(genres_name) as gamegenres, 
COUNT(genres_name) FROM gamegenres
JOIN game USING(game_id) 
GROUP BY genres_name
'''

query_3 = '''
SELECT trim(name_game),price_for_game from game
WHERE price_for_game>70
'''

conn = psycopg2.connect(user = username, password = password, dbname = database)


with conn:
    print("Database opened successfully")
    cur = conn.cursor()


    print('1.\n')
    cur.execute(query_1)
#
    periods = []
    positive = []
    negative = []
    plt.xticks(rotation=10)
    i=0
    for row in cur:
        i+=1
        if i==20:
            break
        periods.append(row[0])
        positive.append(row[1])
        negative.append(row[2])

    data_names = periods
    data_values_n = negative
    data_values_p = positive


    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 9})

    plt.title('співідношення рейтингу ігор')

    ax = plt.axes()
   # ax.xaxis.grid(True, zorder=1)

    xs = range(len(data_names))

    plt.barh([x + 0.3 for x in xs], data_values_p,
             height=0.2, color='red', alpha=0.7, label='Позитивні',
             zorder=2)
    plt.barh([x + 0.05 for x in xs], data_values_n,
             height=0.2, color='blue', alpha=0.7, label='негативні',
             zorder=2)
    plt.yticks(xs, data_names, rotation=0)

    plt.legend(loc='upper right')
    plt.show()


    print('2.\n')
    cur.execute(query_2)
    periods = []
    p_count = []
    explode = []
    for row in cur:
        explode.append(0.08)
        periods.append(row[0])
        p_count.append(row[1])
    p_count=list(p_count)
    plt.pie(p_count, explode=explode, labels=periods, autopct='%1.1f%%')
    #plt.pie.set_title('Частка фільмів кожного жанру')

    plt.show()
#
    def bulba(list,name):
        sorted = True
        lent = len(list)
        for i in range(lent - 1):
            sorted = True
            for j in range(lent - (i + 1)):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    name[j], name[j + 1] = name[j + 1], name[j]
                    sorted = False
            if sorted:
                break
        return list,name
    print('3.\n')
    cur.execute(query_3)
##
    periods = []
    p_count = []
    plt.xticks(rotation=10)
    for row in cur:
        periods.append(row[0])
        p_count.append(row[1])
    bulba(p_count,periods)
    sns.lineplot(x = periods, y = p_count)
    plt.show()