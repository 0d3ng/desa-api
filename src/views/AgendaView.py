from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.AgendaModel import AgendaModel, AgendaSchema
from ..util import response_message

agenda_api = Blueprint('agenda_api', __name__)
agenda_schema = AgendaSchema()


@agenda_api.route('/', methods=['GET'])
def get_all_agenda():
    """
    Get all agenda
    """
    agendas = AgendaModel.get_all_agenda()
    ser_agendas = agenda_schema.dump(agendas, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_agendas)
    return jsonify(res)


@agenda_api.route('/<int:id_agenda>', methods=['GET'])
def get_by_agenda(id_agenda):
    """
    Get a single agenda
    """
    agenda = AgendaModel.get_agenda_by_id(id_agenda=id_agenda)
    if not agenda:
        res = response_message(404, 'Fail', request.url, 'Agenda not found', None)
        return jsonify(res)
    ser_agendas = agenda_schema.dump(agenda).data
    res = response_message(200, 'Success', request.url, None, ser_agendas)
    return jsonify(res)


@agenda_api.route('/limit', methods=['GET'])
def get_agenda_limit():
    """
    Get a single agenda
    """
    agendas = AgendaModel.get_agenda_limit()
    ser_agendas = agenda_schema.dump(agendas, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_agendas)
    return jsonify(res)
