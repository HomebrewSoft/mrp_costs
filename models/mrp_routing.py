# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class MRPRouting(models.Model):
    _inherit = 'mrp.routing'

    rent_kilo = fields.Float(
    )
    man_hour = fields.Float(
    )
    
    def _get_produced_by_product_ids(self, product_ids):
        for record in self:
            workorder_ids = record.operation_ids.mapped('workorder_ids')
            workorder_ids = workorder_ids.filtered(lambda wo: wo.product_id.id in product_ids)
            # workorder_ids = workorder_ids.filtered(lambda wo: wo.date_start >= TODO and wo.date_finished < TODO)  # TODO
            quantities = workorder_ids.mapped('qty_produced')
            return sum(quantities)
