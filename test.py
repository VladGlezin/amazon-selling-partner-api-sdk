# Script tests library installed from whl file on a new python environment.To be tested from anywhere

print("Starting the Script...")

from SellingPartnerAPISDK.auth.credentials import SPAPIConfig
# User inputs their credentials in the config
config = SPAPIConfig(
    client_id='insert client client',
    client_secret='insert client secret',
    refresh_token='inset refresh token',
    region="NA", # Possible values NA, EU, FE, and SANDBOX
    scope=None
)

from SellingPartnerAPISDK.spapi.spapiclient import SPAPIClient

# Create the API Client
print("Config and client initialized...")
api_client = SPAPIClient(config)

marketplace_ids = ["ATVPDKIKX0DER"]
created_after = "2024-01-19T12:34:56.789012"

reports_api = api_client.get_api_client('ReportsApi')
orders_response = reports_api.get_reports(report_types=['GET_SALES_AND_TRAFFIC_REPORT', 'GET_VENDOR_SALES_REPORT'])
print("Orders API Response:")
print(orders_response)

orders_api = api_client.get_api_client('OrdersApi')
orders_response = orders_api.get_orders(marketplace_ids=marketplace_ids, created_after=created_after)
print("Orders API Response:")
print(orders_response)

