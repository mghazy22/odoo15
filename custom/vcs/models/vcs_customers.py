from odoo import models, fields


class VcsCustomers(models.Model):
    _name = "vcs.customers"
    _description = "Customers"

    name = fields.Char(required="True",translate="True")
    phone = fields.Integer(required="True")
    certificate_ids = fields.One2many("vcs.certificates","customer_ids")

