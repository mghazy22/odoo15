from odoo import models, fields


class VcsTrafficDept(models.Model):
    _name = "vcs.traffic_dept"
    _description = "Traffic Department"

    name = fields.Char(required="True",translate="True")
    cert_ids = fields.One2many("vcs.certificates","traffic_dept_ids")
