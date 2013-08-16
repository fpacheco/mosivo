# coding: utf8
# try something like
def index(): 
    return dict(message="hello from admin.py")

@auth.requires_membership('admin')
def users():
    form = SQLFORM.grid(db.auth_user)
    title = T("Registered users")
    return dict(form=form, title=title)

@auth.requires_membership('admin')
def groups():
    form = SQLFORM.grid(db.auth_group)
    title = T("Groups")
    return dict(form=form, title=title)

@auth.requires_membership('admin')
def memberships():
    form = SQLFORM.grid(db.auth_membership)
    title = T("Membership")
    return dict(form=form, title=title)
