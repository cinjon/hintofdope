import app
import os
from flask import send_from_directory, make_response, request, redirect
from sqlalchemy.sql.expression import func, select
from flask.ext.mobility.decorators import mobile_template
import twilio.twiml
import random

# special file handlers and error handlers
@app.flask_app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.flask_app.root_path, 'static'), 'img/favicon.ico')

@app.flask_app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

# routing for basic pages (pass routing onto the Angular app)
@app.flask_app.route('/')
@app.flask_app.route('/about')
def basic_pages():
    return make_response(open('app/public/template/index.html').read())

@app.flask_app.route('/twilio_receiver')
def twilio_receiver():
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    resp = twilio.twiml.Response()
    if body != 'DOPE':
        resp.message("Whatchu say?")
        try:
            app.flask_app.logger.debug('Message from %s: %s' % (from_number, body))
        except Exception, e:
            pass
    elif app.models.delete_phone(from_number):
        resp.message("No biggie son. We be here when you craving that good shit.")
    else:
        resp.message("Shit ain't right. Do that again nig.")
    return str(resp)

@app.flask_app.route('/save-phone', methods=['POST'])
def save_phone():
    try:
        phone = None
        phone_string = request.form['phone']
        if phone_string and len(phone_string) == 10:
            has_phone, phone = app.models.get_or_create_phone(phone_string)
        else:
            return app.utility.xhr_response({'success':False, 'msg':"Those digits don't work fool."}, 200)

        if has_phone and phone.deleted:
            return app.utility.xhr_response({'success':False, 'msg':"Aight, if you really want da Dope again, email the DinoSaur at dino.mihalopoulos@gmail.com."}, 200)
        elif has_phone:
            return app.utility.xhr_response({'success':False, 'msg':"We alrdy got those digits son. Dope on its way!"}, 200)
        else:
            phone.send_intro()
            return app.utility.xhr_response({'success':True, 'msg':'Dope! Coming atcha boy.'}, 200)
    except Exception, e:
        app.flask_app.logger.debug(e)
        return app.utility.xhr_response({'success':False, 'msg':"We messin'. Tell me those digits again yo."}, 200)

# @app.flask_app.route('/google34d3fe92d155a2aa.html')
# def google_verification(**kwargs):
#     return make_response(open('app/public/template/google34d3fe92d155a2aa.html').read())
