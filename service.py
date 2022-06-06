from flask import *

app = Flask(__name__)
app.config.from_object(__name__)

######################Unknown URL Handling
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

######################Endpoints Mahasiswa
###################### Mahasiswa Read #######################
##### Mahasiswa Zone #####
@app.route('/api/mahasiswa/<username>', methods=['GET'])
def mhs_get_by_id(username):
    if request.method == 'GET':
        query = mahasiswa.select().where(mahasiswa.username == username)
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
##### Dosen Zone #####
from mahasiswa import *
@app.route('/api/mahasiswa/', methods=['GET'])
def mhs_get():
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
###################### Mahasiswa Update #######################
##### Mahasiswa Zone #####
@app.route('/api/mahasiswa/update/<iduser>', methods=['GET','POST'])
def mhs_update(iduser):
    if request.method == 'POST':
        data = request.form
        result = (mahasiswa.update(data).where(mahasiswa.idmahasiswa == iduser).execute())
        return jsonify(result)
##### Dosen Zone #####
@app.route('/api/admin/mahasiswa/<iduser>', methods=['GET','POST'])
def mhs_admin_update():
    if request.method == 'POST':
        data = request.form
        result = (mahasiswa.update(data).where(mahasiswa.idmahasiswa == iduser).execute())
        return jsonify(result)    
###################### Mahasiswa Insert #######################
##### Dosen Zone #####
@app.route('/api/admin/mahasiswa/insert', methods=['GET','POST'])
def mhs_insert():
    if request.method == 'POST':
        data = request.form
        result = (mahasiswa.insert(data).execute())
        return jsonify(result)

######################Endpoints Kelompok
###################### Kelompok Read All#######################
from kelompok import *
@app.route('/api/kelompok/', methods=['GET'])
def klmpk_get_all(kode_kelompok):

    # get request
    if request.method == 'GET':
        query = kelompok.select()
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
###################### Kelompok Read Specific #######################
from kelompok import *
@app.route('/api/kelompok/<kode_kelompok>', methods=['GET'])
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
###################### Kelompok Insert #######################
@app.route('/api/admin/kelompok/insert', methods=['GET','POST'])
def kelompok_insert():
    if request.method == 'POST':
        data = request.form
        result = (kelompok.insert(data).execute())
        return jsonify(result)
###################### Kelompok Update #######################
@app.route('/api/kelompok/update/<kode_kelompok>', methods=['GET','POST'])
def kelompok_update(kode_kelompok):
    if request.method == 'POST':
        data = request.form
        result = (kelompok.update(data).where(kelompok.kodekelompok == kode_kelompok).execute())
        return jsonify(result)


######################Endpoints PR
###################### PR Read #######################
from pr import *
@app.route('/api/pr/<user_name>', methods=['GET'])
def pr_get_by_id(user_name):

    # get request
    if request.method == 'GET':
        query = pr.select().where(pr.username == user_name)
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
###################### PR Insert #######################
@app.route('/api/admin/pr/insert', methods=['GET','POST'])
def pr_insert():
    if request.method == 'POST':
        data = request.form
        result = (pr.insert(data).execute())
        return jsonify(result)
###################### Aplikasi Update #######################
@app.route('/api/admin/pr/update/<kode_pr>', methods=['GET','POST'])
def pr_update(kode_pr):
    if request.method == 'POST':
        data = request.form
        result = (pr.update(data).where(pr.kodepr == kode_pr).execute())
        return jsonify(result)

######################Endpoints Aplikasi
###################### Aplikasi Read #######################
from aplikasi import *
@app.route('/api/aplikasi/<id_aplikasi>', methods=['GET'])
def aplikasi_get_by_id(id_aplikasi):

    # get request
    if request.method == 'GET':
        query = aplikasi.select().where(aplikasi.idaplikasi == id_aplikasi)
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
###################### Aplikasi Insert #######################
##### Mahasiswa Zone #####
@app.route('/api/admin/aplikasi/insert', methods=['GET','POST'])
def aplikasi_insert():
    if request.method == 'POST':
        data = request.form
        result = (aplikasi.insert(data).execute())
        return jsonify(result)
###################### Aplikasi Update #######################
##### Mahasiswa Zone #####
@app.route('/api/mahasiswa/aplikasi/update/<id_aplikasi>', methods=['GET','POST'])
def aplikasi_update(id_aplikasi):
    if request.method == 'POST':
        data = request.form
        result = (aplikasi.update(data).where(aplikasi.idaplikasi == id_aplikasi).execute())
        return jsonify(result)
##### Dosen Zone #####
@app.route('/api/admin/aplikasi/update/<id_aplikasi>', methods=['GET','POST'])
def aplikasi_admin_update(id_aplikasi):
    if request.method == 'POST':
        data = request.form
        result = (aplikasi.update(data).where(aplikasi.idaplikasi == id_aplikasi).execute())
        return jsonify(result)

######################Endpoints Rating
###################### Rating View #######################
##### App Rating #####
from rating import *
@app.route('/api/rating/app/<id_aplikasi>', methods=['GET'])
def rating_get_by_appid(id_aplikasi):

    # get request
    if request.method == 'GET':
        query = rating.select().where(rating.idaplikasi == id_aplikasi)
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
##### App Specific User Rating #####
from rating import *
@app.route('/api/rating/user/<id_mahasiswa>', methods=['GET'])
def rating_get_by_userid(id_mahasiswa):

    # get request
    if request.method == 'GET':
        query = rating.select().where(rating.idmahasiswa == id_mahasiswa)
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
###################### Rating Insert #######################
@app.route('/api/rating/insert', methods=['GET','POST'])
def rating_insert():
    if request.method == 'POST':
        data = request.args
        result = (rating.insert(data).execute())
        return jsonify(result)
###################### Rating Update #######################
##### Mahasiswa Zone #####
@app.route('/api/rating/update/<id_aplikasi>', methods=['GET','POST'])
def rating_update(id_aplikasi):
    if request.method == 'POST':
        data = request.args
        result = (rating.update(data).where(rating.idaplikasi == id_aplikasi).where(rating.idmahasiswa == data["idmahasiswa"]).execute())
        return jsonify(result)    

# Endpoints User
from user import *
@app.route('/api/user/<iduser>', methods=['GET'])
def user_get_by_id(iduser):

    # get user main
    if request.method == 'GET':
        query = user.select().where(user.id == iduser)
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