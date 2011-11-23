from fabric.api import local

def test():
    local("./manage.py test")

def commit():
    local("git add . && git commit")

def deploy(prudent=True):
    """
    if prudent:
        test()
    """
    commit()
    local("git push heroku master")

def deployment_package_updater():
    local("heroku run html5libs/manage.py package_updater")

def deployment_superuser_add(username, email):
    command = "heroku run html5libs/manage.py createsuperuser --username %s --email %s" %(username, email)
    local(command)

