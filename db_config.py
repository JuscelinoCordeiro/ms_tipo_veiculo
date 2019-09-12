from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'dimitri'
app.config['MYSQL_DATABASE_PASSWORD'] = '@!@#rf'
app.config['MYSQL_DATABASE_DB'] = 'ms_tipo_veiculo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)