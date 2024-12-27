import logging
from flask import Flask
from flask_restful import Api

from .models.database import initialize_database
from .api.routes import initialize_routes

#########################
### APPLICATION SETUP ###
#########################
app = Flask(__name__)

######################
### DATABASE SETUP ###
######################
initialize_database(app)

#####################
### LOGGING SETUP ###
#####################
logging.basicConfig(
    level=logging.DEBUG,  # Set the default log level (e.g., DEBUG, INFO, WARNING, ERROR)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.StreamHandler(),  # Log to the console
        logging.FileHandler('flask.log')  # Also log to a file named 'app.log'
    ]
)

####################
### ROUTES SETUP ###
####################
api = Api(app)
initialize_routes(api)
