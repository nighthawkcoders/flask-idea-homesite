"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""
def java_ap():
    group = "java"
    tag = "ap"
    title = "AP study"
    timeline = "https://padlet.com/embed/iji39ih2mzwa"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline}
    return data

def java_hello():
    group = "java"
    tag = "hello"
    title = "Hello series"
    timeline = "https://padlet.com/embed/lslb7s7y06sf"
    repo = "https://gh-card.dev/repos/nighthawkcoders/javahello.svg?link_target=_blank"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Java-Hello-Series?lite=true"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo, "repo_description": repo_description, "repl": repl}
    return data

def java_mvc():
    group = "java"
    tag = "mvc"
    title = "MVC ideas"
    timeline = "https://padlet.com/embed/iji39ih2mzwa"
    repo = "https://gh-card.dev/repos/nighthawkcoders/mvc-idea.svg?link_target=_blank"
    repo_description = "Ideas for coding in the Model View Control (MVC) style."
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo, "repo_description": repo_description}
    return data

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
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo, "repo_description": repo_description, "repl": repl}
    return data

def python_flask():
    group = "python"
    tag = "flask"
    title = "MVC ideas"
    timeline = "https://padlet.com/embed/onshvns8f7vrrn2l"
    repo = "https://gh-card.dev/repos/nighthawkcoders/flask-idea-portfolio.svg?link_target=_blank"
    repo_description = "Ideas for building a Flask Web Server."
    repl = "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?lite=true"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo, "repo_description": repo_description, "repl": repl}
    return data