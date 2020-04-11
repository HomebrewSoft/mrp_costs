# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    waste = fields.Float(
        related='bom_id.waste',
    )
    man_hour = fields.Float(
        related='routing_id.man_hour',
    )
    rent = fields.Float(
        compute='_compute_rent',
    )
    transport = fields.Float(
    )
    cost = fields.Float(
        compute='_compute_cost',
        string='Raw material cost',
    )
    sale_percentage = fields.Float(
        string='Sale (%)',
        related='product_id.sale_percentage',
    )
    sale_cost = fields.Float(
        compute='_get_sale_cost'
    )
    cost_total = fields.Float(  # TODO set to product?
        compute='_compute_cost_total',
    )
    default_code = fields.Char(
        related='product_id.default_code',
    )
    uom_id = fields.Many2one(
        related='product_id.uom_id',
    )
    weight = fields.Float(
        related='product_id.weight',
    )
    weight_total = fields.Float(
        related='product_id.weight_total',
    )
    meters = fields.Float(
        related='product_id.meters',
    )
    produced = fields.Float(
        related='bom_id.produced',
    )

    @api.depends('move_raw_ids', 'man_hour', 'rent', 'transport')
    def _compute_cost(self):
        for record in self:
            raw_materials = sum(record.move_raw_ids.mapped('cost_unit'))
            record.cost = sum([raw_materials, record.man_hour, record.rent, record.transport])

    @api.depends('sale_percentage', 'cost')
    def _get_sale_cost(self):
        for record in self:
            record.sale_cost = record.sale_percentage / 100 * record.cost

    @api.depends('cost', 'sale_percentage')
    def _compute_cost_total(self):
        for record in self:
            record.cost_total = record.cost + record.sale_cost

    @api.depends('routing_id.rent_kilo', 'weight', 'move_finished_ids.quantity_done')
    def _compute_rent(self):
        for record in self:
            if record.routing_id:
                record.rent = record.routing_id.rent_kilo * record.weight * sum(map(lambda move: move.quantity_done, record.move_finished_ids))
