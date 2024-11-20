if __name__ == "__main__":
    print("Starting the Script...")

    from SellingPartnerAPISDK.auth import SPAPIConfig
    # User inputs their credentials in the config
    config = SPAPIConfig(
        client_id='amzn1.application-oa2-SellingPartnerAPISDK.029eabd19b744637bfef6510accd058b',
        client_secret = 'amzn1.oa2-cs.v1.297d22bf0447d84b1f33240d47cab210a11612e59c921bcbc5f05109bcebe843',
        refresh_token = """Atzr|IwEBIB5RgnPEIUYE6KxsIgMFyBi2dKPaeI5Gx4CnHu2C8zGY0sOUy_GJXrvTO539lIQfJXByGK37oeQdhvjke1kRiJdYuKGmP-YsrRoGZjyTN2PGq4YRkouloL7B2QXNAEO4Vv_nYhnwTLbEixrWPXCJ4kGkUUdgri21B5MQKQdOTPaBbFnzut9PT99xUhEnmSwDmggBpd9yUIL9OTzezTycn-oSH35888rxB8_jSao62F99_DrN5sqlSPSggz7nPduTJMKrcCIuffJt8YmQDDqFIFJfY0bgsNxTTRpUEeIGSPKcjbD6XdLHoJXbGKS0OJpNvQ4""",
        region="NA",  # Possible values NA, EU, FE, and SANDBOX
        scope = None # Required for grant_type='client_credentials' ; Possible values "sellingpartnerapi::notifications" and "sellingpartnerapi::migration"
    )

    from SellingPartnerAPISDK.spapi.spapiclient import SPAPIClient

    # Create the API Client
    print("Config and SellingPartnerAPISDK initialized...")
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

