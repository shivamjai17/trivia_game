# Trivia Game - Guess the Destination!

## 🏆 Overview
This is a fun and interactive **Django-powered Trivia Game** where users guess travel destinations based on given clues. Players can challenge their friends, track scores, and learn fun facts about various places!

## 🎯 Features
- **Guess the Destination**: Users receive clues and choose the correct destination from multiple options.
- **Score Tracking**: The game tracks the number of correct and incorrect answers per user.
- **Fun Facts**: After each guess, a fun fact about the correct destination is displayed.
- **"Challenge a Friend" Feature**:
  - Users register with a unique username before inviting friends.
  - Generates a dynamic shareable image with an invite link.
  - Friends can see the invitee’s score before playing.
  - Anyone with the invitation link can play the game.
- **Session-Based Score Storage**: Scores are stored per session to track the user's progress.
- **CSRF Protection**: Implemented for secure API interactions.

---

## 🚀 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shivamjai17/trivia_game.git
cd trivia-game
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```bash
python manage.py migrate
```

### 5️⃣ Start the Server
```bash
python manage.py runserver
```

Access the game at: **http://127.0.0.1:8000/**

---

## 🛠 API Endpoints

### 1️⃣ Get CSRF Token
- **Endpoint**: `/get_csrf_token/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "csrfToken": "your_token_here"
  }
  ```

### 2️⃣ Fetch Random Clues
- **Endpoint**: `/get_random_clues/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "clues": ["Famous for its beaches", "Has a famous Christ statue"],
      "options": ["Paris", "Rio de Janeiro", "Tokyo", "New York"],
      "correct_answer": "Rio de Janeiro",
      "fun_fact": "Rio's Christ the Redeemer is one of the New Seven Wonders of the World."
  }
  ```

### 3️⃣ Check Answer
- **Endpoint**: `/check_answer/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "user_answer": "Sam",
      "correct_answer": "Rio de Janeiro"
  }
  ```
- **Response (Correct Answer)**:
  ```json
  {
      "result": "correct",
      "message": "🎉 Correct! Well done!",
      "animation": "confetti",
      "fun_fact": "Rio's Christ the Redeemer is one of the New Seven Wonders of the World.",
      "score": {"correct": 1, "incorrect": 0}
  }
  ```

### 4️⃣ Challenge a Friend
- **Endpoint**: `/challenge_friend/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "player1"
  }
  ```
- **Response**:
  ```json
  {
      "invite_link": "http://127.0.0.1:8000/play?invite=player1"
  }
  ```

---

## 📂 Project Structure
```
trivia-game/
│-- game/
│   │-- migrations/
│   │-- static/
│   │-- templates/game/
│   │   │-- home.html
│   │-- views.py
│   │-- models.py
│   │-- urls.py
│-- static/
│-- templates/
│-- manage.py
│-- README.md
│-- requirements.txt
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 💡 Future Enhancements
- Add a **Leaderboard** to show the top players.
- Implement **different difficulty levels**.
- Add **hints** for difficult questions.

---

## 🎉 Enjoy the game & challenge your friends! 🏆

