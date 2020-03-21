from data import data_manager




def get_20shows():
    data = data_manager.execute_select(
        f''' SELECT shows.id, shows.title, COUNT(seasons.show_id) as sezoane from shows INNER JOIN seasons on shows.id = seasons.show_id
      WHERE shows.id = 1390
    GROUP BY shows.id, shows.title
    ;''')
    return data

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
    data =  data_manager.execute_select(
            f'''SELECT shows.id, shows.title as name, shows.runtime, shows.year, shows.trailer, shows.overview, seasons.title
            FROM shows INNER JOIN seasons ON shows.id = seasons.show_id
            WHERE shows.id = {show_id}
    ;''')
    return data

def get_actors(show_id):
    data = data_manager.execute_select(
        f''' SELECT shows.id, actors.name FROM shows LEFT JOIN show_characters ON show_characters.show_id = shows.id LEFT JOIN actors ON actors.id = show_characters.actor_id
    WHERE shows.id = {show_id}
    ;''')
    return data

def get_genres(show_id):
    data = data_manager.execute_select(
        f''' SELECT shows.id, shows.title, g.name as genres FROM shows LEFT JOIN show_genres sg on shows.id = sg.show_id LEFT JOIN genres g on sg.genre_id = g.id
      WHERE shows.id = {show_id}
    ;''')
    return data