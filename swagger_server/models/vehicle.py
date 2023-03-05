# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class Vehicle(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, vehicle_id: str=None, data_owner: str=None, telemetry_profile: str=None, current_driver: str=None, number_plate: str=None, vin: str=None, color: str=None):  # noqa: E501
        """Vehicle - a model defined in Swagger

        :param vehicle_id: The vehicle_id of this Vehicle.  # noqa: E501
        :type vehicle_id: str
        :param data_owner: The data_owner of this Vehicle.  # noqa: E501
        :type data_owner: str
        :param telemetry_profile: The telemetry_profile of this Vehicle.  # noqa: E501
        :type telemetry_profile: str
        :param current_driver: The current_driver of this Vehicle.  # noqa: E501
        :type current_driver: str
        :param number_plate: The number_plate of this Vehicle.  # noqa: E501
        :type number_plate: str
        :param vin: The vin of this Vehicle.  # noqa: E501
        :type vin: str
        :param color: The color of this Vehicle.  # noqa: E501
        :type color: str
        """
        self.swagger_types = {
            'vehicle_id': str,
            'data_owner': str,
            'telemetry_profile': str,
            'current_driver': str,
            'number_plate': str,
            'vin': str,
            'color': str
        }

        self.attribute_map = {
            'vehicle_id': 'vehicleId',
            'data_owner': 'dataOwner',
            'telemetry_profile': 'telemetryProfile',
            'current_driver': 'currentDriver',
            'number_plate': 'numberPlate',
            'vin': 'vin',
            'color': 'color'
        }
        self._vehicle_id = vehicle_id
        self._data_owner = data_owner
        self._telemetry_profile = telemetry_profile
        self._current_driver = current_driver
        self._number_plate = number_plate
        self._vin = vin
        self._color = color

    @classmethod
    def from_dict(cls, dikt) -> 'Vehicle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Vehicle of this Vehicle.  # noqa: E501
        :rtype: Vehicle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vehicle_id(self) -> str:
        """Gets the vehicle_id of this Vehicle.


        :return: The vehicle_id of this Vehicle.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: str):
        """Sets the vehicle_id of this Vehicle.


        :param vehicle_id: The vehicle_id of this Vehicle.
        :type vehicle_id: str
        """

        self._vehicle_id = vehicle_id

    @property
    def data_owner(self) -> str:
        """Gets the data_owner of this Vehicle.

        Vehicle's owner  # noqa: E501

        :return: The data_owner of this Vehicle.
        :rtype: str
        """
        return self._data_owner

    @data_owner.setter
    def data_owner(self, data_owner: str):
        """Sets the data_owner of this Vehicle.

        Vehicle's owner  # noqa: E501

        :param data_owner: The data_owner of this Vehicle.
        :type data_owner: str
        """

        self._data_owner = data_owner

    @property
    def telemetry_profile(self) -> str:
        """Gets the telemetry_profile of this Vehicle.

        Telemtry profile  # noqa: E501

        :return: The telemetry_profile of this Vehicle.
        :rtype: str
        """
        return self._telemetry_profile

    @telemetry_profile.setter
    def telemetry_profile(self, telemetry_profile: str):
        """Sets the telemetry_profile of this Vehicle.

        Telemtry profile  # noqa: E501

        :param telemetry_profile: The telemetry_profile of this Vehicle.
        :type telemetry_profile: str
        """

        self._telemetry_profile = telemetry_profile

    @property
    def current_driver(self) -> str:
        """Gets the current_driver of this Vehicle.

        Current driver of the vehicle  # noqa: E501

        :return: The current_driver of this Vehicle.
        :rtype: str
        """
        return self._current_driver

    @current_driver.setter
    def current_driver(self, current_driver: str):
        """Sets the current_driver of this Vehicle.

        Current driver of the vehicle  # noqa: E501

        :param current_driver: The current_driver of this Vehicle.
        :type current_driver: str
        """

        self._current_driver = current_driver

    @property
    def number_plate(self) -> str:
        """Gets the number_plate of this Vehicle.

        Number plate  # noqa: E501

        :return: The number_plate of this Vehicle.
        :rtype: str
        """
        return self._number_plate

    @number_plate.setter
    def number_plate(self, number_plate: str):
        """Sets the number_plate of this Vehicle.

        Number plate  # noqa: E501

        :param number_plate: The number_plate of this Vehicle.
        :type number_plate: str
        """

        self._number_plate = number_plate

    @property
    def vin(self) -> str:
        """Gets the vin of this Vehicle.

        Vehicle Identification Number  # noqa: E501

        :return: The vin of this Vehicle.
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin: str):
        """Sets the vin of this Vehicle.

        Vehicle Identification Number  # noqa: E501

        :param vin: The vin of this Vehicle.
        :type vin: str
        """

        self._vin = vin

    @property
    def color(self) -> str:
        """Gets the color of this Vehicle.

        Vehicle's color  # noqa: E501

        :return: The color of this Vehicle.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color: str):
        """Sets the color of this Vehicle.

        Vehicle's color  # noqa: E501

        :param color: The color of this Vehicle.
        :type color: str
        """

        self._color = color