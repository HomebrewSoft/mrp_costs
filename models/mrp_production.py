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
    cost_coil = fields.Float(
        compute='_get_raw_materials_cost',
    )
    cost_bag = fields.Float(
        compute='_get_raw_materials_cost',
    )
    cost_tube = fields.Float(
        compute='_get_raw_materials_cost',
    )
    cost_other = fields.Float(
        compute='_get_raw_materials_cost',
    )

    @api.depends('move_raw_ids')
    def _get_raw_materials_cost(self):
        for record in self:
            coil_ids = record.move_raw_ids.filtered(lambda move: move.product_id.categ_id.id == self.env.ref('mrp_costs.product_category_coil').id)
            bag_ids = record.move_raw_ids.filtered(lambda move: move.product_id.categ_id.id == self.env.ref('mrp_costs.product_category_bag').id)
            tube_ids = record.move_raw_ids.filtered(lambda move: move.product_id.categ_id.id == self.env.ref('mrp_costs.product_category_tube').id)
            other_ids = record.move_raw_ids - (coil_ids | bag_ids | tube_ids)
            record.cost_coil = sum(coil_ids.mapped('cost_unit'))
            record.cost_bag = sum(bag_ids.mapped('cost_unit'))
            record.cost_tube = sum(tube_ids.mapped('cost_unit'))
            record.cost_other = sum(other_ids.mapped('cost_unit'))

    @api.depends('cost_coil', 'cost_bag', 'cost_tube', 'cost_other', 'man_hour', 'rent', 'transport')
    def _compute_cost(self):
        for record in self:
            record.cost = (
                record.cost_coil
                + record.cost_bag
                + record.cost_tube
                + record.cost_other
                + record.man_hour
                + record.rent
                + record.transport
            )

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
                record.rent = record.routing_id.rent_kilo
