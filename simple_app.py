from flask import Flask, request, jsonify, session, redirect
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'voting-secret'

# In-memory storage for simplicity
votes = {}
users = {}

@app.route('/')
def home():
    return '''
    <html>
    <body>
        <h1>Voting App</h1>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Enter your name" required>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok'}, 200

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session_id = str(uuid.uuid4())
    session['username'] = username
    session['session_id'] = session_id
    return redirect('/vote')

@app.route('/vote')
def vote():
    if 'username' not in session:
        return redirect('/')
    
    return f'''
    <html>
    <body>
        <h1>Vote for your party, {session["username"]}!</h1>
        <form method="POST" action="/cast_vote">
            <input type="radio" name="party" value="BJP" required> BJP<br>
            <input type="radio" name="party" value="Congress"> Congress<br>
            <input type="radio" name="party" value="RJD"> RJD<br>
            <button type="submit">Vote</button>
        </form>
        <a href="/results">View Results</a>
    </body>
    </html>
    '''

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    if 'session_id' not in session:
        return redirect('/')
    
    party = request.form['party']
    session_id = session['session_id']
    
    if session_id in votes:
        return "Already voted!"
    
    votes[session_id] = party
    return redirect('/results')

@app.route('/results')
def results():
    tally = {'BJP': 0, 'Congress': 0, 'RJD': 0}
    for vote in votes.values():
        if vote in tally:
            tally[vote] += 1
    
    result_html = f'''
    <html>
    <body>
        <h1>Live Results</h1>
        <p>BJP: {tally["BJP"]}</p>
        <p>Congress: {tally["Congress"]}</p>
        <p>RJD: {tally["RJD"]}</p>
        <a href="/vote">Back to Vote</a>
        <br><a href="/">Logout</a>
    </body>
    </html>
    '''
    return result_html

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)