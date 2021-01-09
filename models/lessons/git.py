"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Github and Git Only """


def git_details():
    return {"title": 'GitHub + Git', 'key': 'git'}


def git_concepts():
    route = "git-concepts"
    title = "Intro to GitHub concepts"
    video = "https://www.youtube.com/embed/phGdqJB6ep0"
    data = {"route": route, "title": title, "video": video}
    return data


def git_replto():
    route = "git-replto"
    title = "Migration from Repl-2-Git-2-IntelliJ"
    video = "https://www.youtube.com/embed/8TG99JmNUaM"
    data = {"route": route, "title": title, "video": video}
    return data


def git_projects():
    return [git_concepts(), git_replto()]
