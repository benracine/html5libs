from fabric.api import local

def test():
    local("./manage.py test")

def commit():
    local("git add .")
    try:
        local("git commit -a")
    except:
        print "No changes were made"

def push_to_github():
    local("git push github master")

def deploy(prudent=True):
    """
    if prudent:
        test()
    """
    commit()
    local("git push heroku master")


def deployment_syncdb():
    local("heroku run python html5libs/manage.py syncdb")

def deployment_migrate():
    local("heroku run python html5libs/manage.py migrate")

def deployment_package_updater():
    local("heroku run python html5libs/manage.py package_updater")

def deployment_superuser_add(username, email):
    command = "heroku run html5libs/manage.py createsuperuser --username %s --email %s" %(username, email)
    local(command)
