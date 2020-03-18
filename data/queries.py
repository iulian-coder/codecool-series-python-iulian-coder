from data import data_manager


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


def tv_show(show_id):
    data =  data_manager.execute_select(
            f'''SELECT {show_id}, shows.title, shows.trailer, seasons.title AS seasons
            FROM shows INNER JOIN seasons ON shows.id = seasons.show_id
            LIMIT 15
    ;''')
    return data

