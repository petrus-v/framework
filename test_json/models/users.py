# -*- coding: utf-8 -*-
from openerp import models, fields


class Users(models.Model):

    _name = 'res.users'
    _inherit = 'res.users'

    more_data = fields.Json(string="More data")
