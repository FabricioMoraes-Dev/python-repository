import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

kv_name = "KEYVAULT NAME"
secret_name = "SECRET NAME"

credential_client = DefaultAzureCredential()

kv_url = f"https://{kv_name}.vault.azure.net/"
secret_client = SecretClient(vault_url=kv_url, credential=credential_client)

secret_value = secret_client.get_secret(secret_name).value

svr_url = "SERVER NAME.database.windows.net"
db_name = "DATABASE NAME"
username = "USER NAME"
pw = secret_value

connection_str = (
    f'''Driver={'ODBC Driver 18 for SQL Server'};
    Server={svr_url};
    Database={db_name};
    UID={username};
    Pwd={pw};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;''')

try:
    conn = pyodbc.connect(connection_str)
    print("Connected!")
    
except:
    raise Exception
