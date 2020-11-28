"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Project-base Learning Only """


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