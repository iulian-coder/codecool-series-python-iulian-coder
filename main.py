from flask import *
from data import queries

app = Flask('codecool_series')


@app.route('/', defaults={'page': 0})
@app.route('/<page>')
def index(page):
    try:
        page_number = int(page)
    except:
        page_number = 0
    shows = queries.get_shows(page_number)
    # print(shows)
    return render_template('index.html', shows=shows , page=page_number)


@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/tv-show/<show_id>')
def view_show(show_id):
    data = queries.tv_show(show_id)
    print(data)
    if data[0]['trailer']:
        trailer = data[0]['trailer'].replace('watch?v=', 'embed/', 1)
    else:
        trailer = ''
    return render_template('tv-show.html', data=data, trailer=trailer)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

# seriesdb