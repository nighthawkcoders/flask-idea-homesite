"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" PYTHON ONLY """


def python_details():
    return {"title": 'CSP: Python', 'key': 'python'}


def python_ap():
    route = "python-ap"
    title = "AP study big ideas outline"
    timeline = "https://padlet.com/embed/k3bwade11ekevmum"
    data = {"route": route, "title": title, "timeline": timeline}
    return data


def python_hello():
    route = "python-hello"
    title = "Hello to Project-based learning and Python"
    timeline = "https://padlet.com/embed/2p9700yyoz3flccs"
    repo = "https://gh-card.dev/repos/nighthawkcoders/pythonhello.svg"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Python-Hello-Series?lite=true"
    data = {"route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_flask():
    route = "python-flask"
    title = "Flask Web server introduction and ideas"
    timeline = "https://padlet.com/embed/onshvns8f7vrrn2l"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-portfolio.svg?link_target=_blank"
    repo_description = "Ideas for building a Flask Web Server."
    repl = "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?lite=true"
    data = {"route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_cbproj():
    route = "python-cbproj"
    title = "College Board project preparation focus"
    timeline = "https://padlet.com/jmortensen7/cspcbproject"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-homesite.svg?link_target=_blank"
    repo_description = "Start process of building a project for College Board. Use my website or previous projects as " \
                       "idea starters. "
    data = {"route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def python_study():
    route = "python-study"
    title = "Python study resources"
    padlet = "https://padlet.com/jmortensen7/csp2021"
    data = {"route": route, "title": title, "padlet": padlet}
    return data


def python_database():
    route = "pythondb_bp.databases"
    title = "Hello to Databases and Python"
    data = {"route": route, "title": title}
    return data


def python_restapi():
    route = "restapi_bp.index"
    title = "REST API examples"
    data = {"route": route, "title": title}
    return data


def python_projects():
    return [python_hello(), python_flask(), python_cbproj(), python_ap(), python_study(), python_database(),
            python_restapi()]
