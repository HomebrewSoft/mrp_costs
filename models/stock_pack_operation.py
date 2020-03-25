# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    cost_unit = fields.Float(
        compute='_compute_cost_unit'
    )
    purchase_id = fields.Many2one(
        related='picking_id.purchase_id',
    )

    @api.depends('product_id', 'purchase_id.order_line')
    def _compute_cost_unit(self):
        for r in self:
            if not r.product_id or not r.picking_id.purchase_id:
                continue
            r.cost_unit = r.picking_id.purchase_id.order_line.filtered(lambda l: l.product_id == r.product_id).price_unit
