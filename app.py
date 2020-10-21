from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


from mid_admin import admin
app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()
