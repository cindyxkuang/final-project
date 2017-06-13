from flask import Flask
from flask import render_template
from flask import abort
import client

app = Flask(__name__)

INIT_NUM = 200

@app.route('/')
def index():
    template = 'index.html'
    object_list = client.get_stations(INIT_NUM)
    return render_template(template, object_list=object_list, data=INIT_NUM)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = client.get_stations(INIT_NUM)
    for row in object_list:
        if row['id'] == int(row_id):
            return render_template(template, object=row, data=INIT_NUM)
    abort(404)
if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
