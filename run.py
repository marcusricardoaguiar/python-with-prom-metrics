from app import app

if __name__ == '__main__':
    app.logger.info("Application started.")
    app.run(host='0.0.0.0', port=5000)
