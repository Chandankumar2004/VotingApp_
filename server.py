from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
import os
from datetime import datetime

app = Flask(__name__, static_folder='frontend/static', template_folder='frontend')
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Database Models
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    choice = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Vote {self.choice} by {self.username}>'

@app.before_request
def before_request():
    if 'session_id' not in session and request.endpoint not in ['login', 'static']:
        if request.path != url_for('login_page'):
            return redirect(url_for('login_page'))

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    if username:
        session['username'] = username
        if 'session_id' not in session:
            import uuid
            session['session_id'] = str(uuid.uuid4())
        existing_vote = Vote.query.filter_by(session_id=session['session_id']).first()
        if existing_vote:
            return redirect(url_for('results_page'))
        return redirect(url_for('vote_page'))
    return redirect(url_for('login_page'))

@app.route('/vote')
def vote_page():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return render_template('vote.html', username=session['username'])

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    if 'username' not in session or 'session_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401

    username = session['username']
    session_id = session['session_id']
    choice = request.form['option']

    existing_vote = Vote.query.filter_by(session_id=session_id).first()
    if existing_vote:
        return jsonify({'success': False, 'message': 'You have already voted.'}), 400

    new_vote = Vote(session_id=session_id, username=username, choice=choice)
    db.session.add(new_vote)
    db.session.commit()

    socketio.emit('vote_update', _get_results_data())
    return jsonify({'success': True, 'message': 'Vote cast successfully!'})

@app.route('/results')
def results_page():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return render_template('results.html', username=session['username'])

def _get_results_data():
    votes = Vote.query.all()
    tally = {'BJP': 0, 'RJD': 0, 'Congress': 0}
    for vote in votes:
        if vote.choice in tally:
            tally[vote.choice] += 1
    return tally

@app.route('/get_results')
def get_results():
    return jsonify(_get_results_data())

@app.route('/get_detailed_votes')
def get_detailed_votes():
    votes = Vote.query.all()
    detailed_votes = [{'username': vote.username, 'choice': vote.choice, 'created_at': vote.created_at.strftime('%Y-%m-%d %H:%M:%S')} for vote in votes]
    return jsonify(detailed_votes)

@app.route('/reset_votes', methods=['POST'])
def reset_votes():
    try:
        num_deleted = Vote.query.delete()
        db.session.commit()
        socketio.emit('vote_update', _get_results_data())
        return jsonify({'success': True, 'message': f'{num_deleted} votes reset successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('vote_update', _get_results_data())

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login_page'))

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True, port=5000)