from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask.wrappers import Request
from flask_mysqldb import MySQL
import hashlib

from werkzeug.local import F

# MySql Connection
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='gestionclientes'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

session = None

months = [{
    1: 'Enero', 
    2: 'Febrero', 
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'}]

def CUR():
    cur_gender = mysql.connection.cursor()
    cur_gender.execute('SELECT * FROM genre')
    gender = cur_gender.fetchall()
    
    cur_depart = mysql.connection.cursor()
    cur_depart.execute('SELECT * FROM department')
    departs = cur_depart.fetchall()

    cur_city = mysql.connection.cursor()
    cur_city.execute('SELECT * FROM city')
    cities = cur_city.fetchall()

    cur_plan = mysql.connection.cursor()
    cur_plan.execute('SELECT * FROM plans')
    plan = cur_plan.fetchall()

    cur_company = mysql.connection.cursor()
    cur_company.execute('SELECT * FROM company')
    company = cur_company.fetchall()
    return gender, departs, cities, plan, company

def allclient_cur():
    cur_allclient = mysql.connection.cursor()
    cur_allclient.execute('SELECT * FROM client')
    return cur_allclient.fetchall()

@app.route('/')
def Index():
    if not session:
        return render_template('login.html')
    else:
        return render_template('index.html')

# CLIENTES

def depart(idMuni):
    _, departs,cities,_,_ = CUR()
    for i in range(len(cities)):
        a = int(idMuni)
        b = int(cities[i][0])
        if a == b:
            x = int(cities[i][2])
            for j in range(len(departs)):
                z = int(departs[j][0])
                if x == z:
                    idDepart = departs[j][0]
                    break 
    return idDepart  

def getKey(item):
    return item[1]

def verify_user(met):
    if request.method == met:
        user_login = request.form['user_login']
        cur_user = mysql.connection.cursor()
        cur_user.execute('SELECT * FROM users WHERE user_login = %s', [user_login])
        user = cur_user.fetchall()
        if not user:
            return False, None
        else:
            user_pass = request.form['user_pass']
            encode_pass = hashlib.md5(user_pass.encode())
            crypt_pass = encode_pass.hexdigest()
            cur_pass = mysql.connection.cursor()
            cur_pass.execute('SELECT * FROM users WHERE user_pass = %s', [crypt_pass])
            password = cur_pass.fetchall()
            if not password:
                return False, None
            else:
                return True, user_login

def Date(date, num_month):
    id = []
    for i in range(len(date)):
        print(f'{date[i][4].month} == {num_month}')
        if int(date[i][4].month) == int(num_month):
            id.insert(i, str(date[i][0]))
            print(id)
    return id

@app.route('/client/add', methods=['POST', 'GET'])
def add_cliente():
    verify, _ = verify_user(request.method)
    if verify is True:
        gender, _, cities,plan,company = CUR()
        _cities = sorted(cities, key=getKey)
        return render_template('./clientes/addclient.html', gender = gender, cities = _cities, plan = plan, companies = company)
    else:
        flash(f'Usuario y contrase??a son incorrectos')
        return redirect(url_for('Index'))

@app.route('/client/save', methods=['POST'])
def save_client():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        dni = request.form['dni']
        date = request.form['date']
        idGender = request.form['idGender']
        tel = request.form['tel']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        idMuni = request.form['idMuni']
        idDepart = depart(idMuni)
        idPlan = request.form['idPlan']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO client (name, lastname, dni, date, idGender, tel, phone, email, address, idDepart, idMuni, idPlan) VALUES (%s, %s, %s, %b, %b, %s, %s, %s, %s, %b, %b, %b)', (name, lastname, dni, date, idGender, tel, phone, email, address, idDepart, idMuni, idPlan))
        mysql.connection.commit()
        flash('Cliente a??adido satisfactoriamente')
        return redirect(url_for('Index'))

@app.route('/client/consult', methods=['POST'])
def consult_cliente():
    if request.method == 'POST':
        gender, departs, cities, plan, company = CUR()
        tel = request.form['tel']
        cur_client = mysql.connection.cursor()
        cur_client.execute('SELECT * FROM client WHERE tel = %s', [tel])
        client = cur_client.fetchall()
        if not tel:
            allclient = allclient_cur()
            _cities = sorted(cities, key=getKey)
            return render_template('./clientes/showclient.html', client = allclient, cities = _cities, months = months)
        else:
            if not client:
                flash(f'El cliente con el n??mero "{tel}" no existe')
                return redirect(url_for('Index'))
            else:
                return render_template('./clientes/consultclient.html', client = client, gender = gender, departs = departs, cities = cities, plan = plan, companies = company)

@app.route('/client/consult/<id>')
def id_client(id):
    gender, departs, cities, plan, company = CUR()
    cur_client = mysql.connection.cursor()
    cur_client.execute('SELECT * FROM client WHERE id = %s', [id])
    client = cur_client.fetchall()
    _cities = sorted(cities, key=getKey)
    return render_template('./clientes/consultclient.html', client = client, gender = gender, departs = departs, cities = _cities, plan = plan, companies = company)

@app.route('/client/search', methods=['POST'])
def search_client():
    global session
    if request.method == 'POST':
        _, _, cities, _, _ = CUR()
        _cities = sorted(cities, key=getKey)
        idMuni = request.form['idMuni']
        month = request.form['month']
        if idMuni == 'null' and month == 'null':
            allclient = allclient_cur()
            return render_template('./clientes/showclient.html', client = allclient, cities = _cities, months = months)
        else:
            cur_client = mysql.connection.cursor()
            if idMuni != 'null' and month == 'null':
                cur_client.execute('SELECT * FROM client WHERE idMuni = %s', [idMuni])
            elif idMuni == 'null' and month != 'null':
                allclient = allclient_cur()
                id = Date(allclient, month)
                if id:
                    cur_client.execute('SELECT * FROM client WHERE id = %s', [id])
                else:
                    cur_client.execute('SELECT * FROM client WHERE id = %s', [month])
            else:
                allclient = allclient_cur()
                id = Date(allclient, month)
                if not id:
                    id = month
                cur_client.execute('SELECT * FROM client WHERE idMuni = %s AND id = %s', [idMuni, id])
            client = cur_client.fetchall()
            return render_template('./clientes/showclient.html', client = client, cities = _cities, months = months)

@app.route('/client/delete/<string:id>', methods=['POST'])
def delete_client(id):
    verify, _ = verify_user(request.method)
    if verify is True:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM client WHERE id = {0}'.format(id))
        mysql.connection.commit()
        flash('Cliente eliminado satifactoriamente')
        return redirect(url_for('Index'))
    else:
        flash(f'No se ha podido eliminar el cliente. Usuario y contrase??a incorrectos')
        return redirect(url_for('Index'))

@app.route('/client/edit/<id>', methods=['POST'])
def get_client(id):
    verify, _ = verify_user(request.method)
    if verify is True:
        gender, _, cities,plan,company = CUR()
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM client WHERE id = %s', [id])
        client = cur.fetchall()
        _cities = sorted(cities, key=getKey)
        return render_template('/clientes/editclient.html', client = client[0], gender = gender, cities = _cities, plan = plan, companies = company)
    else:
        flash(f'Usuario y contrase??a son incorrectos')
        return redirect(url_for('Index'))

@app.route('/client/update/<id>', methods = ['POST'])
def update_client(id):
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        dni = request.form['dni']
        date = request.form['date']
        idGender = request.form['idGender']
        tel = request.form['tel']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        idMuni = request.form['idMuni']
        idDepart = depart(idMuni)
        idPlan = request.form['idPlan']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE client 
            SET name = %s, 
            lastname = %s, 
            dni = %s, 
            date = %b, 
            idGender = %b, 
            tel = %s, 
            phone = %s, 
            email = %s, 
            address = %s, 
            idDepart = %b, 
            idMuni = %b,
            idPlan = %b
            WHERE id = %s
            """, (name, lastname, dni, date, idGender, tel, phone, email, address, idDepart, idMuni, idPlan, id))
        mysql.connection.commit()
        flash('Contacto editado satisfactoriamente')
        return redirect(url_for('Index'))

# PLANES

@app.route('/plan/add', methods=['POST', 'GET'])
def add_plan():
    verify, _ = verify_user(request.method)
    if verify is True:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM company')
        company = cur.fetchall()
        companies = sorted(company, key=getKey)
        return render_template('./planes/addplan.html', companies = companies)
    else:
        flash(f'Usuario y contrase??a son incorrectos')
        return redirect(url_for('Index'))

@app.route('/plan/save', methods=['POST'])
def save_plan():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        idComp = request.form['idComp']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO plans (name, description, idComp) VALUES (%s, %s, %b)', (name, description, idComp))
        mysql.connection.commit()
        flash('Plan a??adido satisfactoriamente')
        return redirect(url_for('Index'))

@app.route('/plan/consult')
def consult_plan():
    _,_,_,plan, company = CUR()
    return render_template('./planes/consultplan.html', planes = plan, companies = company)

@app.route('/plan/delete/<string:id>')
def delete_plan(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM plans WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Plan eliminado satifactoriamente')
    return redirect(url_for('Index'))

@app.route('/plan/edit/<id>')
def get_plan(id):
    cur_plan = mysql.connection.cursor()
    cur_plan.execute('SELECT * FROM plans WHERE id = %s', [id])
    plan = cur_plan.fetchall()
    cur_company = mysql.connection.cursor()
    cur_company.execute('SELECT * FROM company')
    company = cur_company.fetchall()
    companies = sorted(company, key=getKey)
    return render_template('/planes/editplan.html', plan = plan[0], companies = companies)

@app.route('/plan/update/<id>', methods = ['POST'])
def update_plan(id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        idComp = request.form['idComp']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE plans 
            SET name = %s, 
            description = %s, 
            idComp = %b 
            WHERE id = %s
            """, (name, description, idComp, id))
        mysql.connection.commit()
        flash('Plan editado satisfactoriamente')
        return redirect(url_for('Index'))

# EMPRESA

@app.route('/company/add', methods=['GET'])
def add_company():
    return render_template('./others/addcompany.html')

@app.route('/company/save', methods=['POST'])
def save_company():
    if request.method == 'POST':
        name = request.form['name']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO company (name) VALUES (%s)', [name])
        mysql.connection.commit()
        flash('Empresa a??adida satisfactoriamente')
        return redirect(url_for('add_company'))

# MUNICIPIOS

@app.route('/city/add', methods=['GET'])
def add_city():
    _,depart,_,_,_ = CUR()
    return render_template('./others/addcity.html', depart = depart)

@app.route('/city/save', methods=['POST'])
def save_city():
    if request.method == 'POST':
        name = request.form['name']
        idDepart = request.form['idDepart']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO city (name, idDepart) VALUES (%s, %b)', (name, idDepart))
        mysql.connection.commit()
        flash('Municipio a??adido satisfactoriamente')
        return redirect(url_for('add_city'))

@app.route('/logout')
def logout():
    global session
    session = None
    return redirect(url_for('Index'))

@app.route('/login', methods=['POST'])
def login():
    verify, user_login = verify_user(request.method)
    global session
    if verify is True:
        session = user_login
        return redirect(url_for('Index'))
    else:
        flash(f'El usuario y la contrase??a son incorrectos')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)