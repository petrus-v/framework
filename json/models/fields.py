# -*- coding: utf-8 -*-
from openerp import fields
from openerp import models
from openerp.osv import fields as columns


class json(columns._column):
    _type = 'json'


class Json(fields.Field):
    type = 'json'


fields.Json = Json
columns.json = json
models.FIELDS_TO_PGTYPES[json] = 'jsonb'
