from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'rahasia_sejarah_leo'

# Simulasi database
users = {
    'Pembuat': {'password': 'kontolkuda', 'role': 'owner'},
    'leo': {'password': 'leo123', 'role': 'user'},
    'nayla': {'password': 'bucinbanget', 'role': 'user'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        user = users.get(uname)

        if user and user['password'] == pwd:
            session['username'] = uname
            session['role'] = user['role']
            if user['role'] == 'admin':
                return redirect('/admin')
            else:
                return redirect('/user')
        return 'Login gagal. Coba lagi.'

    return render_template('login.html')

@app.route('/owner')
def admin_dashboard():
    if session.get('role') == 'owner':
        return render_template('dashboard_admin.html')
    return redirect('/')

@app.route('/user')
def user_dashboard():
    if session.get('role') == 'user':
        return render_template('dashboard_user.html')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
