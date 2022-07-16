from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomerPartner (models.Model):

    _inherit = 'res.partner'

    related_customer_id = fields.Many2one("vcs.customers")



