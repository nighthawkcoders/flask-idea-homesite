"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" PYTHON ONLY """



def python_ap():
    group = "python"
    tag = "ap"
    title = "AP study"
    timeline = "https://padlet.com/embed/k3bwade11ekevmum"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline}
    return data


def python_hello():
    group = "python"
    tag = "hello"
    title = "Hello series"
    timeline = "https://padlet.com/embed/2p9700yyoz3flccs"
    repo = "https://gh-card.dev/repos/nighthawkcoders/pythonhello.svg"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Python-Hello-Series?lite=true"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_flask():
    group = "python"
    tag = "flask"
    title = "Flask ideas"
    timeline = "https://padlet.com/embed/onshvns8f7vrrn2l"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-portfolio.svg?link_target=_blank"
    repo_description = "Ideas for building a Flask Web Server."
    repl = "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?lite=true"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def python_study():
    group = "python"
    tag = "study"
    title = "Python study"
    padlet = "https://padlet.com/jmortensen7/csp2021"
    data = {"group": group, "tag": tag, "title": title, "padlet": padlet}
    return data


def python_projects():
    return [python_hello(), python_flask(), python_ap(), python_study()]

