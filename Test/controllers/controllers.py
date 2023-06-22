# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import logging
import json
from datetime import datetime
import werkzeug.wrappers
from odoo.http import request
import base64
import os
import gcsfs
from datetime import date, datetime
import traceback

from library.logging import logging
from config import config_broker

# INIT LOG
logger = None
logger = logging.init_log(logger, __name__)

class testing(http.Controller):

    @http.route('/api/v1.0/testing', csrf=False, type='json',
        auth='none', methods=['POST'], cors='*')
    def testing(self, **kw):
        try:
            logger.info("start testing...")
            header = request.httprequest.headers
            req_body = json.loads(request.httprequest.data.decode('utf-8'))

            logger.info("end testing.")

            return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response={
                    'message': 'Success !',
                },
            )

        except Exception as ex:
            logger.error(ex)
            logger.info("end.")
            return werkzeug.wrappers.Response(
                status=404,
                content_type='application/json; charset=utf-8',
                response={
                    'message': str(ex),
                },
            )
    
    @http.route('/api/v1.0/testing', csrf=False, type='http',
                auth='public', methods=['OPTIONS'])
    def option_testing(self, id=None, **kw):
        headers = {
            'Access-Control-Allow-Headers': 'apikey,Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        }
        return werkzeug.wrappers.Response(
            status=200,
            content_type='application/json',
            response={},
            headers=headers
        )