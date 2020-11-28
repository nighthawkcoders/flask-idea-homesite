"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" JAVA ONLY """


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