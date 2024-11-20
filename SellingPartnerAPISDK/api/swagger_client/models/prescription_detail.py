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


class PrescriptionDetail(object):
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
        'prescription_id': 'str',
        'expiration_date': 'datetime',
        'written_quantity': 'int',
        'total_refills_authorized': 'int',
        'refills_remaining': 'int',
        'clinic_id': 'str',
        'usage_instructions': 'str'
    }

    attribute_map = {
        'prescription_id': 'prescriptionId',
        'expiration_date': 'expirationDate',
        'written_quantity': 'writtenQuantity',
        'total_refills_authorized': 'totalRefillsAuthorized',
        'refills_remaining': 'refillsRemaining',
        'clinic_id': 'clinicId',
        'usage_instructions': 'usageInstructions'
    }

    def __init__(self, prescription_id=None, expiration_date=None, written_quantity=None, total_refills_authorized=None, refills_remaining=None, clinic_id=None, usage_instructions=None):  # noqa: E501
        """PrescriptionDetail - a model defined in Swagger"""  # noqa: E501

        self._prescription_id = None
        self._expiration_date = None
        self._written_quantity = None
        self._total_refills_authorized = None
        self._refills_remaining = None
        self._clinic_id = None
        self._usage_instructions = None
        self.discriminator = None

        self.prescription_id = prescription_id
        self.expiration_date = expiration_date
        self.written_quantity = written_quantity
        self.total_refills_authorized = total_refills_authorized
        self.refills_remaining = refills_remaining
        self.clinic_id = clinic_id
        self.usage_instructions = usage_instructions

    @property
    def prescription_id(self):
        """Gets the prescription_id of this PrescriptionDetail.  # noqa: E501

        The identifier for the prescription used to verify the regulated product.  # noqa: E501

        :return: The prescription_id of this PrescriptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, prescription_id):
        """Sets the prescription_id of this PrescriptionDetail.

        The identifier for the prescription used to verify the regulated product.  # noqa: E501

        :param prescription_id: The prescription_id of this PrescriptionDetail.  # noqa: E501
        :type: str
        """
        if prescription_id is None:
            raise ValueError("Invalid value for `prescription_id`, must not be `None`")  # noqa: E501

        self._prescription_id = prescription_id

    @property
    def expiration_date(self):
        """Gets the expiration_date of this PrescriptionDetail.  # noqa: E501

        The expiration date of the prescription used to verify the regulated product, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.  # noqa: E501

        :return: The expiration_date of this PrescriptionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this PrescriptionDetail.

        The expiration date of the prescription used to verify the regulated product, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.  # noqa: E501

        :param expiration_date: The expiration_date of this PrescriptionDetail.  # noqa: E501
        :type: datetime
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def written_quantity(self):
        """Gets the written_quantity of this PrescriptionDetail.  # noqa: E501

        The number of units in each fill as provided in the prescription.  # noqa: E501

        :return: The written_quantity of this PrescriptionDetail.  # noqa: E501
        :rtype: int
        """
        return self._written_quantity

    @written_quantity.setter
    def written_quantity(self, written_quantity):
        """Sets the written_quantity of this PrescriptionDetail.

        The number of units in each fill as provided in the prescription.  # noqa: E501

        :param written_quantity: The written_quantity of this PrescriptionDetail.  # noqa: E501
        :type: int
        """
        if written_quantity is None:
            raise ValueError("Invalid value for `written_quantity`, must not be `None`")  # noqa: E501
        if written_quantity is not None and written_quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `written_quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._written_quantity = written_quantity

    @property
    def total_refills_authorized(self):
        """Gets the total_refills_authorized of this PrescriptionDetail.  # noqa: E501

        The total number of refills written in the original prescription used to verify the regulated product. If a prescription originally had no refills, this value must be 0.  # noqa: E501

        :return: The total_refills_authorized of this PrescriptionDetail.  # noqa: E501
        :rtype: int
        """
        return self._total_refills_authorized

    @total_refills_authorized.setter
    def total_refills_authorized(self, total_refills_authorized):
        """Sets the total_refills_authorized of this PrescriptionDetail.

        The total number of refills written in the original prescription used to verify the regulated product. If a prescription originally had no refills, this value must be 0.  # noqa: E501

        :param total_refills_authorized: The total_refills_authorized of this PrescriptionDetail.  # noqa: E501
        :type: int
        """
        if total_refills_authorized is None:
            raise ValueError("Invalid value for `total_refills_authorized`, must not be `None`")  # noqa: E501
        if total_refills_authorized is not None and total_refills_authorized < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_refills_authorized`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_refills_authorized = total_refills_authorized

    @property
    def refills_remaining(self):
        """Gets the refills_remaining of this PrescriptionDetail.  # noqa: E501

        The number of refills remaining for the prescription used to verify the regulated product. If a prescription originally had 10 total refills, this value must be `10` for the first order, `9` for the second order, and `0` for the eleventh order. If a prescription originally had no refills, this value must be 0.  # noqa: E501

        :return: The refills_remaining of this PrescriptionDetail.  # noqa: E501
        :rtype: int
        """
        return self._refills_remaining

    @refills_remaining.setter
    def refills_remaining(self, refills_remaining):
        """Sets the refills_remaining of this PrescriptionDetail.

        The number of refills remaining for the prescription used to verify the regulated product. If a prescription originally had 10 total refills, this value must be `10` for the first order, `9` for the second order, and `0` for the eleventh order. If a prescription originally had no refills, this value must be 0.  # noqa: E501

        :param refills_remaining: The refills_remaining of this PrescriptionDetail.  # noqa: E501
        :type: int
        """
        if refills_remaining is None:
            raise ValueError("Invalid value for `refills_remaining`, must not be `None`")  # noqa: E501
        if refills_remaining is not None and refills_remaining < 0:  # noqa: E501
            raise ValueError("Invalid value for `refills_remaining`, must be a value greater than or equal to `0`")  # noqa: E501

        self._refills_remaining = refills_remaining

    @property
    def clinic_id(self):
        """Gets the clinic_id of this PrescriptionDetail.  # noqa: E501

        The identifier for the clinic which provided the prescription used to verify the regulated product.  # noqa: E501

        :return: The clinic_id of this PrescriptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._clinic_id

    @clinic_id.setter
    def clinic_id(self, clinic_id):
        """Sets the clinic_id of this PrescriptionDetail.

        The identifier for the clinic which provided the prescription used to verify the regulated product.  # noqa: E501

        :param clinic_id: The clinic_id of this PrescriptionDetail.  # noqa: E501
        :type: str
        """
        if clinic_id is None:
            raise ValueError("Invalid value for `clinic_id`, must not be `None`")  # noqa: E501

        self._clinic_id = clinic_id

    @property
    def usage_instructions(self):
        """Gets the usage_instructions of this PrescriptionDetail.  # noqa: E501

        The instructions for the prescription as provided by the approver of the regulated product.  # noqa: E501

        :return: The usage_instructions of this PrescriptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._usage_instructions

    @usage_instructions.setter
    def usage_instructions(self, usage_instructions):
        """Sets the usage_instructions of this PrescriptionDetail.

        The instructions for the prescription as provided by the approver of the regulated product.  # noqa: E501

        :param usage_instructions: The usage_instructions of this PrescriptionDetail.  # noqa: E501
        :type: str
        """
        if usage_instructions is None:
            raise ValueError("Invalid value for `usage_instructions`, must not be `None`")  # noqa: E501

        self._usage_instructions = usage_instructions

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
        if issubclass(PrescriptionDetail, dict):
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
        if not isinstance(other, PrescriptionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other