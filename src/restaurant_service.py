import os
import psycopg2
import psycopg2.extras
from flask import Flask, request, jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_host = os.environ.get('CLOUD_SQL_HOST')

app = Flask(__name__)


@app.route('/')
def main():
    cnx = psycopg2.connect(dbname=db_name, user=db_user,
                           password=db_password, host=db_host)

    with cnx.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        grade = request.args['grade']
        cuisine = request.args['cuisine']
        cursor.execute('SELECT * FROM restaurant WHERE grade <= %s AND cuisine_description like %s',  # noqa: E501
                       (grade, cuisine))
        result = cursor.fetchall()

    cnx.commit()
    cnx.close()

    return jsonify(result)
