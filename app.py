from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
messages = []
global loggedIn
loggedIn = False



# Pages
@app.route('/')
def index():
    return render_template('view.html', messages=messages)

@app.route('/view')
def view_messages():
    return render_template('view.html', messages=messages)

@app.route('/about', methods=['GET', 'POST'])
def about():
    """
       
        loggedIn = False
        if request.method == 'POST':
            if request.form.get('clear') == 'clear':
                messages.clear()
                loggedIn = True
            elif  request.form.get('action2') == 'VALUE2':
                print("AZIONE 2")
                loggedIn = True
            else:
                pass
        elif request.method == 'GET':
            return render_template('about.html')
            
    
        return render_template("about.html")
    """
    return render_template("about.html")



# API per aggiornamento AJAX
@app.route('/get_messages')
def get_messages():
    return jsonify(messages[::-1])  # Messaggi in ordine inverso (più recente in alto)



# Handlers user
@app.route('/handle_data', methods=['POST'])
def handle_data():
    message = request.form['message']
    if len(message) < 140:
        messages.append(message)
        print(message)
    return redirect(url_for('view_messages'))

@app.route('/handle_refresh', methods=['POST'])
def handle_refresh():
    return redirect(url_for('view_messages'))


        


#########
##ADMIN##
#########

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    global loggedIn
    if loggedIn == True:        
        loggedIn = False
        if request.method == 'POST':
            if request.form.get('clear') == 'clear':
                messages.clear()
                loggedIn = True
            elif  request.form.get('action2') == 'VALUE2':
                print("AZIONE 2")
                loggedIn = True
            else:
                pass
        elif request.method == 'GET':
            return render_template('admin.html')
            
    
        return render_template("admin.html")
    else:
        return redirect(url_for('login'))

@app.route('/clear_messages')
def clear_messages():
    
    return redirect(url_for('view_messages'))


#admin heandler



@app.route('/login', methods=['GET', 'POST'])
def login():
    global loggedIn
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            loggedIn = False
            return render_template('login.html', error=error)
        else:
            loggedIn = True
            return redirect(url_for('admin_page'))
           


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
