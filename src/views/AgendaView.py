from flask import request, json, Response, Blueprint, g
from ..models.AgendaModel import AgendaModel, AgendaSchema

agenda_api = Blueprint('agenda_api', __name__)
agenda_schema = AgendaSchema()


@agenda_api.route('/', methods=['GET'])
def get_all_agenda():
    """
    Get all agenda
    """
    agendas = AgendaModel.get_all_agenda()
    ser_agendas = agenda_schema.dump(agendas, many=True).data
    return custom_response(ser_agendas, 200)


@agenda_api.route('/<int:id_agenda>', methods=['GET'])
def get_by_agenda(id_agenda):
    """
    Get a single agenda
    """
    agenda = AgendaModel.get_agenda_by_id(id_agenda=id_agenda)
    if not agenda:
        return custom_response({'error': 'agenda not found'}, 404)
    ser_agendas = agenda_schema.dump(agenda).data
    return custom_response(ser_agendas, 200)


@agenda_api.route('/limit', methods=['GET'])
def get_agenda_limit():
    """
    Get a single agenda
    """
    agendas = AgendaModel.get_agenda_limit()
    ser_agendas = agenda_schema.dump(agendas, many=True).data
    return custom_response(ser_agendas, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
