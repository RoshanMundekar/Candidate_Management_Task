# 🧑‍💼 Candidate Management System

A web-based Candidate Management System built with **Flask**, **Tailwind CSS**, and **MySQL**. It allows you to manage candidate records with full Create, Read, Update, and Delete (CRUD) functionality.

---

## ✅ Frontend Stack

| Layer         | Tool/Library     | Purpose                               |
|---------------|------------------|----------------------------------------|
| UI Framework  | Tailwind CSS     | Utility-first responsive styling       |
| Template      | Jinja2 (Flask)   | Render dynamic content in HTML         |
| Modal/Dialog  | Custom JS        | Modal logic for add/edit form          |
| Input Forms   | HTML5 + Tailwind | User input and data submission         |

---

## ✅ Backend Stack

| Layer        | Tool/Library     | Purpose                                          |
|--------------|------------------|--------------------------------------------------|
| Web Framework| Flask            | Lightweight Python web server                    |
| Templating   | Jinja2           | For dynamic HTML rendering                       |
| DB Access    | PyMySQL          | To connect to MySQL DB using Python              |
| Env Config   | python-dotenv    | Load DB credentials securely from `.env` file    |
| DB Server    | MySQL/MariaDB    | Persistent database backend                      |

---


---

📹 **Demo Video**  
[Download or Watch Video](assets/demo.mp4)

---

## 📁 Project Setup

1. Clone the repository:
```bash
git clone https://github.com/RoshanMundekar/Candidate_Management_Task.git
cd Candidate_Management_Task
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure `.env` with your MySQL credentials:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=candidates_db
```

5. Run the application:
```bash
flask run
```

---

## 📂 Folder Structure

```
Candidate_Management_Task/
├── app.py
├── templates/
├── static/
│   ├── css/ (Tailwind)
│   └── js/  (Custom modal logic)
├── assets/       # Screenshots & videos
├── .env          # Environment configuration (not pushed)
├── requirements.txt
└── README.md
```

---

## 📃 License

MIT License