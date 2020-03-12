# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, fields


class MRPBOM(models.Model):
    _inherit = 'mrp.bom'

    waste = fields.Float(
        string='Waste (%)',
    )
    produced = fields.Float(
        compute='_get_produced',
    )
    production_ids = fields.One2many(
        comodel_name='mrp.production',
        inverse_name='bom_id',
    )
    
    def _get_produced(self):
        for record in self:
            if record.routing_id:
                record.produced = record.routing_id._get_produced_by_product_ids(record.product_tmpl_id.product_variant_ids.ids)
