import mysql.connector
from decouple import config

def get_connection():
  try:
      db = mysql.connector.connect(
          host=config('MYSQL_HOST'),
          user=config('MYSQL_USER'),
          password=config('MYSQL_PASSWORD'),
          database=config('MYSQL_DATABASE')
      )
      return db
  except print(0):
      pass