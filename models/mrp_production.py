# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, fields


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    weight_net = fields.Float(
    )
    waste = fields.Float(
        string='Waste (%)',
    )
    weight_total = fields.Float(
        compute='_compute_weight_total',
    )
    meters = fields.Float(
    )
    man_hour = fields.Float(
    )
    rent = fields.Float(
    )
    transport = fields.Float(
    )
    cost = fields.Float(
        compute='_compute_cost',
    )
    sale_percentage = fields.Float(
        string='Sale (%)',
    )
    cost_total = fields.Float(
        compute='_compute_cost_total',
    )

    @api.depends('weight_net', 'waste')
    def _compute_weight_total(self):
        for r in self:
            r.weight_total = (1 + r.waste / 100) * r.weight_net

    @api.depends('move_raw_ids', 'man_hour', 'rent', 'transport')
    def _compute_cost(self):
        for r in self:
            raw_materials = sum(r.move_raw_ids.mapped('cost_unit'))
            r.cost = sum([raw_materials, r.man_hour, r.rent, r.transport])

    @api.depends('cost', 'sale_percentage')
    def _compute_cost_total(self):
        for r in self:
            r.cost_total = (1 + r.sale_percentage / 100) * r.cost
