from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from mysql.connector import Error
import hashlib

app = Flask(__name__, template_folder='templates')

app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'online_voting_system'
}

# Initialize a dictionary to store vote counts
vote_counts = {
    'Candidate 1': 0,
    'Candidate 2': 0,
    'Candidate 3': 0,
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print("Error:", e)
        return None

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle user register logic here
        # Redirect to the login page after successful register
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle user login logic here
        # Redirect to the vote page after successful login
        return redirect(url_for('vote'))

    return render_template('login.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_candidate = request.form.get('candidate')
        if selected_candidate in vote_counts:
            # Update the vote count for the selected candidate
            vote_counts[selected_candidate] += 1

            # Redirect to the results page after casting a vote
            return redirect(url_for('results'))

    return render_template('vote.html')

@app.route('/results')
def results():
    # Fetch and display voting results here
    # Pass the vote_counts dictionary to the template
    return render_template('results.html', vote_counts=vote_counts)

@app.route('/logout')
def logout():
    # Your logout logic here
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
