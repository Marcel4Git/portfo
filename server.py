from flask import Flask, url_for, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')


#create a dynamic way to create new routes

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#create a function that writes to a file

# def write_to_file(data):
#     with open(r'C:\Users\marcel.hovsepian\Desktop\webserver\database.txt', mode = 'a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open(r'C:\Users\marcel.hovsepian\Desktop\webserver\database.csv', newline='', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database)
        csv_writer.writerow([email, subject, message])

#create a request object to capture data sent through the form.

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went really wrong. Try again. '











# ======================================================
# creating routes by copying and pasting each route
# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# ======================================================

# Creating variable names using the flask docs

# @app.route('/<username>')
# def add_username(username=None):
#     return render_template('index.html', name=username)

# @app.route('/<int:post_id>')
# def add_post_num(post_id =None):
#     return render_template('index.html', post=post_id)
# ========================================================