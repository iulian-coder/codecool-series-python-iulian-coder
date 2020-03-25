from data import data_manager



# def get_20shows():
#     data = data_manager.execute_select(
#         f''' SELECT shows.id, shows.title, COUNT(episodes.id) as numar_episoade from shows
#         INNER JOIN seasons on shows.id = seasons.show_id INNER JOIN episodes ON seasons.id = episodes.season_id
#         GROUP BY shows.id, shows.title
#         ORDER BY numar_episoade DESC
#         LIMIT 20
#     ;''')
#     return data
#
# def get_20shows_actors(show_id):
#     data = data_manager.execute_select(
#         f''' SELECT shows.id, shows.title, actors.id as nr_actori, actors.name FROM shows
#         LEFT JOIN show_characters sc on shows.id = sc.show_id
#         LEFT JOIN actors on sc.actor_id = actors.id
#         WHERE shows.id = {show_id}
# ;''')
#     return data


def get_shows(page_number):
    data = data_manager.execute_select(
        f'''SELECT DISTINCT shows.id, shows.title, shows.year, shows.runtime, shows.trailer, shows.homepage, shows.rating, first_value(genres.name) OVER (PARTITION BY shows.id) 
            FROM shows 
            INNER JOIN show_genres ON shows.id = show_genres.show_id
            INNER JOIN genres ON show_genres.genre_id=genres.id
            GROUP BY shows.title, shows.id, shows.year, shows.runtime, shows.trailer, shows.homepage, shows.rating, genres.name
            ORDER by shows.rating DESC
            LIMIT 15 OFFSET {15 * page_number}; 
                                           ''')
    return data


# Tv show Page Queries

def tv_show(show_id):
    data = data_manager.execute_select(
        f'''SELECT shows.id, shows.title as name, shows.runtime, shows.year, shows.trailer, shows.overview, seasons.season_number, seasons.title
            FROM shows INNER JOIN seasons ON shows.id = seasons.show_id
            WHERE shows.id = {show_id}
    ;''')
    return data


def get_actors(show_id):
    data = data_manager.execute_select(
        f''' SELECT shows.id, actors.name FROM shows 
    LEFT JOIN show_characters ON show_characters.show_id = shows.id LEFT JOIN actors ON actors.id = show_characters.actor_id
    WHERE shows.id = {show_id}
    ;''')
    return data


def get_genres(show_id):
    data = data_manager.execute_select(
        f''' SELECT shows.id, shows.title, g.name as genres FROM shows 
      LEFT JOIN show_genres sg on shows.id = sg.show_id LEFT JOIN genres g on sg.genre_id = g.id
      WHERE shows.id = {show_id}
    ;''')
    return data


def ex_table(show_id, season_id):
    data = data_manager.execute_select(f'''
    SELECT seasons.title as season, e.title, e.episode_number as episode, shows.runtime, e.id FROM seasons 
    INNER JOIN shows ON seasons.show_id = shows.id INNER JOIN episodes e on seasons.id = e.season_id
    WHERE shows.id = {show_id} AND seasons.season_number = {season_id}
;''')
    return data


#
# def delet_episode(episode_id):
#     data = data_manager.execute_select(
#         f''' DELETE FROM episodes WHERE episodes.id = {episode_id}
# ;''')
#     return data

def add_user(user_email, user_password):
    data_manager.execute_select_special(
        f'''INSERT INTO users ( email, password) 
            VALUES ( '{user_email}', '{user_password}');''')


def check_user(user_email):
    data = data_manager.execute_select(
        f''' SELECT id, email, password FROM users WHERE email ='{user_email}';'''
    )
    return data

def add_favourite_episodes(user_id, episodes_id):
    data_manager.execute_select_special(
        f''' INSERT INTO favourites (user_id, episodes_id) VALUES ('{user_id}', '{episodes_id}')
;'''
    )

def get_favourite(user_id):
    data = data_manager.execute_select(
        f''' SELECT users.id, favourites.episodes_id, episodes.title, seasons.title as sezon, shows.title as name FROM users 
        JOIN favourites ON users.id = favourites.user_id
        JOIN episodes ON favourites.episodes_id = episodes.id 
        JOIN seasons ON episodes.season_id = seasons.id
        JOIN shows ON seasons.show_id = shows.id
        WHERE users.id = {user_id}
;''')
    return data