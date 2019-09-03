from flask import Flask, render_template, request, make_response, jsonify


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

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
            return render_template('thanks.html')
        else:
            return render_template('contact.html')

    return app
