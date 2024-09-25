from flask import Flask, send_from_directory
from supabase import create_client, Client
import os

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')


# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://***.supabase.co')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'your-supabase-key')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        return send_from_directory('static/uploads', filename)
    except FileNotFoundError:
        return "File not found", 404


from app import routes
