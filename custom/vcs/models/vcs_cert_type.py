from odoo import models, fields


class VcsCertificatesTypes(models.Model):
    _name = "vcs.cert_type"
    _description = "Certificate Types"

    name = fields.Char(required="True",translate="True")
    cert_ids = fields.One2many("vcs.certificates","certificate_Type_ids")