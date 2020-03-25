# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    waste = fields.Float(
        string='Waste (%)',
        compute='_get_waste',
    )
    weight_total = fields.Float(
        compute='_compute_weight_total',
    )
    meters = fields.Float(
    )

    @api.depends('waste', 'weight')
    def _compute_weight_total(self):
        for record in self:
            record.weight_total = (1 + record.waste / 100) * record.weight

    @api.depends('bom_ids')
    def _get_waste(self):
        for record in self:
            if record.bom_ids:
                record.waste = record.bom_ids[0].waste  # TODO always the first?
