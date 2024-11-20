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


class BusinessHours(object):
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
        'day_of_week': 'str',
        'open_intervals': 'list[OpenInterval]'
    }

    attribute_map = {
        'day_of_week': 'DayOfWeek',
        'open_intervals': 'OpenIntervals'
    }

    def __init__(self, day_of_week=None, open_intervals=None):  # noqa: E501
        """BusinessHours - a model defined in Swagger"""  # noqa: E501

        self._day_of_week = None
        self._open_intervals = None
        self.discriminator = None

        if day_of_week is not None:
            self.day_of_week = day_of_week
        if open_intervals is not None:
            self.open_intervals = open_intervals

    @property
    def day_of_week(self):
        """Gets the day_of_week of this BusinessHours.  # noqa: E501

        Day of the week.  # noqa: E501

        :return: The day_of_week of this BusinessHours.  # noqa: E501
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this BusinessHours.

        Day of the week.  # noqa: E501

        :param day_of_week: The day_of_week of this BusinessHours.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]  # noqa: E501
        if day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `day_of_week` ({0}), must be one of {1}"  # noqa: E501
                .format(day_of_week, allowed_values)
            )

        self._day_of_week = day_of_week

    @property
    def open_intervals(self):
        """Gets the open_intervals of this BusinessHours.  # noqa: E501

        Time window during the day when the business is open.  # noqa: E501

        :return: The open_intervals of this BusinessHours.  # noqa: E501
        :rtype: list[OpenInterval]
        """
        return self._open_intervals

    @open_intervals.setter
    def open_intervals(self, open_intervals):
        """Sets the open_intervals of this BusinessHours.

        Time window during the day when the business is open.  # noqa: E501

        :param open_intervals: The open_intervals of this BusinessHours.  # noqa: E501
        :type: list[OpenInterval]
        """

        self._open_intervals = open_intervals

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
        if issubclass(BusinessHours, dict):
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
        if not isinstance(other, BusinessHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other