from flask import Flask, render_template, request, redirect
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MySQL Connection
def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset=os.getenv("DB_CHARSET", "utf8"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/", methods=["GET", "POST"])
def index():
    search_id = request.args.get("search_id", "")
    selected = None

    # Handle update form
    if request.method == "POST":
        record_id = request.form.get("record_id")
        feedback = request.form.get("feedback", "")
        note = request.form.get("note", "")
        action = request.form.get("action", "")

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE register_data SET feedback=%s, note=%s, action=%s WHERE id=%s
                """, (feedback, note, action, record_id))
                conn.commit()

    # Fetch all records
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM register_data")
            records = cursor.fetchall()

    # Search and select record
    if search_id:
        try:
            search_id = int(search_id)
            selected = next((r for r in records if r['id'] == search_id), None)
        except ValueError:
            selected = None

    if not selected and records:
        selected = records[0]

    return render_template("index.html", records=records, selected=selected, search_id=search_id)

@app.route("/add", methods=["POST"])
def add():
    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "location": request.form["location"],
        "degree": request.form["degree"],
        "mobile": request.form["mobile"],
        "email": request.form["email"]
    }

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO register_data (id, name, location, degree, mobile, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (data["id"], data["name"], data["location"], data["degree"], data["mobile"], data["email"]))
            conn.commit()

    return redirect("/?search_id=" + str(data["id"]))

if __name__ == "__main__":
    app.run(debug=True)
