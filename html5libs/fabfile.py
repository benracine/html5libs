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
    commit()
    local("git push github master")

def deploy(prudent=True):
    """need to change debug from true to false
    and change serve using static media from false to true"""
    try:
        commit()
    except:
        pass
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
    if server=='dev':
        local("python manage.py package_updater")
    else:
        local("heroku run python html5libs/manage.py package_updater")

def db_pull():
    dbname = raw_input("What db name?")
    local("heroku db:pull --app html5libs postgres://postgres@localhost/%s --confirm html5libs" %(dbname))

# Admin features
def superuser(server):
    username = raw_input("What username?")
    email = raw_input("What email?")
    if server=='dep':
        command = "heroku run html5libs/manage.py createsuperuser --username %s --email %s" %(username, email)
        local(command)
