from rosemary import create_app

if __name__ == '__main__':
    app = create_app(__name__)
    app.run(port=7070, host="0.0.0.0")
