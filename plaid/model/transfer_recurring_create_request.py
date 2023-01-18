"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.ach_class import ACHClass
    from plaid.model.transfer_device import TransferDevice
    from plaid.model.transfer_network import TransferNetwork
    from plaid.model.transfer_recurring_idempotency_key import TransferRecurringIdempotencyKey
    from plaid.model.transfer_recurring_schedule import TransferRecurringSchedule
    from plaid.model.transfer_type import TransferType
    from plaid.model.transfer_user_in_request import TransferUserInRequest
    globals()['ACHClass'] = ACHClass
    globals()['TransferDevice'] = TransferDevice
    globals()['TransferNetwork'] = TransferNetwork
    globals()['TransferRecurringIdempotencyKey'] = TransferRecurringIdempotencyKey
    globals()['TransferRecurringSchedule'] = TransferRecurringSchedule
    globals()['TransferType'] = TransferType
    globals()['TransferUserInRequest'] = TransferUserInRequest


class TransferRecurringCreateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'access_token': (str,),  # noqa: E501
            'idempotency_key': (TransferRecurringIdempotencyKey,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'type': (TransferType,),  # noqa: E501
            'network': (TransferNetwork,),  # noqa: E501
            'amount': (str,),  # noqa: E501
            'user_present': (bool, none_type,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'schedule': (TransferRecurringSchedule,),  # noqa: E501
            'user': (TransferUserInRequest,),  # noqa: E501
            'device': (TransferDevice,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'ach_class': (ACHClass,),  # noqa: E501
            'iso_currency_code': (str,),  # noqa: E501
            'test_clock_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'access_token': 'access_token',  # noqa: E501
        'idempotency_key': 'idempotency_key',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'network': 'network',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'user_present': 'user_present',  # noqa: E501
        'description': 'description',  # noqa: E501
        'schedule': 'schedule',  # noqa: E501
        'user': 'user',  # noqa: E501
        'device': 'device',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'ach_class': 'ach_class',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'test_clock_id': 'test_clock_id',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, access_token, idempotency_key, account_id, type, network, amount, user_present, description, schedule, user, device, *args, **kwargs):  # noqa: E501
        """TransferRecurringCreateRequest - a model defined in OpenAPI

        Args:
            access_token (str): The Plaid `access_token` for the account that will be debited or credited. Required if not using `payment_profile_token`.
            idempotency_key (TransferRecurringIdempotencyKey):
            account_id (str): The Plaid `account_id` for the account that will be debited or credited. Required if not using `payment_profile_token`.
            type (TransferType):
            network (TransferNetwork):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").
            user_present (bool, none_type): If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.
            description (str): The description of the recurring transfer.
            schedule (TransferRecurringSchedule):
            user (TransferUserInRequest):
            device (TransferDevice):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            ach_class (ACHClass): [optional]  # noqa: E501
            iso_currency_code (str): The currency of the transfer amount. The default value is \"USD\".. [optional]  # noqa: E501
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.access_token = access_token
        self.idempotency_key = idempotency_key
        self.account_id = account_id
        self.type = type
        self.network = network
        self.amount = amount
        self.user_present = user_present
        self.description = description
        self.schedule = schedule
        self.user = user
        self.device = device
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)