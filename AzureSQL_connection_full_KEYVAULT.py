import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


# Azure Key Vault and Secret Name settings
kv_name = "KEYVAULT NAME"
pw_secret_name = "SECRET NAME FOR PASSWORD"
user_secret_name = "SECRET NAME FOR USER"
db_secret_name = "SECRET NAME FOR DATABASE"
urlsvr_secret_name = "SECRET NAME FOR SERVER URL"
kv_url = f"https://{kv_name}.vault.azure.net/"

# Initialize default Azure credentials client
credential_client_pw = DefaultAzureCredential()

# Initialize the Azure Key Vault secrets client
secret_client_pw = SecretClient(vault_url=kv_url, credential=credential_client_pw)

# Get the secret value from Azure Key Vault
pw_secret_value = secret_client_pw.get_secret(pw_secret_name).value

credential_client_user = DefaultAzureCredential()
secret_client_user = SecretClient(vault_url=kv_url, credential=credential_client_user)
user_secret_value = secret_client_user.get_secret(user_secret_name).value

credential_client_db = DefaultAzureCredential()
secret_client_db = SecretClient(vault_url=kv_url, credential=credential_client_db)
db_secret_value = secret_client_db.get_secret(db_secret_name).value

credential_client_svr = DefaultAzureCredential()
secret_client_svr = SecretClient(vault_url=kv_url, credential=credential_client_svr)
svr_secret_value = secret_client_svr.get_secret(urlsvr_secret_name).value

# Azure SQL Database Settings
svr_url = svr_secret_value
db_name = db_secret_value
username = user_secret_value
pw = pw_secret_value

# Connection string
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
    # Establish the database connection
    conn = pyodbc.connect(connection_str)
    print("Connected!")
    
    # Close the connection
    conn.close()
    
except:
    raise Exception
