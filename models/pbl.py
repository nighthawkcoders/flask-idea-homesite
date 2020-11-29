"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Project-base Learning Only """


def pbl_overview():
    group = "pbl"
    route = ".pbloverview"
    title = "Project-base learning overview"
    html = "pbl.html"
    data = {"group": group, "route": route, "title": title, "html": html}
    return data


def pbl_scrum():
    group = "pbl"
    route = ".pblscrum"
    title = "Classroom Roles and Scrum intro"
    html = "scrum.html"
    data = {"group": group, "route": route, "title": title, "html": html}
    return data


def pbl_projects():
    return [pbl_overview(), pbl_scrum()]

def pbl_details():
    return {"title": 'Project-based Learning', 'key': 'pbl'}