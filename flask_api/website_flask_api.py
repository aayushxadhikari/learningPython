from flask import Flask, request, render_template, redirect, url_for
import random
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('scores.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Generate a random number when the server starts
secret_number = random.randint(1, 100)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    global secret_number, attempts, username
    message = "Enter your name to start the game!"

    if request.method == 'POST':
        if 'username' in request.form:
            # Step 1: User enters the username
            username = request.form.get('username')
            if not username or username.strip() == "":
                message = "Please enter a valid username."
                return render_template('home.html', message=message)
            message = "Guess a number between 1 and 100!"
        elif 'guess' in request.form:
            # Step 2: User submits a guess
            try:
                guess = int(request.form.get('guess'))
                attempts += 1
                if guess < secret_number:
                    message = "Too Low! Try again."
                elif guess > secret_number:
                    message = "Too High! Try again."
                else:
                    message = f"Congratulations, {username}! You guessed it in {attempts} attempts! 🎉"

                    # Save the score
                    save_score(username.strip(), attempts)

                    # Reset the game
                    secret_number = random.randint(1, 100)
                    attempts = 0
                    return redirect(url_for('leaderboard'))
            except ValueError:
                message = "Please enter a valid number."

    return render_template('home.html', message=message)

@app.route('/leaderboard')
def leaderboard():
    scores = fetch_scores()
    return render_template('leaderboard.html', scores=scores)

def save_score(username, score):
    if not username:
        return
    conn = sqlite3.connect('scores.db')
    c = conn.cursor()
    c.execute('INSERT INTO scores (username, score, date) VALUES (?, ?, ?)',
              (username, score, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def fetch_scores():
    conn = sqlite3.connect('scores.db')
    c = conn.cursor()
    c.execute('SELECT username, score, date FROM scores ORDER BY score ASC LIMIT 10')
    scores = c.fetchall()
    conn.close()
    return scores

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
