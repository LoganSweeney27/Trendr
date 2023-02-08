from flask import Flask

app = Flask(__name__)

# For defining different pages, this is the home page.
# Currently only using in-line HTML but templates are
# available
@app.route("/")
def homepage():
    return "<h1>Welcome to Trendr!<h1>"

# Use 'python main.py' to run the server and 
# ctrl + click "http://127.0.0.1:5000" to open the page

if __name__ == "__main__":
    app.run()