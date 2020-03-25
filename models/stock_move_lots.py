# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class StockMoveLots(models.Model):
    _inherit = 'stock.move.lots'

    cost_unit = fields.Float(
        related='lot_id.cost_unit'
    )
