from rest_framework import serializers
from addresses.models import Person, PhoneNumber, Email, Address
from .email import EmailSerializer, BasicEmailSerializer
from .phone_number import PhoneNumberSerializer, BasicPhoneNumberSerializer
from .address import BasicAddressSerializer, AddressSerializer
from .person import PersonSerializer, PersonListSerializer, CreatePersonSerializer

__all__ = ['BasicEmailSerializer', 'BasicPhoneNumberSerializer', 'BasicAddressSerializer', 'AddressSerializer', 'PhoneNumberSerializer', 'EmailSerializer', 'PersonSerializer', 'PersonListSerializer', 'CreatePersonSerializer']