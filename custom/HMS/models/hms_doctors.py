from odoo import models , fields

class HasDoctors (models.Model):
    _name = "hms.doctors"
    _description = "HMS Doctors"
    _rec_name = "First_name"

    First_name = fields.Char(required="True")
    Last_name = fields.Char(required="True")
    Image = fields.Binary()
    patient_ids = fields.Many2many("hms.patients")
    #dept_ids = fields.Many2many("hms.departments")

