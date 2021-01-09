"""Driver for Web server"""

from views import app

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5001')
