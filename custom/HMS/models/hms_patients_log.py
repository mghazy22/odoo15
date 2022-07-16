import logging

from odoo import models, fields

class PatientLogs (models.Model):
    _name = "hms.plogs"
    _description = "HMS Patient Logs"

    description = fields.Text()
    patient_log_id = fields.Many2one("hms.patients")


