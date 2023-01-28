# import des fonctions 
try:
    from logic import *
except:
    from chat.logic import *

import json


# Route concernant la reception d'un message
@application.route("/msgSent", methods=["POST"])
def msg_sent():
    try:
        msg = json.loads(request.data)
    except Exception as e:
        return str(e)

    if verification_msg(msg) == True:
        try:
            with psycopg2.connect(
                    "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)) as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO message (content) VALUES (%s);", (msg,))
                    conn.commit()
        except Exception as e:
            return str(e)
    return "0"


# Routes pour servir l'application "conversation"
@application.route("/conversation", methods=["GET"])
def conversation():
    html = open("templates/chat/conversation.html", "r").read()
    return html


@application.route("/conversation.js", methods=["GET"])
def am38_js():
    js = open("templates/chat/conversation.js", "r").read()
    return Response(js, mimetype='text/javascript')
