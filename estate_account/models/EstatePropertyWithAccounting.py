from odoo import models, fields

class EstatePropertyWithAccounting(models.Model):
    _inherit = "estate.property"

    onlyVisibleWithAccounting = fields.Boolean(string="Only visible with accounting", default=False)

    def action_create_invoice(self):
        pass

    def action_create_expense(self):
        pass

    def action_create_payment(self):
        pass