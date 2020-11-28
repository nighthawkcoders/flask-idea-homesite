"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Github and Git Only """


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