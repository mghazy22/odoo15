from odoo import models, fields, api, _, exceptions
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
    allow_print = fields.Boolean(default='False')
    click = fields.Boolean(default='False')

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

    def print_rpt(self):
        if self.click == False:
            self.click ='True'
            return self.env.ref('vcs.vcs_certificate_card').report_action(self, data={}, config=False)
        elif self.allow_print:
            return self.env.ref('vcs.vcs_certificate_card').report_action(self, data={}, config=False)
        elif self.allow_print == False & self.click ==True:
            raise exceptions.ValidationError("you printed once")


    def allow_reprint(self):
        self.allow_print = 'True'

