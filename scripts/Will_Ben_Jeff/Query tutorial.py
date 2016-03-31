# -*- coding: utf-8 -*-
"""
William Koehler


--------------------Query tutorial-----------------------
Must install mysql-connector-python to import this
Or install the connector from the mysql website.

create user tempuser at localhost with no password. Privledges, at least SELECT
"""

import mysql.connector

cnx = mysql.connector.connect(user='tempuser', password='',
                              host='127.0.0.1',
                              database='traces')
cursor = cnx.cursor()
         
query = ("SELECT id, src_ip, dst_ip, packets FROM traces.flows "
        "WHERE id BETWEEN %s AND %s")
        
cursor.execute(query, (1, 5))

for (id, src_ip, dst_ip, packets) in cursor:
  print((id, src_ip, dst_ip, packets))

cnx.close()