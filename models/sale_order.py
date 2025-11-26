# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_default_observations(self):
        return False

    observations = fields.Text(
        string="Observaciones",
        default=lambda self: self._get_default_observations()
    )

    