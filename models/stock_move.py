# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'

    cost_unit = fields.Float(
        compute='_compute_cost_unit',
    )

    @api.depends('product_id', 'move_lot_ids', 'raw_material_production_id.weight_total')
    def _compute_cost_unit(self):
        for r in self:
            if r.move_lot_ids and (r.has_tracking != 'none' or r.sudo().move_lot_ids.mapped('lot_id')):
                r.cost_unit = r.move_lot_ids[0].cost_unit * r.raw_material_production_id.weight_total
            else:
                r.cost_unit = r.product_id.standard_price
