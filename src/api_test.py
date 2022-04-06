import os
from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json

from main import JWTGenerator

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

jwt = JWTGenerator(account = env["ACCOUNT"], user = env["S_USER"],\
    private_key_file_path = env["P8_PATH"]+"/rsa_key.p8",\
        private_key_passphrase = env["PRIVATE_KEY_PASSPHRASE"])

jwt = token
header = {"Authorization": "Bearer " + jwt,\
        "Content-Type": "application/json",\
            "Accept": "application/json",\
                "X-Snowflake-Authorization-Token-Type": "KEYPAIR_JWT"}

sql = "select * from testdata" 
my_data = {"statement": sql, "timeout": 60,\
        "resultSetMetaData": {"format": "jsonv2"},\
            "warehouse": env["WAREHOUSE"],\
                "database": env["DATABASE"],\
                    "schema": env["SCHEMA"]}
 
url = 'https://'+env["ACCOUNT"]+'/api/statements'
 
r = requests.post(url, headers = header, json=my_data)
json.loads(r.text)