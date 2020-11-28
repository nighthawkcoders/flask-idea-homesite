"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Java Section """


def java_ap():
    group = "java"
    tag = "ap"
    title = "AP study"
    timeline = "https://padlet.com/jmortensen7/APCentralCSA_p1"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline}
    return data


def java_hello():
    group = "java"
    tag = "hello"
    title = "Hello series"
    timeline = "https://padlet.com/jmortensen7/csatime"
    repo = "https://gh-card.dev/repos/nighthawkcoders/javahello.svg?link_target=_blank"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Java-Hello-Series?lite=true"
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def java_mvc():
    group = "java"
    tag = "mvc"
    title = "MVC ideas"
    timeline = "https://padlet.com/jmortensen7/csatime1_2"
    repo = "https://gh-card.dev/repos/nighthawkcoders/mvc-idea.svg?link_target=_blank"
    repo_description = "Ideas for coding in the Model View Control (MVC) style."
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def java_event():
    group = "java"
    tag = "event"
    title = "Event-based"
    timeline = "https://padlet.com/jmortensen7/jho9v5wc4p9jgyn2"
    repo = "https://gh-card.dev/repos/nighthawkcoders/virussim-idea-events.svg?link_target=_blank"
    repo_description = "Concepts to get started with Event-based programming."
    data = {"group": group, "tag": tag, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def java_study():
    group = "java"
    tag = "study"
    title = "Java study"
    padlet = "https://padlet.com/embed/b24kstdegziddjqr"
    data = {"group": group, "tag": tag, "title": title, "padlet": padlet}
    return data


def java_projects():
    return [java_hello(), java_mvc(), java_event(), java_ap(), java_study()]


""" Python Section """


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


""" Pi Section """


def pi_webserver():
    group = "pi"
    tag = "webserver"
    title = "Web server"
    padlet = "https://padlet.com/jmortensen7/pideploy"
    data = {"group": group, "tag": tag, "title": title, "padlet": padlet}
    return data


def pi_portforward():
    group = "pi"
    tag = "portforward"
    title = "Port forward"
    padlet = "https://padlet.com/jmortensen7/piportforward"
    data = {"group": group, "tag": tag, "title": title, "padlet": padlet}
    return data

def pi_vncsetup():
    group = "pi"
    tag = "vncsetup"
    title = "VNC setup"
    html = "vncsetup.html"
    data = {"group": group, "tag": tag, "title": title, "html": html}
    return data

def pi_realvnc():
    group = "pi"
    tag = "realvnc"
    title = "RealVNC"
    html = "realvnc.html"
    data = {"group": group, "tag": tag, "title": title, "html": html}
    return data


def pi_projects():
    return [pi_webserver(), pi_portforward(), pi_vncsetup(), pi_realvnc()]


""" Git Section """


def git_concepts():
    group = "git"
    tag = "concepts"
    title = "Concepts"
    video = "https://www.youtube.com/embed/phGdqJB6ep0"
    data = {"group": group, "tag": tag, "title": title, "video": video}
    return data


def git_replto():
    group = "git"
    tag = "replto"
    title = "Repl-2-Git"
    video = "https://www.youtube.com/embed/8TG99JmNUaM"
    data = {"group": group, "tag": tag, "title": title, "video": video}
    return data


def git_projects():
    return [git_concepts(), git_replto()]


""" PBL Section """


def pbl_overview():
    group = "pbl"
    tag = "overview"
    title = "Overview"
    html = "pbl.html"
    data = {"group": group, "tag": tag, "title": title, "html": html}
    return data


def pbl_scrum():
    group = "pbl"
    tag = "scrum"
    title = "Scrum"
    html = "scrum.html"
    data = {"group": group, "tag": tag, "title": title, "html": html}
    return data


def pbl_projects():
    return [pbl_overview(), pbl_scrum()]
