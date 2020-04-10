# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class MRPCostsWizard(models.TransientModel):
    _inherit = 'res.company'
    _name = 'mrp.costs_wizard'

    transport_cost = fields.Float(
        required=True,
        default=lambda self: self.env.user.company_id['transport_cost'],
    )
    rent = fields.Float(
        required=True,
        default=lambda self: self.env.user.company_id['cost_rent'],
    )    
    waste = fields.Float(
        required=True,
        default=lambda self: self.env.user.company_id['waste'],
    )    
    date_start = fields.Datetime(
        # default=fields.Date.context_today,
        required=True,
    )
    date_end = fields.Datetime(
        # default=fields.Date.context_today,
        required=True,
    )

    @api.multi
    def calculate(self):
        routing_ids = self.env['mrp.routing'].search([])
        if not routing_ids:
            return {}

        rent_routing = self.rent / len(routing_ids)
        for routing_id in routing_ids:
            move_ids = self.env['stock.move'].search([
                ('state', '=', 'done'),
                ('date', '>=', self.date_start),
                ('date', '<', self.date_end),
                ('routing_id', '=', routing_id.id),
            ])
            kilos = sum(map(lambda move_id: move_id.product_uom_qty * move_id.product_id.weight, move_ids))
            routing_id.rent_kilo = (rent_routing / kilos) if kilos else 0
        return {}
