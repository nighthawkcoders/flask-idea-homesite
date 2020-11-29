"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Raspberry Pi Only """


def pi_webserver():
    key = "pi"
    route = ".piwebserver"
    title = "Web server setup"
    padlet = "https://padlet.com/jmortensen7/pideploy"
    data = {"key": key, "route": route, "title": title, "padlet": padlet}
    return data


def pi_portforward():
    key = "pi"
    route = ".piportforward"
    title = "Port forward overview"
    padlet = "https://padlet.com/jmortensen7/piportforward"
    data = {"key": key, "route": route, "title": title, "padlet": padlet}
    return data


def pi_vncsetup():
    key = "pi"
    route = ".pivncsetup"
    title = "Virtual-Network-Computing setup"
    html = "vncsetup.html"
    data = {"key": key, "route": route, "title": title, "html": html}
    return data


def pi_realvnc():
    key = "pi"
    route = ".pirealvnc"
    title = "RealVNC sharing access overview"
    html = "realvnc.html"
    data = {"key": key, "route": route, "title": title, "html": html}
    return data


def pi_ssh():
    key = "pi"
    route = ".pissh"
    title = "SSH (secure shell) introduction"
    html = "ssh.html"
    data = {"key": key, "route": route, "title": title, "html": html}
    return data


def pi_projects():
    return [pi_webserver(), pi_portforward(), pi_vncsetup(), pi_realvnc(), pi_ssh()]


def pi_details():
    return {"title": 'Raspberry Pi', 'key': 'pi'}
