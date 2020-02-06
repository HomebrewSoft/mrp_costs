# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, fields


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    operation_lot_ids = fields.One2many(
        comodel_name='stock.pack.operation.lot',
        inverse_name='lot_id',
    )
    cost_unit = fields.Float(
        compute='_get_cost_unit',
    )

    @api.depends('operation_lot_ids')
    def _get_cost_unit(self):
        for r in self:
            r.cost_unit = r.operation_lot_ids[0].cost_unit
