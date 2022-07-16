from odoo import models, fields, api,_
import re, datetime as dt


class VcsCertificates(models.Model):
    _name = "vcs.certificates"
    _description = "Validation Certificates"

    serial_no = fields.Char(string="Serial No", readonly=True, required=True, copy=False, default='New')
    Vehicle_Type = fields.Selection([
        ('ca', 'Car'),
        ('b', 'Bus'),
        ('mn', 'Minibus'),
        ('mc', 'Microbus')
    ], default="ca", translate="True")
    certificate_Type_ids = fields.Many2one("vcs.cert_type")
    customer_ids = fields.Many2one("vcs.customers")
    traffic_dept_ids = fields.Many2one("vcs.traffic_dept")
    price = fields.Integer()
    motor_number = fields.Integer()
    chassis_number = fields.Char()
    car_model = fields.Selection(selection='getyear')
    brand_ids = fields.Many2one("vcs.brand")

    @api.model
    def create(self, vals):
        if vals.get('serial_no', 'New') == 'New':
            vals['serial_no'] = self.env['ir.sequence'].next_by_code('vcs.certificates') or 'New'
        res = super(VcsCertificates, self).create(vals)
        return res

    @api.model
    def getyear(self):
        current_year = dt.date.today().year
        current_year += 1
        years = []
        for x in range(1, 21):
            current_year -= 1
            years.append(str(current_year))
        data = list(zip(years, years))
        return data

