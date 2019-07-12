from flask import Flask

app = Flask(__name__)

@app.route('/') #homepage
def index():
    return 'This is homepage.'

if __name__ == "__main__":
    app.run(debug=True) #start this app