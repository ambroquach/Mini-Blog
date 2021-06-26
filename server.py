# Creating app instance using Connexion instead of Flask
# from flask import (
#     Flask,
#     render_template
# )
# app = Flask(__name__, template_folder="templates")
from flask import render_template
# import connexion

# local modules
import config

# Create the application instance
# app = connexion.App(__name__, specification_dir='./')
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yml')


# Create a URL route in our application for "/"
@connex_app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=True)
