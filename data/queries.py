from data import data_manager


def get_shows(page):

    page_number = int(page)
    data = data_manager.execute_select(
            f'''SELECT * FROM shows ORDER BY rating DESC LIMIT 15 OFFSET {15 * page_number};
                                           ''')
    return data

# def get_pagination():
#     data = data_manager.execute_select(
#         f'''SELECT COUNT (DISTINCT id) FROM shows;
#                                                ''')
#     return data

def tv_show(show_id):
    data =  data_manager.execute_select(
            f'''SELECT * FROM shows WHERE id = {show_id};''')
    return data