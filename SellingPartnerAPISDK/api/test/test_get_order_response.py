# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.get_order_response import GetOrderResponse  # noqa: E501
from swagger_client.rest import ApiException


class TestGetOrderResponse(unittest.TestCase):
    """GetOrderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetOrderResponse(self):
        """Test GetOrderResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.get_order_response.GetOrderResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
