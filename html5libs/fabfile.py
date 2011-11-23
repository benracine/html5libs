from fabric.api import local

def test():
    local("./manage.py test")

def commit():
    local("git add .")
    try:
        local("""git commit -am "deploy" """)
    except:
        print "No changes were made"

def push():
    local("git push github master")

def deploy(prudent=True):
    commit()
    local("git push heroku master")


# Database Administration
def syncdb(server):
    if server=='dep':
        local("heroku run python html5libs/manage.py syncdb")
    else:
        local("python manage.py syncdb")

def migrate(server):
    if server=='dep':
        local("heroku run python html5libs/manage.py migrate")
    else:
        local("python manage.py migrate")

def package_updater(server):
    if server=='dep':
        local("heroku run python html5libs/manage.py package_updater")
    else:
        local("python manage.py package_updater")


# Admin features
def superuser(server):
    username = raw_input("What username?")
    email = raw_input("What email?")
    if server=='dep':
        command = "heroku run html5libs/manage.py createsuperuser --username %s --email %s" %(username, email)
        local(command)
