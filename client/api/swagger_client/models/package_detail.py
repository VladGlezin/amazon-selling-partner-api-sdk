# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PackageDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'package_reference_id': 'PackageReferenceId',
        'carrier_code': 'str',
        'carrier_name': 'str',
        'shipping_method': 'str',
        'tracking_number': 'str',
        'ship_date': 'datetime',
        'ship_from_supply_source_id': 'str',
        'order_items': 'ConfirmShipmentOrderItemsList'
    }

    attribute_map = {
        'package_reference_id': 'packageReferenceId',
        'carrier_code': 'carrierCode',
        'carrier_name': 'carrierName',
        'shipping_method': 'shippingMethod',
        'tracking_number': 'trackingNumber',
        'ship_date': 'shipDate',
        'ship_from_supply_source_id': 'shipFromSupplySourceId',
        'order_items': 'orderItems'
    }

    def __init__(self, package_reference_id=None, carrier_code=None, carrier_name=None, shipping_method=None, tracking_number=None, ship_date=None, ship_from_supply_source_id=None, order_items=None):  # noqa: E501
        """PackageDetail - a model defined in Swagger"""  # noqa: E501

        self._package_reference_id = None
        self._carrier_code = None
        self._carrier_name = None
        self._shipping_method = None
        self._tracking_number = None
        self._ship_date = None
        self._ship_from_supply_source_id = None
        self._order_items = None
        self.discriminator = None

        self.package_reference_id = package_reference_id
        self.carrier_code = carrier_code
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if shipping_method is not None:
            self.shipping_method = shipping_method
        self.tracking_number = tracking_number
        self.ship_date = ship_date
        if ship_from_supply_source_id is not None:
            self.ship_from_supply_source_id = ship_from_supply_source_id
        self.order_items = order_items

    @property
    def package_reference_id(self):
        """Gets the package_reference_id of this PackageDetail.  # noqa: E501


        :return: The package_reference_id of this PackageDetail.  # noqa: E501
        :rtype: PackageReferenceId
        """
        return self._package_reference_id

    @package_reference_id.setter
    def package_reference_id(self, package_reference_id):
        """Sets the package_reference_id of this PackageDetail.


        :param package_reference_id: The package_reference_id of this PackageDetail.  # noqa: E501
        :type: PackageReferenceId
        """
        if package_reference_id is None:
            raise ValueError("Invalid value for `package_reference_id`, must not be `None`")  # noqa: E501

        self._package_reference_id = package_reference_id

    @property
    def carrier_code(self):
        """Gets the carrier_code of this PackageDetail.  # noqa: E501

        Identifies the carrier that will deliver the package. This field is required for all marketplaces. For more information, refer to the [`CarrierCode` announcement](https://developer-docs.amazon.com/sp-api/changelog/carriercode-value-required-in-shipment-confirmations-for-br-mx-ca-sg-au-in-jp-marketplaces).  # noqa: E501

        :return: The carrier_code of this PackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this PackageDetail.

        Identifies the carrier that will deliver the package. This field is required for all marketplaces. For more information, refer to the [`CarrierCode` announcement](https://developer-docs.amazon.com/sp-api/changelog/carriercode-value-required-in-shipment-confirmations-for-br-mx-ca-sg-au-in-jp-marketplaces).  # noqa: E501

        :param carrier_code: The carrier_code of this PackageDetail.  # noqa: E501
        :type: str
        """
        if carrier_code is None:
            raise ValueError("Invalid value for `carrier_code`, must not be `None`")  # noqa: E501

        self._carrier_code = carrier_code

    @property
    def carrier_name(self):
        """Gets the carrier_name of this PackageDetail.  # noqa: E501

        Carrier Name that will deliver the package. Required when `carrierCode` is \"Others\"   # noqa: E501

        :return: The carrier_name of this PackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this PackageDetail.

        Carrier Name that will deliver the package. Required when `carrierCode` is \"Others\"   # noqa: E501

        :param carrier_name: The carrier_name of this PackageDetail.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def shipping_method(self):
        """Gets the shipping_method of this PackageDetail.  # noqa: E501

        Ship method to be used for shipping the order.  # noqa: E501

        :return: The shipping_method of this PackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """Sets the shipping_method of this PackageDetail.

        Ship method to be used for shipping the order.  # noqa: E501

        :param shipping_method: The shipping_method of this PackageDetail.  # noqa: E501
        :type: str
        """

        self._shipping_method = shipping_method

    @property
    def tracking_number(self):
        """Gets the tracking_number of this PackageDetail.  # noqa: E501

        The tracking number used to obtain tracking and delivery information.  # noqa: E501

        :return: The tracking_number of this PackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this PackageDetail.

        The tracking number used to obtain tracking and delivery information.  # noqa: E501

        :param tracking_number: The tracking_number of this PackageDetail.  # noqa: E501
        :type: str
        """
        if tracking_number is None:
            raise ValueError("Invalid value for `tracking_number`, must not be `None`")  # noqa: E501

        self._tracking_number = tracking_number

    @property
    def ship_date(self):
        """Gets the ship_date of this PackageDetail.  # noqa: E501

        The shipping date for the package. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date/time format.  # noqa: E501

        :return: The ship_date of this PackageDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this PackageDetail.

        The shipping date for the package. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date/time format.  # noqa: E501

        :param ship_date: The ship_date of this PackageDetail.  # noqa: E501
        :type: datetime
        """
        if ship_date is None:
            raise ValueError("Invalid value for `ship_date`, must not be `None`")  # noqa: E501

        self._ship_date = ship_date

    @property
    def ship_from_supply_source_id(self):
        """Gets the ship_from_supply_source_id of this PackageDetail.  # noqa: E501

        The unique identifier for the supply source.  # noqa: E501

        :return: The ship_from_supply_source_id of this PackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._ship_from_supply_source_id

    @ship_from_supply_source_id.setter
    def ship_from_supply_source_id(self, ship_from_supply_source_id):
        """Sets the ship_from_supply_source_id of this PackageDetail.

        The unique identifier for the supply source.  # noqa: E501

        :param ship_from_supply_source_id: The ship_from_supply_source_id of this PackageDetail.  # noqa: E501
        :type: str
        """

        self._ship_from_supply_source_id = ship_from_supply_source_id

    @property
    def order_items(self):
        """Gets the order_items of this PackageDetail.  # noqa: E501

        The list of order items and quantities to be updated.  # noqa: E501

        :return: The order_items of this PackageDetail.  # noqa: E501
        :rtype: ConfirmShipmentOrderItemsList
        """
        return self._order_items

    @order_items.setter
    def order_items(self, order_items):
        """Sets the order_items of this PackageDetail.

        The list of order items and quantities to be updated.  # noqa: E501

        :param order_items: The order_items of this PackageDetail.  # noqa: E501
        :type: ConfirmShipmentOrderItemsList
        """
        if order_items is None:
            raise ValueError("Invalid value for `order_items`, must not be `None`")  # noqa: E501

        self._order_items = order_items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PackageDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PackageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
