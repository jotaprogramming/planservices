from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask.wrappers import Request
from flask_mysqldb import MySQL

# MySql Connection
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='gestionclientes'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

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

@app.route('/')
def Index():
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

@app.route('/client/add', methods=['GET'])
def add_cliente():
    gender, _, cities,plan,company = CUR()
    _cities = sorted(cities, key=getKey)
    return render_template('./clientes/addclient.html', gender = gender, cities = _cities, plan = plan, companies = company)

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
        flash('Cliente añadido satisfactoriamente')
        return redirect(url_for('add_cliente'))

@app.route('/client/consult', methods=['POST'])
def consult_cliente():
    if request.method == 'POST':
        gender, departs, cities, plan, company = CUR()
        tel = request.form['tel']
        cur_client = mysql.connection.cursor()
        cur_client.execute('SELECT * FROM client WHERE tel = %s', [tel])
        client = cur_client.fetchall()
        if not tel:
            cur_allclient = mysql.connection.cursor()
            cur_allclient.execute('SELECT * FROM client')
            allclient = cur_allclient.fetchall()
            return render_template('./clientes/showclient.html', client = allclient)
        else:
            if not client:
                flash(f'El cliente con el número "{tel}" no existe')
                return redirect(url_for('Index'))
            else:
                return render_template('./clientes/consultclient.html', client = client, gender = gender, departs = departs, cities = cities, plan = plan, companies = company)

@app.route('/client/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM client WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado satifactoriamente')
    return redirect(url_for('Index'))

@app.route('/client/edit/<id>')
def get_client(id):
    gender, _, cities,plan,company = CUR()
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM client WHERE id = %s', [id])
    client = cur.fetchall()
    _cities = sorted(cities, key=getKey)
    return render_template('/clientes/editclient.html', client = client[0], gender = gender, cities = _cities, plan = plan, companies = company)

@app.route('/update/<id>', methods = ['POST'])
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

@app.route('/plan/add', methods=['GET'])
def add_plan():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM company')
    company = cur.fetchall()
    companies = sorted(company, key=getKey)
    return render_template('./planes/addplan.html', companies = companies)

@app.route('/plan/save', methods=['POST'])
def save_plan():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        idComp = request.form['idComp']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO plans (name, description, idComp) VALUES (%s, %s, %b)', (name, description, idComp))
        mysql.connection.commit()
        flash('Plan añadido satisfactoriamente')
        return redirect(url_for('add_plan'))

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

@app.route('/update/<id>', methods = ['POST'])
def update_plan(id):
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
            idMuni = %b
            WHERE id = %s
            """, (name, lastname, dni, date, idGender, tel, phone, email, address, idDepart, idMuni, id))
        mysql.connection.commit()
        flash('Contacto editado satisfactoriamente')
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
        flash('Empresa añadida satisfactoriamente')
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
        flash('Municipio añadido satisfactoriamente')
        return redirect(url_for('add_city'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)