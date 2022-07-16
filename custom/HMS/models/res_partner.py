from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patientpartner (models.Model):

    _inherit = 'res.partner'

    related_patient_id = fields.Many2one("hms.patients")

    @api.constrains("related_patient_id")
    def _related_patient_email(self):
        if self.related_patient_id.email and self.related_patient_id.email != self.email:
            raise ValidationError("Patient has a different e-mail")

    def unlink(self):
        if self.related_patient_id:
            raise ValidationError("Patient has been linked to customer")
        return super().unlink()

