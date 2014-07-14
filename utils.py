# coding: utf-8

def extract_params():
    uri = request.uri
    method = request.method
    headers = request.headers
    body = request.arguments

    return uri, method, body, headers
