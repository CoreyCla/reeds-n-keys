from flask import Flask, render_template, request, make_response, jsonify


app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/contact_form', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        print(request.form['last_name'])
        print(request.form['first_name'])
        print(request.form['email'])
        print(request.form['inst-type'])
        print(request.form['description'])

        return render_template('thanks.html')
    else:
        return render_template('contact.html')


if __name__ == "__main__":
    app.run()
