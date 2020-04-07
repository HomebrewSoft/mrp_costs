# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class MRPSalesListDelivery(models.TransientModel):
    _inherit = 'res.company'
    _name = 'mrp.list_delivery'

    rent = fields.Float(   
    )