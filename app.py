from flask import *
import threading
import API

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def main():
    macs = API.get_macs()
    options = { "macs": macs }
    if request.method == 'GET':
        return render_template('base.html', **options)
    else:
        if request.form['op'] == 'new_mac':
            if request.form['address'] is not None:
                print("Adding: ", request.form['address'])
                API.add_mac(request.form['address'])


        return render_template('base.html', **options)

if __name__ == '__main__':
    # API = threading.Thread(target=API.main)
    app.run()
