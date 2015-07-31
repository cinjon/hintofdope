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
    {'type':i, 'body':"Let's get dis shit kickin' wit da dope. here's da word - you get yo dope every one to two weeks, and if you decide you no longer want yo dope, reply DOPE to this number. yaheard"},
    {'type':d, 'body':"Dopity dop."},
    {'type':r, 'body':"Hi there, welcome back to Hints of Hope. We're so honored to be your Mercury of inspiration."},
    {'type':g, 'body':'Help your friends and loved ones by sending them a Hint of Hope @ hintofhope.today! ... Or just reply to this message with their phone number. We gotchu.'},
    ]
