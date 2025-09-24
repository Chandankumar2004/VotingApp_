# 🗳️ VotingApp

_A Real-Time Online Voting Application built with Flask, SocketIO & SQLite_

<p align="center">
  <img src="frontend/static/images/bjp-removebg-preview.png" alt="Logo" height="80">
  <img src="frontend/static/images/congress-removebg-preview.png" alt="Logo" height="80">
  <img src="frontend/static/images/rjd-removebg-preview.png" alt="Logo" height="80">
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-Backend-black?logo=flask" alt="Flask"></a>
  <a href="https://socket.io/"><img src="https://img.shields.io/badge/Socket.IO-RealTime-lightgrey?logo=socket.io" alt="SocketIO"></a>
  <a href="https://www.sqlite.org/"><img src="https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite" alt="SQLite"></a>
</p>

---

## 🌟 Features

✅ **User Authentication** – Simple login with a username  
✅ **Vote Casting** – Users can cast a single vote for their preferred party  
✅ **Live Results** – Real-time updates of vote counts using SocketIO  
✅ **Dynamic Party Ranking** – Parties automatically reorder based on current votes  
✅ **Detailed Votes View** – Breakdown of individual votes (voter, party, date, time)  
✅ **Admin Reset** – Admin can reset all votes with one click  
✅ **Responsive Design** – Clean, user-friendly interface

---

## 🛠️ Tech Stack

| Layer          | Technology                                   |
| -------------- | -------------------------------------------- |
| **Backend**    | Flask, Flask-SocketIO                        |
| **Database**   | SQLite (`votes.db`)                          |
| **Frontend**   | HTML, CSS, JavaScript (AJAX + Socket.IO)     |
| **Deployment** | Localhost (default: `http://127.0.0.1:5000`) |

---

## 🚀 How It Works

- **Backend (Flask)**  
  Handles authentication, vote submission, SQLite storage, API endpoints, and broadcasts vote updates to all clients in real-time.

- **Frontend (HTML/CSS/JS)**  
  Provides login, voting, and results pages. Uses JavaScript to fetch & display live vote data and dynamically reorders parties.

---

## 📦 Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Chandankumar2004/VotingApp_.git
cd VotingApp_

# 2️⃣ Create & activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Initialize the database (auto-created on first run)
```

---

## ▶️ Running the App

```bash
# Start the Flask server
python server.py
```

Open your browser and navigate to 👉 `http://127.0.0.1:5000/`

## 🖥️ Usage Guide

> ### 1️⃣ Login Page
>
> 📝 **Action:** Enter a username to log in.  
> 🔄 **Already Voted?** You'll be redirected to the results page.
>
> ![Login Page](https://github.com/Chandankumar2004/VotingApp_/blob/90539b34c5e2c5bc852604eef59541980a74e00c/login.png)

---

> ### 2️⃣ Vote Page
>
> 📝 **Action:** Cast your vote for one of the available parties.
>
> ![Vote Page](https://github.com/Chandankumar2004/VotingApp_/blob/90539b34c5e2c5bc852604eef59541980a74e00c/vote.png)

---

> ### 3️⃣ Results Page
>
> 📝 **View:** Live voting results.  
> 🏆 **Highlight:** The party with the most votes automatically appears at the top.
>
> ![Results Page](https://github.com/Chandankumar2004/VotingApp_/blob/90539b34c5e2c5bc852604eef59541980a74e00c/result.png)

---

> ### 4️⃣ Detailed Votes
>
> 📝 **Action:** Click **"View Detailed Votes"** to see a table of individual votes  
> 👀 **Details shown:** Voter name, party, date & time.
>
> ![Detailed Votes](https://github.com/Chandankumar2004/VotingApp_/blob/90539b34c5e2c5bc852604eef59541980a74e00c/vote_details.png)

---

> ### 🔄 Admin Reset
>
> 📝 **Feature:** "Reset All Votes" button (visible by default) lets the admin clear all votes.  
> ⚠️ **Safety:** A confirmation prompt appears before resetting.

## 📂 Project Structure

```
VotingApp_/
├── README.md
├── server.py
├── requirements.txt
├── database/
│   └── votes.db
└── frontend/
    ├── login.html
    ├── results.html
    ├── vote.html
    └── static/
        ├── css/
        │   └── style.css
        ├── images/
        │   ├── bjp-removebg-preview.png
        │   ├── congress-removebg-preview.png
        │   └── rjd-removebg-preview.png
        └── js/
            ├── results.js
            └── vote.js
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

> ⚡ _Enjoy seamless, real-time voting with Flask, Socket.IO, and SQLite!_

---

## 👨💻 Author

**Chandan Kumar Chaurasiya**

- 📧 [chandan32005c@gmail.com](mailto:chandan32005c@gmail.com)
- 🔗 [LinkedIn](https://www.linkedin.com/in/chandan2004)
- 💻 [GitHub](https://github.com/Chandankumar2004)
- 🌐 [Portfolio](https://chandan-portfolio-tau.vercel.app/)

---
