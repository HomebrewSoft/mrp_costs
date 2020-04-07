# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class MRPConfigSettings(models.TransientModel):
    _inherit = 'mrp.config.settings'

    cost_rent = fields.Float(
        related='company_id.cost_rent',
    )
    transport_cost = fields.Float(
        related='company_id.transport_cost',
    )
    
