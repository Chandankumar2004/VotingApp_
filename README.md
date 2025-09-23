# VotingApp_Python

A real-time online voting application built with Flask, SocketIO, and SQLite. This application allows users to log in, cast their votes for different parties, view live results, and see detailed vote breakdowns. An admin can also reset all votes.

## Features

*   **User Authentication:** Simple login with a username.
*   **Vote Casting:** Users can cast a single vote for their preferred party.
*   **Real-time Results:** Live updates of vote counts using SocketIO.
*   **Dynamic Party Ordering:** Parties in the results page are automatically reordered based on their current vote count (highest first).
*   **Detailed Vote View:** See a breakdown of individual votes, including voter name, party choice, date, and time.
*   **Admin Reset Functionality:** An admin can reset all votes, clearing the database.
*   **Responsive Design:** Basic styling for a user-friendly experience.

## How it Works

The application consists of a Flask backend and a simple HTML/CSS/JavaScript frontend.

*   **Backend (Flask):**
    *   Manages user sessions and authentication.
    *   Handles vote submission and storage in an SQLite database (`votes.db`).
    *   Provides API endpoints for fetching current vote counts and detailed vote information.
    *   Uses Flask-SocketIO to broadcast real-time vote updates to all connected clients.
*   **Frontend (HTML, CSS, JavaScript):**
    *   Displays login, voting, and results pages.
    *   Uses JavaScript to interact with the Flask backend via AJAX calls and SocketIO.
    *   Listens for `vote_update` events from the server to refresh results in real-time.
    *   Dynamically reorders party display on the results page based on vote counts.

## Setup and Installation

To set up and run the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd VotingApp_Python
    ```
    (Assuming you are already in the project root `c:\Users\chand\Downloads\VotingApp_Python\VotingApp_Python`)

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv backend/venv
    # On Windows:
    .\backend\venv\Scripts\activate
    # On macOS/Linux:
    # source backend/venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Initialize the database:**
    The application uses SQLite, and the database will be created automatically if it doesn't exist. You can ensure it's set up by running the server once.

## How to Run

1.  **Start the Flask backend server:**
    Make sure your virtual environment is activated (as shown in step 2 of Setup).
    ```bash
    python backend/server.py
    ```
    The server will typically start on `http://127.0.0.1:5000/`.

2.  **Access the application:**
    Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Usage

### 1. Login Page
Enter a username to log in. If you have already voted in a previous session, you will be redirected to the results page.

**Screenshot: Login Page**
![Login Page](screenshots/login.png)
*(Please replace `screenshots/login.png` with your actual screenshot)*

### 2. Vote Page
After logging in, you can cast your vote for one of the available parties.

**Screenshot: Vote Page**
![Vote Page](screenshots/vote.png)
*(Please replace `screenshots/vote.png` with your actual screenshot)*

### 3. Results Page
View live voting results. The party with the most votes will appear at the top.

**Screenshot: Results Page**
![Results Page](screenshots/results.png)
*(Please replace `screenshots/results.png` with your actual screenshot)*

### 4. Detailed Votes
Click the "View Detailed Votes" button to see a table of individual votes, including the voter's name, party choice, date, and time.

**Screenshot: Detailed Votes**
![Detailed Votes](screenshots/vote_details.png)
*(Please replace `screenshots/vote_details.png` with your actual screenshot)*

### Admin Reset
The "Reset All Votes" button is now visible by default on the results page. Clicking it will clear all votes from the database. A confirmation prompt will appear before resetting.

## Project Structure

```
VotingApp_Python/
├───README.md
├───backend/
│   ├───config.py
│   ├───requirements.txt
│   ├───server.py
│   └───venv/
├───database/
│   ├───votes.db
│   └───voting_app.sql
├───frontend/
│   ├───login.html
│   ├───results.html
│   ├───vote.html
│   └───static/
│       ├───css/
│       │   └───style.css
│       ├───images/
│       │   ├───bjp-removebg-preview.png
│       │   ├───congress-removebg-preview.png
│       │   └───rjd-removebg-preview.png
│       └───js/
│           ├───results.js
│           └───vote.js
└───instance/
    ├───test.txt
    └───votes.db
```
