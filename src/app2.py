
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config


app=Flask(__name__)

con=MySQL(app)


@app.route('/alumnos', methods=['GET'])
def list_alumnos():
    try:
        cursor=con.connection.cursor()
        sql='select * from alumnos'
        cursor.execute(sql)
        datos=cursor.fetchall()
        listAlum=[]
        for fila in datos:
            alum={'matricula': fila[0], 'nombre':fila[1], 'apaterno':fila[2],
            'amaterno':fila[3], 'correo':fila[4]}
            listAlum.append(alum)

        #print(listAlum)
        return jsonify({'Alumnos': listAlum, ' mensaje':'lista de alumnos'})
    
    except Exception as ex:
        return jsonify({'mensaje': '{}'.format(ex)})


@app.route('/alumnos/<int:mat>', methods=['GET'])
def leer_alumno(mat):
    try:
            cursor=con.connection.cursor()
            sql="select * from alumnos where matricula= '{0}'".format(mat)
            cursor.execute(sql)
            datos=cursor.fetchone()
            if datos!=None:
                alum=alum={'matricula': fila[0], 'nombre':fila[1], 'apaterno':fila[2],
                'amaterno':fila[3], 'correo':fila[4]}
                return jsonify({'Alumnos': alum, ' mensaje':'el alumno es'})
        except Exception as ex:
            return jsonify({'mensaje': '{}'.format(ex)})
def pagina_no_encontrada(error):
    return '<h1> Pagina no encontrada unu </h1>', 404

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()