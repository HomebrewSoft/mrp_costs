# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, fields


class StockPackOperationLot(models.Model):
    _inherit = 'stock.pack.operation.lot'

    cost_unit = fields.Float(
        related='operation_id.cost_unit',
    )
