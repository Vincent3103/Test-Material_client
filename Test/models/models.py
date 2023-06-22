# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, time, timedelta
from odoo.addons.resource.models.resource import float_to_time, HOURS_PER_DAY
from pytz import timezone, UTC
from library.logging import logging
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import http.client
import json
from sys import exc_info
from odoo import models, fields, api, http
from collections.abc import Iterable
from odoo.http import request
import logging
import numpy as np
from datetime import datetime, date
from odoo.exceptions import UserError
import pytz
from library.google import google
import requests
import calendar
import pandas as pd
from dateutil.relativedelta import relativedelta
from google.cloud import bigquery
from validator_collection import validators, checkers
from library.logging import logging

from config import config_broker

# INIT LOG
logger = None
logger = logging.init_log(logger, __name__)

class testing_master_material(models.Model):

    _name = 'testing_master_material'

    active = fields.Boolean(default=True)
    name = fields.Char(string='Material Name')
    code = fields.Char(string='Material Code')
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('cotton', 'Cotton'),
        ('jeans','Jeans')
    ], string='Material Type')
    price = fields.Float(string='Material Price',default = 100)
    supplier = fields.Many2one('testing.supplier', string='Related Supplier')

    @api.onchange('price')
    def onchange_price(self):
        if self.price < 100:
            raise ValidationError('Harga Material tidak boleh < 100 !')

class testing_supplier(models.Model):

    _name = 'testing.supplier'

    active = fields.Boolean(default=True)
    name = fields.Char(string='Name Supplier')