#!/usr/bin/python3

# global reqs
import json
import logging
import websocket
import configparser
from flask import Flask, request
from websocket import create_connection

# create a Flask app     
app = Flask(__name__)

# flask routes
@app.route('/sparqlgen', methods=["POST"])
def translate():

    # debug print
    logging.debug("New SPARQLgenerate request received!")
    
    # read the input
    query = request.form["query"]
    
    # build a message for SPARQL-generate api
    msg = {"defaultquery": query,
           "namedqueries": [],
           "defaultgraph": "",
           "namedgraphs": [],
           "documentset": [{
	       "uri": "",
	       "string": "",
	       "mediatype": "" }],
           "stream": False }

    def on_message(ws, message):

        # if log="" and clear=True -> connection should not be closed, since the real message is not arrived
        # if log="..." -> this is the real message, but not the interesting output
        # if log="" and clear=False -> then in result we found what we need
        
        msg = json.loads(message)
        print(msg)
        for el in msg:
            if (el["log"] == "") and (not(el["clear"])):
                logging.debug("Results:")
                logging.debug(el["result"])
                ws.resp = {"success":True, "result":el["result"]}
                ws.close()

    def on_error(ws, error):
        ws.resp = {"success":False}
        logging.debug(error)

    def on_close(ws):
        logging.debug("Closing connection")
    
    def on_open(ws, msg = msg):
        logging.debug("Sending request to SPARQLgenerate websocket server")
        ws.send(json.dumps(msg))
        logging.debug("Sent...")

    ws = websocket.WebSocketApp("wss://ci.mines-stetienne.fr/sparql-generate/transformStream",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
        
    # return
    return json.dumps(ws.resp)


# main
if __name__ == "__main__":

    # configure logger
    logging.basicConfig(level=logging.DEBUG)
    logging.info("SPARQLgenerate service starting...")

    # read the config file
    app.run(host='0.0.0.0')
