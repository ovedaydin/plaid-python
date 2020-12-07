# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class Owner(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'names': 'list[str]',
        'phone_numbers': 'list[PhoneNumber]',
        'emails': 'list[Email]',
        'addresses': 'list[Address]'
    }

    attribute_map = {
        'names': 'names',
        'phone_numbers': 'phone_numbers',
        'emails': 'emails',
        'addresses': 'addresses'
    }

    def __init__(self, names=None, phone_numbers=None, emails=None, addresses=None, local_vars_configuration=None):  # noqa: E501
        """Owner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._names = None
        self._phone_numbers = None
        self._emails = None
        self._addresses = None
        self.discriminator = None

        if names is not None:
            self.names = names
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if emails is not None:
            self.emails = emails
        if addresses is not None:
            self.addresses = addresses

    @property
    def names(self):
        """Gets the names of this Owner.  # noqa: E501

        A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. If the name of a business is reported, please contact Plaid Support.  In the case of a joint account, the names of all account holders will be reported.  If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account's `names` array.  # noqa: E501

        :return: The names of this Owner.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this Owner.

        A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. If the name of a business is reported, please contact Plaid Support.  In the case of a joint account, the names of all account holders will be reported.  If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account's `names` array.  # noqa: E501

        :param names: The names of this Owner.  # noqa: E501
        :type names: list[str]
        """

        self._names = names

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this Owner.  # noqa: E501

        A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.  # noqa: E501

        :return: The phone_numbers of this Owner.  # noqa: E501
        :rtype: list[PhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this Owner.

        A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.  # noqa: E501

        :param phone_numbers: The phone_numbers of this Owner.  # noqa: E501
        :type phone_numbers: list[PhoneNumber]
        """

        self._phone_numbers = phone_numbers

    @property
    def emails(self):
        """Gets the emails of this Owner.  # noqa: E501

        A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.  # noqa: E501

        :return: The emails of this Owner.  # noqa: E501
        :rtype: list[Email]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Owner.

        A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.  # noqa: E501

        :param emails: The emails of this Owner.  # noqa: E501
        :type emails: list[Email]
        """

        self._emails = emails

    @property
    def addresses(self):
        """Gets the addresses of this Owner.  # noqa: E501

        Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.  # noqa: E501

        :return: The addresses of this Owner.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Owner.

        Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.  # noqa: E501

        :param addresses: The addresses of this Owner.  # noqa: E501
        :type addresses: list[Address]
        """

        self._addresses = addresses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Owner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Owner):
            return True

        return self.to_dict() != other.to_dict()