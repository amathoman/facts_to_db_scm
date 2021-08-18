#Facts2DB Usage
#7 Parameters
#1 Directory containing facts files
#2 Destination DB table name for the facts
#3 DB Host, 4 DB Database,  5 DB Username, 6 DB Password, 7 DB Port 

import os
import json
import psycopg2
import sys


#grab the parameters should add some error checking
factfiledirectory = sys.argv[1] 
dbTableName = sys.argv[2] 

#connect to db
dbConn = psycopg2.connect(
    host=sys.argv[3],
    database=sys.argv[4],
    user=sys.argv[5],
    password=sys.argv[6],
    port = sys.argv[7])

dbCursor = dbConn.cursor()

#Only drop and create table first time through
createTable = True

#Loop through list of fact files and insert fact into DB
for filename in os.listdir(factfiledirectory):
    print("reading fact file %s" % (filename))
    f = open(os.path.join(factfiledirectory, filename),)
  
    # returns JSON object as a dictionary
    data = json.load(f)
    facts_data_dictionary = data['ansible_facts'] 
      
    #if first time in drop and create facts table
    if createTable:
        columns_create = ', '.join( str(x) + " varchar(1000)" for x in facts_data_dictionary.keys())
        sql = "DROP TABLE IF EXISTS public.%s " % (dbTableName)
        dbCursor.execute(sql)
        sql = "CREATE TABLE public.%s ( %s )" % (dbTableName, columns_create)
        print ("creating fact table " + dbTableName)
        dbCursor.execute(sql)
        dbCursor.execute('commit')
        createTable = False

    #Loop through dictionary keys and values to get columns and data for inserts
    columns_insert = ', '.join(str(x) for x in facts_data_dictionary.keys())
    values = ', '.join("'" + str(x).replace("'", '"') + "'" for x in facts_data_dictionary.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (dbTableName, columns_insert, values)
    dbCursor.execute(sql)
    print ("Inserting fact row " + filename)

    f.close()

dbCursor.execute('commit')
dbConn.close()