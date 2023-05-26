from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body>
        <h1 style="text-align:center;">Chen Bible</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
