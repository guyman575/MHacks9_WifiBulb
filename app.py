from flask import *
from flask_bootstrap import Bootstrap
import threading
import API

app = Flask(__name__, template_folder='templates')
Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def main():
    macs = API.get_macs()
    options = { "macs": macs }
    if request.method == 'GET':
        return render_template('test.html', **options)
    else:
        if request.form['op'] == 'new_mac':
            if request.form['address'] is not None:
                print("Adding: ", request.form['address'])
                API.add_mac(request.form['address'])
        elif request.form['op'] == "remove_mac":
            API.remove_mac(request.form['remove'])
        elif request.form['set_speed'] == "set_speed":
            # API.set_speed(request.form["speed"])
            pass

        return render_template('test.html', **options)

if __name__ == '__main__':
    # API = threading.Thread(target=API.main)
    app.run(debug=True)
