import re , datetime
from odoo import models, fields, api, exceptions


class HmsPatient(models.Model):
    _name = "hms.patients"
    _description = "Hospital Patient"
    _rec_name = "First_name"

    First_name = fields.Char(required="True")
    Last_name = fields.Char(required="True")
    birthdate = fields.Date()
    image = fields.Binary()
    history = fields.Html()
    ce_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ])
    age = fields.Integer(compute="calculate_age", store=True)
    email = fields.Char(required="True")
    pcr = fields.Boolean()
    address = fields.Text()
    dept_id = fields.Many2one("hms.departments")
    dept_capacity = fields.Integer(related="dept_id.Capacity")
    doct_ids = fields.Many2many("hms.doctors")
    log_history_ids = fields.One2many("hms.plogs", "patient_log_id")
    state = fields.Selection([
        ('un', 'Undetermined'),
        ('g', 'Good'),
        ('f', 'Fair'),
        ('s', 'Serious')
    ], default="un")

    @api.onchange("age")
    def onchange_age(self):
        if 0 < self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    "title": "Warning",
                    "message": "PCR Field Has Been Checked"
                }
            }
        elif self.age > 30:
            self.pcr = False

    def set_good(self):
        self.state = "g"
        self._set_log("Good")

    def set_fair(self):
        self.state = "f"
        self._set_log("Fair")

    def set_serious(self):
        self.state = "s"
        self._set_log("Serious")

    def _set_log(self, status):
        self.env['hms.plogs'].create({
            "description": f"State Changed to {status}",
            "patient_log_id": self.id
        })

    @api.constrains("email")
    def validate_email(self):
        if self.email:
            if not re.fullmatch(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email):
                raise exceptions.ValidationError("Wrong E-mail")

    @api.depends("birthdate")
    def calculate_age(self):
        today = datetime.date.today()
        for rec in self:
            if rec.birthdate:
                bdate = datetime.datetime.strptime(str(rec.birthdate), '%Y-%m-%d').date()
                diff = today.year - bdate.year
                rec.age = str(diff)

    _sql_constraints = [
        ('Unique_mail', 'UNIQUE(email)', 'E-Mail already exists')
    ]
