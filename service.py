from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config.from_object(__name__)

# error handling
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


# Endpoints Mahasiswa
from mahasiswa import *
@app.route('/api/mahasiswa', methods=['GET'])
def mhs_get():

    # get request
    if request.method == 'GET':
        query = mahasiswa.select()
        data = [i.serialize for i in query]

        if data:
            res = jsonify(data)
            res.status_code = 200
        else:
            # if no results are found.
            output = {
                "error": "No results found",
                "url": request.url,
            }
            res = jsonify(output)
            res.status_code = 404
        return res

# Endpoints Kelompok
from kelompok import *
@app.route('/api/kelompok/<string:kode_kelompok>', methods=['GET'])
def klmpk_get_by_id(kode_kelompok):

    # get request
    if request.method == 'GET':
        query = kelompok.select().where(kelompok.kodekelompok == kode_kelompok)
        data = [i.serialize for i in query]

        if data:
            res = jsonify(data)
            res.status_code = 200
        else:
            # if no results are found.
            output = {
                "error": "No results found",
                "url": request.url,
            }
            res = jsonify(output)
            res.status_code = 404
        return res

if __name__ == '__main__':
    app.run(debug=True)