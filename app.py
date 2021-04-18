import flask
import functions

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for turning on the TV through Siri, such as a lazy ass person.</p>"

@app.route('/tv', methods=['GET'])
def turnTVOn():
    return functions.turnTVOn()

app.run(host='192.168.18.24', port=14749)
