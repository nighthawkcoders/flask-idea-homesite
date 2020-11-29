"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Github and Git Only """


def git_concepts():
    group = "git"
    route = ".gitconcepts"
    title = "Intro to GitHub concepts"
    video = "https://www.youtube.com/embed/phGdqJB6ep0"
    data = {"group": group, "route": route, "title": title, "video": video}
    return data


def git_replto():
    group = "git"
    route = ".gitreplto"
    title = "Migration from Repl-2-Git-2-IntelliJ"
    video = "https://www.youtube.com/embed/8TG99JmNUaM"
    data = {"group": group, "route": route, "title": title, "video": video}
    return data


def git_projects():
    return [git_concepts(), git_replto()]