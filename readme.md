Currently an example on how to upload gathered facts from Windows hosts to a database

###### Example Variables ##########

#########################################################

Database Variables

   You will need to pass these in as extra vars, or specify them in the fact_to_db.yml playbook.  Change the values to suit...

      instance_address: serverreporting.cferhetrt.ap-southeast-2.rds.amazonaws.com
      database_name: reporting
      pg_port: 5432
      fact_table_name: windowsserverfacts

   You will need to pass these in, either vars in encrypted ansible-vault vars file..   Or from a tower credential

      pg_user: postgres
      pg_pass: P@ssword123

#########################################################

Ansible Tower (Extra Credential Config)

    input configuration:
      fields:
        - id: pg_user
          type: string
          label: Username
        - id: pg_pass
          type: string
          label: Password
          secret: true
      required:
        - pg_user
        - pg_pass


    Injector Configuration

      extra_vars:
        pg_pass: '{{ pg_pass }}'
        pg_user: '{{ pg_user }}'
