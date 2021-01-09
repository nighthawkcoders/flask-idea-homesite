"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Raspberry Pi Only """


def pi_details():
    return {"title": 'Raspberry Pi', 'key': 'pi'}


def pi_webserver():
    route = "pi-webserver"
    title = "Development Web server setup"
    padlet = "https://padlet.com/jmortensen7/pideploy"
    data = {"route": route, "title": title, "padlet": padlet}
    return data


def pi_deploy():
    route = "pi-deploy"
    title = "Production Web server setup"
    padlet = "https://padlet.com/jmortensen7/flaskdeploy"
    data = {"route": route, "title": title, "padlet": padlet}
    return data


def pi_portforward():
    route = "pi-portforward"
    title = "Port forward overview"
    padlet = "https://padlet.com/jmortensen7/piportforward"
    data = {"route": route, "title": title, "padlet": padlet}
    return data


def pi_vncsetup():
    route = "pi-vncsetup"
    title = "Virtual-Network-Computing setup"
    html = "vncsetup.html"
    data = {"route": route, "title": title, "html": html}
    return data


def pi_realvnc():
    route = "pi-realvnc"
    title = "RealVNC sharing access overview"
    html = "realvnc.html"
    data = {"route": route, "title": title, "html": html}
    return data


def pi_ssh():
    route = "pi-ssh"
    title = "SSH (secure shell) introduction"
    html = "ssh.html"
    data = {"route": route, "title": title, "html": html}
    return data


def pi_projects():
    return [pi_webserver(), pi_deploy(), pi_portforward(), pi_vncsetup(), pi_realvnc(), pi_ssh()]
