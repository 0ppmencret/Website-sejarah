from flask import Flask, request, redirect, session, render_template_string
import hashlib

app = Flask(__name__)
app.secret_key = 'rahasia_super_amankan_Leo'

# Simulasi database (nanti bisa pakai PostgreSQL, MongoDB, atau SQLite)
users = {
    'admin': hashlib.sha256('superpassword'.encode()).hexdigest()
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/dashboard')
        return 'Login gagal. Coba lagi!'
    return render_template_string('''<form action="/login" method="post">
        <input name="username"><input name="password" type="password">
        <button>Login</button></form>''')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Halo {session['user']}, kamu berhasil login ke Sejarah Leo!"
    return redirect('/login')
