"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" PYTHON ONLY """


def python_ap():
    group = "python"
    route = ".pythonap"
    title = "AP study big ideas outline"
    timeline = "https://padlet.com/embed/k3bwade11ekevmum"
    data = {"group": group, "route": route, "title": title, "timeline": timeline}
    return data


def python_hello():
    group = "python"
    route = ".pythonhello"
    title = "Hello to Project-based learning and Python"
    timeline = "https://padlet.com/embed/2p9700yyoz3flccs"
    repo = "https://gh-card.dev/repos/nighthawkcoders/pythonhello.svg"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Python-Hello-Series?lite=true"
    data = {"group": group, "route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_flask():
    group = "python"
    route = ".pythonflask"
    title = "Flask Web server introduction and ideas"
    timeline = "https://padlet.com/embed/onshvns8f7vrrn2l"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-portfolio.svg?link_target=_blank"
    repo_description = "Ideas for building a Flask Web Server."
    repl = "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?lite=true"
    data = {"group": group, "route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_cbproj():
    group = "python"
    route = ".pythoncbproj"
    title = "College Board project preparation focus"
    timeline = "https://padlet.com/jmortensen7/cspcbproject"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-homesite.svg?link_target=_blank"
    repo_description = "Start process of building a project for College Board. Use my website or previous projects as " \
                       "idea starters. "
    data = {"group": group, "route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def python_study():
    group = "python"
    route = ".pythonstudy"
    title = "Python study resources"
    padlet = "https://padlet.com/jmortensen7/csp2021"
    data = {"group": group, "route": route, "title": title, "padlet": padlet}
    return data


def python_projects():
    return [python_hello(), python_flask(), python_cbproj(), python_ap(), python_study()]


def python_details():
    return {"title": 'CSP: Python', 'key': 'python'}
