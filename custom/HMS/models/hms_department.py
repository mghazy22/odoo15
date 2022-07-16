from odoo import models , fields

class HasDepartments (models.Model):
    _name = "hms.departments"
    _description = "HMS Department"
    _rec_name = "Department_name"

    Department_name = fields.Char(required="True")
    Capacity = fields.Integer()
    Is_opened = fields.Boolean()
    patient_ids = fields.One2many("hms.patients", "dept_id")
   # doctor_ids = fields.Many2many("hms.doctors")






