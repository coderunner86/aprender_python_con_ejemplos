#Automatizacion de reportes con Python
#Caso de facturas de una tienda online
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import mysql.connector as mariadb
import sys

##rear conexion 
conn = mariadb.connect(
  user = "root",
  password = "1234",
  host = "localhost"
  port = 3306,
  database = "see_test"
)
