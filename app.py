from flask import Flask
from flask import render_template
from flask import abort, request
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
    obj = client.get_by_id(row_id)[0]
    if str(obj['id']) == row_id:
        return render_template(template, object=obj)
    abort(404)

@app.route('/search/')
def search():
    zip_code = request.args.get('search')
    if zip_code == '':
        abort(404)
    template = 'search.html'
    raw_object = client.get_by_zip(zip_code)
    object_list = raw_object[0]
    search_results = raw_object[1]
    return render_template(template, object_list=object_list, data=search_results)

@app.route('/search/<row_id>/')
def search_detail(row_id):
    template = 'search_detail.html'
    obj = client.get_by_id(row_id)[0]
    if str(obj['id']) == row_id:
        return render_template(template, object=obj)
    abort(404)

if __name__ == '__main__':
    # Fire up the Flask test server
    #app.run(debug=True, use_reloader=True)
    app.run(debug=True)