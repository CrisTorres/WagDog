from datetime import datetime

def index():
    return dict()

def first():
    return dict()

def second():
    return dict()

def loginpage():
    return dict()

def signuppage():
    return dict()

def signuppage2():
    return dict()

def createProfile():
    return dict()

def createProfile2():
    return dict()

def createProfile_interests():
    return dict()

def createProfile_aboutYourself():
    return dict()

def createProfile_confirmation():
    return dict()

@auth.requires_login()
def mainPage():
    if (db(db.profile.id==auth.user.id).count()==1):
        redirect(URL("index"))
    #record = db.profile(request.args(0,cast=int)) or redirect(URL('index'))
    #db.profile.id.default=auth.user.id
    #form = SQLFORM(db.profile,record)
    #form = SQLFORM(db.profile, buttons = [TAG.image(_type="submit", _href=URL("user"), _src= "http://127.0.0.1:8000/WagMore/static/_2.14.6/images/nextButton.png"),TAG.button('Submit',_type="submit")]) ##Wanna make the first image to work as a button
    
    db.profile.id.default=auth.user.id
    form = SQLFORM(db.profile)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
