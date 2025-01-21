from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Generate a random number when the server starts
secret_number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    message = "Guess a number between 1 and 100!"
    if request.method == 'POST':
        try:
            # Get the user's guess from the form
            guess = int(request.form.get('guess'))
            global secret_number
            
            # Check the guess
            if guess < secret_number:
                message = "Too Low! Try again."
            elif guess > secret_number:
                message = "Too High! Try again."
            else:
                message = "Congratulations! You guessed the number! 🎉"
                # Regenerate the number for a new game
                secret_number = random.randint(1, 100)
        except ValueError:
            message = "Please enter a valid number."

    # Render the HTML template
    return render_template('home.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
