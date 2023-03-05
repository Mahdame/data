import connexion
import six

from swagger_server.models.create_data_request import CreateDataRequest  # noqa: E501
from swagger_server.models.create_data_response import CreateDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_data_response import GetDataResponse  # noqa: E501
from swagger_server.models.list_data_response import ListDataResponse  # noqa: E501
from swagger_server.models.update_data_request import UpdateDataRequest  # noqa: E501
from swagger_server import util


def create_data(body):  # noqa: E501
    """Create new Data

    This operation is used to create a new Data on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateDataResponse
    """
    if connexion.request.is_json:
        body = CreateDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_data(data_id):  # noqa: E501
    """Delete Data

    This operation is delete a Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_data(data_id):  # noqa: E501
    """Get a single Data&#x27;s info

    This operation is used to retrieve the details of a specific device. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: GetDataResponse
    """
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_data():  # noqa: E501
    """Get Data list

    This operation is used to retrieve a list of Data. # noqa: E501


    :rtype: ListDataResponse
    """
    return 'do some magic!'


def update_data(body, data_id):  # noqa: E501
    """Update Data&#x27;s attributes

    This operation is used to update some of the Data&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
