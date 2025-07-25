from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(
            host='db',
            user='root',
            password='root123',
            database='mydb'
        )
        if connection.is_connected():
            return "✅ Connected to MySQL from Flask!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
