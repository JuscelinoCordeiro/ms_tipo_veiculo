import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add_tipo_veiculo():
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		_json = request.json
		_tipo = _json['tipo']
		# validate the received values
		if _tipo and request.method == 'POST':
			# save edits
			sql = "INSERT INTO tipo_veiculo(tipo) VALUES(%s)"
			data = (_tipo)
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('1')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		
@app.route('/tipo_veiculos')
def tipo_veiculos():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, tipo FROM tipo_veiculo")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/tipo_veiculos/<int:id>')
def tipo_veiculo(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, tipo FROM tipo_veiculo WHERE id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def update_tipo_veiculo():
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		_json = request.json
		_id = _json['id']
		_tipo = _json['tipo']
		# validate the received values
		if _tipo and _id and request.method == 'PUT':
			# save edits
			sql = "UPDATE tipo_veiculo SET tipo=%s WHERE id=%s"
			data = (_tipo, _id)			
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('1')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_tipo_veiculo(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tipo_veiculo WHERE id=%s", (id,))
		conn.commit()
		resp = jsonify('1')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
	app.debug = True
	#app.run(host='0.0.0.0')
	app.run()
