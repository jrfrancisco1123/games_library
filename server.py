from flask import Flask, render_template, redirect, request
from game_model import Game
app = Flask(__name__)
app.secret_key = "secret project"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_started')
def get_started():
    return render_template('add_game.html')

@app.route('/library')
def library():
    games = Game.get_all()
    return render_template('library.html', games = Game.get_all())

@app.route('/show_game/<int:id>')
def show_game(id):
    games = Game.get_one(id)
    return render_template('game_info.html', games = Game.get_one(id))

@app.route('/edit_game/<int:id>')
def edit_game_info(id):
    return render_template('edit_game.html', one_game = Game.get_one(id))

@app.route('/delete_game/<int:id>')
def delete_one_game(id):
    Game.delete(id)
    return redirect('/library')
# <-------------------------------POST------------------------------->

@app.route('/add_game', methods=["POST"])
def add_game():
    print(request.form)
    data = {
        'name': request.form['name'],
        'console': request.form['console'],
        'genre': request.form['genre']
    }
    Game.save(data)
    return redirect('/library')

@app.route('/edit_one_game/<int:id>', methods=['POST'])
def update_game(id):
    print(request.form)
    data = {
        'name': request.form['name'],
        'console': request.form['console'],
        'genre': request.form['genre'],
        'id': id
    }
    Game.update_game(data)
    return redirect('/library')

# <-------------------------------POST------------------------------->

if __name__ == "__main__":
    app.run(debug=True)