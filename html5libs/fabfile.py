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
