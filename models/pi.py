"""Model in MVC has responsibility of managing data or database"""

"""A series of dictionaries to support data rendering"""

""" Raspberry Pi Only """


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


def pi_ssh():
    group = "pi"
    tag = "ssh"
    title = "SSH"
    html = "ssh.html"
    data = {"group": group, "tag": tag, "title": title, "html": html}
    return data


def pi_projects():
    return [pi_webserver(), pi_portforward(), pi_vncsetup(), pi_realvnc(), pi_ssh()]






