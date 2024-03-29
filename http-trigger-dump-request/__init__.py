import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, msg: func.Out[str], msg2: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    msg.set('Message from http')

    msg2.set('Message from http')

    return func.HttpResponse(
        json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'get_body': req.get_body().decode()
        })
    )
