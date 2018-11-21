"""
  desa-api
  
  Copyright (c) 2018
  All rights reserved.
  Written by od3ng created on 21/11/18 20.11
  Email   : lepengdados@gmail.com
  Github  : 0d3ng
  Hp      : 085878554150
 """


def response_message(code, message, link, developer_message, data):
    """
    Response message using jsonify
    """
    response = {
        'code': code,
        'message': message,
        'link': link,
        'developerMessage': developer_message,
        'data': data
    }
    return response
