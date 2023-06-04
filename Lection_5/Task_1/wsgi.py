from flask import Flask, render_template, redirect, request, url_for
import json

app = Flask(__name__)

user = None   # current user

@app.route('/')
@app.route('/home')
def index():
    return render_template('main.html')

@app.route('/sign', methods=["POST"])
def sign():     # Create user and password on file login_users
    global user

    username = request.form['username']
    password = request.form['psw']
    password_repeat = request.form['psw-repeat']

    with open('data_base/login_users', 'r', encoding='utf8') as file:
        login_dict = json.load(file)
    if username in login_dict.keys():
        error = 'This username was used!'
        return render_template('form_signup.html', rep_username=error)
    elif password != password_repeat:
        error = 'Wrong repeat password!'
        return render_template('form_signup.html', not_repeat=error)
    else:       #right action
        with open('data_base/login_users', 'w', encoding='utf8') as file:
            login_dict[username] = password
            file.write(json.dumps(login_dict))
        user = username
        return render_template('chat.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    global user

    username = request.form['username']
    password = request.form['psw']

    with open('data_base/login_users', 'r', encoding='utf8') as file:
        login_dict = json.load(file)    # Checking user and password
    if username in login_dict.keys():
        for key, value in login_dict.items():
            if username == key and password == value:
                user = username
                return render_template('chat.html')
        else:
            wrong_password = "Invalid password!"
            return render_template('form_login.html', invalid=wrong_password)
    else:
        unknow_name = "Invalid name!"
        return render_template('form_login.html', not_exist=unknow_name)


@app.route('/chat')
def chat():
    with open('data_base/chat_history', 'r', encoding='utf8') as file:
        chat_list = json.load(file)

    return render_template('chat.html', chat_messages=chat_list)

@app.route('/message', methods=['POST'])
def add_item():     # add message in chat
    chat_input = request.form['chat']

    with open('data_base/chat_history', 'r', encoding='utf8') as file:
        chat_list = json.load(file)
        chat_list.append(f"{user}: {chat_input}")
    with open('data_base/chat_history', 'w', encoding='utf8') as file:
        file.write(json.dumps(chat_list))
    return redirect(url_for('chat'))


@app.route('/form_login')
def logIN():
    return render_template('form_login.html')

@app.route('/form_signup')
def signup():
    return render_template('form_signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
