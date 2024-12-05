from app import create_app
import logging

app = create_app()

# Set log level
app.logger.setLevel(logging.DEBUG)

# Add a file handler
file_handler = logging.FileHandler('flask.log')
file_handler.setLevel(logging.DEBUG)

# Define log format
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)

# Add the handler to the Flask logger
app.logger.addHandler(file_handler)


if __name__ == '__main__':
    app.logger.info("Application started.")
    app.run(debug=True)
