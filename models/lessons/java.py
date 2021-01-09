"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" JAVA ONLY """


def java_details():
    return {"title": 'CSA: Java', 'key': 'java'}


def java_ap():
    route = "java-ap"
    title = "AP 10 unit study outline"
    timeline = "https://padlet.com/jmortensen7/APCentralCSA_p1"
    data = {"route": route, "title": title, "timeline": timeline}
    return data


def java_hello():
    route = "java-hello"
    title = "Hello to Project-based learning and Java"
    timeline = "https://padlet.com/jmortensen7/csatime"
    repo = "https://gh-card.dev/repos/nighthawkcoders/javahello.svg?link_target=_blank"
    repo_description = "Hello, World! and a variety of classroom and technical introductions"
    repl = "https://repl.it/@jmort1021/Java-Hello-Series?lite=true"
    data = {"route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description, "repl": repl}
    return data


def java_mvc():
    route = "java-mvc"
    title = "Model-View-Control introduction and ideas"
    timeline = "https://padlet.com/jmortensen7/csatime1_2"
    repo = "https://gh-card.dev/repos/nighthawkcoders/mvc-idea.svg?link_target=_blank"
    repo_description = "Ideas for coding in the Model View Control (MVC) style."
    data = {"route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def java_event():
    route = "java-events"
    title = "Events, Inheritance, Database concepts"
    timeline = "https://padlet.com/jmortensen7/jho9v5wc4p9jgyn2"
    repo = "https://gh-card.dev/repos/nighthawkcoders/virussim-idea-events.svg?link_target=_blank"
    repo_description = "Concepts to get started with Event-based programming."
    data = {"route": route, "title": title, "timeline": timeline, "repo": repo,
            "repo_description": repo_description}
    return data


def java_study():
    route = "java-resources"
    title = "Java study resources"
    padlet = "https://padlet.com/embed/b24kstdegziddjqr"
    data = {"route": route, "title": title, "padlet": padlet}
    return data


def java_projects():
    return [java_hello(), java_mvc(), java_event(), java_ap(), java_study()]
