from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # In a real application, you would validate credentials here
        # For now, we'll just redirect to the main page
        return redirect(url_for('main_page'))
    return render_template('login.html')

@app.route('/main')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)