# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class StockPackOperationLot(models.Model):
    _inherit = 'stock.pack.operation.lot'

    cost_unit = fields.Float(
        related='operation_id.cost_unit',
    )
