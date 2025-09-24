from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
from datetime import datetime

app = Flask(__name__, static_folder='frontend/static', template_folder='frontend')
app.config['SECRET_KEY'] = 'voting-app-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    choice = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    if username:
        session['username'] = username
        session['session_id'] = str(uuid.uuid4())
        existing_vote = Vote.query.filter_by(session_id=session['session_id']).first()
        if existing_vote:
            return redirect('/results')
        return redirect('/vote')
    return redirect('/')

@app.route('/vote')
def vote_page():
    if 'username' not in session:
        return redirect('/')
    return render_template('vote.html', username=session['username'])

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    choice = request.form['option']
    existing_vote = Vote.query.filter_by(session_id=session['session_id']).first()
    if existing_vote:
        return jsonify({'success': False, 'message': 'Already voted'}), 400
    
    new_vote = Vote(session_id=session['session_id'], username=session['username'], choice=choice)
    db.session.add(new_vote)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Vote cast successfully!'})

@app.route('/results')
def results_page():
    if 'username' not in session:
        return redirect('/')
    return render_template('results.html', username=session['username'])

@app.route('/get_results')
def get_results():
    votes = Vote.query.all()
    tally = {'BJP': 0, 'RJD': 0, 'Congress': 0}
    for vote in votes:
        if vote.choice in tally:
            tally[vote.choice] += 1
    return jsonify(tally)

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
        return jsonify({'success': True, 'message': f'{num_deleted} votes reset successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)