from flask import render_template,Flask

# app = Flask(__name__,static_url_path='/foo')

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/aa')
# def index():
#     return app.send_static_file('index.html')

# if __name__ == '__main__':
#     app.run()

# if __name__ == '__main__':
#     app.run(debug=True)


'''
基本流程
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
'''