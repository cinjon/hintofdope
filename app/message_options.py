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
    {'type':d, 'body':"When it comes to sex, I’m similar to the Thrilla in Manila. Honeys call me Bigga the condom filler. Whether it’s stiff tongue or stiff dick, Biggie squeeze it to make shit fit, now check this shit."},
    {'type':d, 'body':"She mad because what we had didn’t last. I’m glad because her cousin let me hit the ass."},
    {'type':d, 'body':"I got the cleanest meanest penis. Ya never seen this stroke of genius."},
    {'type':d, 'body':"Hit you with my dick, make your kidneys shift."},
    {'type':d, 'body':"Crack mothers, crack babies and AIDS patients. Youngbloods can’t spell, but they could rock you in Playstation"},
    {'type':d, 'body':"And even after all my logic and all my theory. I add a motherfucker so you ignorant niggas hear me"},
    {'type':d, 'body':"Swimmin' laps around a bottle of Louie the Thirteenth. Jumpin' off of a mountain into a sea of codeine/I'm at the top of the top, but still I climb/And if I should ever fall, the ground will then turn to wine."},
    {'type':d, 'body':"Rollin' down the street, smokin' indo, sippin' on gin an juice. Lay back with my mind on my money and my money on my mind."},
    {'type':d, 'body':"Brain cells are lit. Ideas start to hit/Next the formation of words that fit. At the table I sit, making it legit/And when my pen hits the paper. Ahh shit!"},
    {'type':r, 'body':"Welcome back gangsta! Fresh hit of dope coming right up."},
    {'type':g, 'body':'Help your friends and loved ones by sending them a Hint of Hope @ hintofhope.today! ... Or just reply to this message with their phone number. We gotchu.'},
    ]
