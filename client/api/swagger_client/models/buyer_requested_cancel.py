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


class BuyerRequestedCancel(object):
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
        'is_buyer_requested_cancel': 'str',
        'buyer_cancel_reason': 'str'
    }

    attribute_map = {
        'is_buyer_requested_cancel': 'IsBuyerRequestedCancel',
        'buyer_cancel_reason': 'BuyerCancelReason'
    }

    def __init__(self, is_buyer_requested_cancel=None, buyer_cancel_reason=None):  # noqa: E501
        """BuyerRequestedCancel - a model defined in Swagger"""  # noqa: E501

        self._is_buyer_requested_cancel = None
        self._buyer_cancel_reason = None
        self.discriminator = None

        if is_buyer_requested_cancel is not None:
            self.is_buyer_requested_cancel = is_buyer_requested_cancel
        if buyer_cancel_reason is not None:
            self.buyer_cancel_reason = buyer_cancel_reason

    @property
    def is_buyer_requested_cancel(self):
        """Gets the is_buyer_requested_cancel of this BuyerRequestedCancel.  # noqa: E501

        Indicate whether the buyer has requested cancellation.  **Possible Values**: `true`, `false`.  # noqa: E501

        :return: The is_buyer_requested_cancel of this BuyerRequestedCancel.  # noqa: E501
        :rtype: str
        """
        return self._is_buyer_requested_cancel

    @is_buyer_requested_cancel.setter
    def is_buyer_requested_cancel(self, is_buyer_requested_cancel):
        """Sets the is_buyer_requested_cancel of this BuyerRequestedCancel.

        Indicate whether the buyer has requested cancellation.  **Possible Values**: `true`, `false`.  # noqa: E501

        :param is_buyer_requested_cancel: The is_buyer_requested_cancel of this BuyerRequestedCancel.  # noqa: E501
        :type: str
        """

        self._is_buyer_requested_cancel = is_buyer_requested_cancel

    @property
    def buyer_cancel_reason(self):
        """Gets the buyer_cancel_reason of this BuyerRequestedCancel.  # noqa: E501

        The reason that the buyer requested cancellation.  # noqa: E501

        :return: The buyer_cancel_reason of this BuyerRequestedCancel.  # noqa: E501
        :rtype: str
        """
        return self._buyer_cancel_reason

    @buyer_cancel_reason.setter
    def buyer_cancel_reason(self, buyer_cancel_reason):
        """Sets the buyer_cancel_reason of this BuyerRequestedCancel.

        The reason that the buyer requested cancellation.  # noqa: E501

        :param buyer_cancel_reason: The buyer_cancel_reason of this BuyerRequestedCancel.  # noqa: E501
        :type: str
        """

        self._buyer_cancel_reason = buyer_cancel_reason

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
        if issubclass(BuyerRequestedCancel, dict):
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
        if not isinstance(other, BuyerRequestedCancel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
