"""
Options for Messages. Each one looks like:
{type:<'death'|'life'|...>, body:'The world is a teapot and you are the tea.'}
"""

ty_enum = {'dope':0, 'intro':1, 'reintro':2, 'growth':3}
d = ty_enum.get('dope')
i = ty_enum.get('intro')
r = ty_enum.get('reintro')
g = ty_enum.get('growth')

options = [
    {'type':i, 'body':"Yo homie coming atchu from the 213! Every 1-2 weeks we’ll drop dope ass rhymes on ya fone. If y'all no longer want ya dope (why you frontin??), reply DOPE to this message."},
    {'type':d, 'body':"Dopity dop."},
    {'type':r, 'body':"Welcome back gangsta! Fresh hit of dope coming right up."},
    {'type':g, 'body':'Help your friends and loved ones by sending them a Hint of Hope @ hintofhope.today! ... Or just reply to this message with their phone number. We gotchu.'},
    ]
