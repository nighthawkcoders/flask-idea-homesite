"""
1. This file enable execution of WSGI server
2. The routes for Web server comes from views additions to app
"""

from views import app

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5001')
