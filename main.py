from flask import *
from data import queries
import os, bcrypt

app = Flask('codecool_series')

app.secret_key = os.urandom(24)

@app.route('/', defaults={'page': 0})
@app.route('/<page>')
def index(page):
    data_user = session['user_id'] if is_user_in() else None
    try:
        page_number = int(page)
    except:
        page_number = 0
    shows = queries.get_shows(page_number)
    return render_template('index.html', shows=shows, page=page_number, data_user=data_user)


@app.route('/design')
def design():
    return render_template('design.html')


# @app.route('/20show')
# def test_page():
#     data = queries.get_20shows()
#     return render_template('20show.html', data=data)


# @app.route('/api/show-actors/<show_id>')
# def get_actors(show_id):
#     data_actors = queries.get_20shows_actors(show_id)
#     return jsonify(data_actors)


# @app.route('/api/delete', methods=['POST'])
# def delete_episode():
#     episode_id = request.json['episodeId']
#     queries.delet_episode(episode_id)


@app.route('/tv-show/<show_id>/<season_id>')
def view_show(show_id, season_id):
    data = queries.tv_show(show_id)
    actors = queries.get_actors(show_id)
    genres = queries.get_genres(show_id)
    table = queries.ex_table(show_id, season_id)
    data_user = session['user_id'] if is_user_in() else None

    # print(table)
    if data[0]['trailer']:
        trailer = data[0]['trailer'].replace('watch?v=', 'embed/', 1)
    else:
        trailer = ''
    return render_template('tv-show.html', data=data, trailer=trailer, actors=actors, genres=genres, table=table, data_user = data_user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/account/register', methods=['GET','POST'])
def account_register():
    if is_user_in():
        return redirect(url_for('index'))

    if request.method == 'POST':
        email_data = request.form['email']
        password_data = hash_password(request.form['password'])
        queries.add_user(email_data, password_data)
        return redirect(url_for('account_login'))
    return render_template('signup.html')



@app.route('/account/login', methods=['GET','POST'])
def account_login():
    if is_user_in():
        return redirect(url_for('index'))

    if request.method == 'POST':
        email_data = request.form['email']
        password_data = request.form['password']
        user = queries.check_user(email_data)

        if  user and verify_password(password_data, user[0]['password']):
            session['user_id'] = user[0]['id']
            session['email'] = user[0]['email']
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('E-mail or Password do not match')
    return render_template('login.html')



@app.route('/account/logout')
def account_logout():
    session.pop('user_id', None)
    session.pop('email', None)
    session.pop('logged_in', None)
    return redirect('/')



@app.route('/api/add-favorite', methods=['POST'])
def add_favorite():
    user_id = session['user_id'] if is_user_in() else None
    episode_id = request.json['episodeId']
    fav_check = queries.check_favourite(user_id,episode_id)
    if not fav_check:
        queries.add_favourite_episodes(user_id,episode_id)
        answer = 'Episode add to favorite'
    else:
        answer = 'Episode is already in favorite'
    return jsonify(answer)

@app.route('/favourite')
def favourite_page():
    data_user = session['user_id'] if is_user_in() else None
    data = queries.get_favourite(data_user)
    return render_template('favourite.html', data=data)


@app.route('/test')
def check_favorite():
    data = queries.check_favourite()
    return render_template('test.html', data = data)

def is_user_in():
    if 'logged_in' in session:
        return True
    return False



def hash_password(text_password):
    hashed_pass = bcrypt.hashpw(text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pass.decode('utf-8')


def verify_password(text_password, hashed_pass):
    return bcrypt.checkpw(text_password.encode('utf-8'), hashed_pass.encode('utf-8'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

