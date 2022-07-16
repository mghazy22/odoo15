from odoo import models, fields


class VcsBrand(models.Model):
    _name = "vcs.brand"
    _description = "Car Brands"

    name = fields.Char(required="True",translate="True")
    cert_ids = fields.One2many("vcs.certificates","brand_ids")
