Currently an example on how to upload gathered facts from Windows hosts to a database

###### Example Variables ##########

Initial Connection Variables



Database Variables

you will need to pass these in as extra vars, or specify them in the fact_to_db.yml playbook

   instance_address: serverreporting.cferhetrt.ap-southeast-2.rds.amazonaws.com
   database_name: reporting
   pg_port: 5432
   fact_table_name: windowsserverfacts