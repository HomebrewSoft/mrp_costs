# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, fields


class MRPBOM(models.Model):
    _inherit = 'mrp.bom'

    waste = fields.Float(
        string='Waste (%)',
    )
    default_code = fields.Char(
        related='product_tmpl_id.default_code',
    )
    uom_id = fields.Many2one(
        related='product_tmpl_id.uom_id',
    )
    weight = fields.Float(
        related='product_tmpl_id.weight',
    )
    weight_total = fields.Float(
        related='product_tmpl_id.weight_total',
    )
    meters = fields.Float(
        related='product_tmpl_id.meters',
    )
