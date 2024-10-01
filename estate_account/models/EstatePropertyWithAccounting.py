from odoo import models

class EstatePropertyWithAccounting(models.Model):
    _inherit = "estate.property"

    def action_create_invoice(self):
        pass

    def action_create_expense(self):
        pass

    def action_create_payment(self):
        pass