import krbV

'''
http://stackoverflow.com/questions/3143630/python-validate-kerberos-ticket
'''

def has_ticket():
    '''
    Checks to see if the user has a valid ticket.
    '''
    ctx = krbV.default_context()
    cc = ctx.default_ccache()
    try:
        princ = cc.principal()
        retval = True
    except krbV.Krb5Error:
        retval = False

    return retval
