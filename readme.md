ATM App (Full-Stack Project)

A simple full-stack ATM simulation app built with Flask (Python) and HTML/CSS/JavaScript. 
This project demonstrates backend API handling, frontend-backend integration, and dynamic updates through the Fetch API.

------------------------------------------------------------
🚀 Features
------------------------------------------------------------
✅ View current balance
✅ Withdraw and deposit amounts
✅ Interactive UI connected to Flask backend
✅ Modular and reusable Python logic
✅ Clean and simple frontend

------------------------------------------------------------
🧠 Tech Stack
------------------------------------------------------------
Frontend: HTML, CSS, JavaScript (Fetch API)
Backend: Python, Flask, Flask-CORS
Version Control: Git & GitHub

------------------------------------------------------------
🏗️ Project Structure
------------------------------------------------------------
atm_app/
│
├── app.py                 # Flask backend API
├── atm.py                 # Core ATM logic (balance, withdraw, deposit)
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   ├── style.css          # Optional custom styling
│   └── script.js          # JavaScript functions for API calls
│
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

------------------------------------------------------------
⚙️ Setup & Installation
------------------------------------------------------------
1️⃣ Clone this repository
    git clone https://github.com/<yourusername>/atm_app.git
    cd atm_app

2️⃣ Create a virtual environment
    python -m venv venv

3️⃣ Activate the virtual environment
    Windows:
        venv\Scripts\activate
    macOS/Linux:
        source venv/bin/activate

4️⃣ Install dependencies
    pip install -r requirements.txt

5️⃣ Run the application
    python app.py

Then open your browser and visit: http://127.0.0.1:5000

------------------------------------------------------------
🔌 API Endpoints
------------------------------------------------------------
| Endpoint     | Method | Description                                |
|---------------|---------|--------------------------------------------|
| /             | GET     | Render homepage (HTML)                     |
| /balance      | GET     | Get current balance                        |
| /withdraw     | POST    | Withdraw money (expects JSON {amount})     |
| /deposit      | POST    | Deposit money (expects JSON {amount})      |

------------------------------------------------------------
📈 Future Improvements
------------------------------------------------------------
✨ Add user login and authentication
✨ Store transactions in a database (SQLite or PostgreSQL)
✨ Add transaction history
✨ Deploy on Render or Railway for live demo
✨ Make it mobile responsive using Bootstrap or Tailwind CSS

------------------------------------------------------------
🧑‍💻 Author
------------------------------------------------------------
Bhakti Kulkarni
LinkedIn: https://www.linkedin.com/in/bhaktiskulkarni/
GitHub: https://github.com/bhakti259

------------------------------------------------------------
💡 Learning Outcomes
------------------------------------------------------------
This project helped me strengthen my understanding of:
- REST APIs with Flask
- Frontend-Backend data flow
- Fetch API and JSON handling
- Virtual environments and dependency management
- Git/GitHub project setup and documentation

⭐ If you liked this project, don’t forget to star the repo on GitHub!

