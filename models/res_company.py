# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    cost_rent = fields.Float(
    )
