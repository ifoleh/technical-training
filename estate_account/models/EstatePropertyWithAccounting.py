from odoo import _, models, fields
from odoo.exceptions import UserError

class EstatePropertyWithAccounting(models.Model):
    _inherit = "estate.property"

    onlyVisibleWithAccounting = fields.Boolean(string="Only visible with accounting", default=False)

    def action_create_invoice(self):
        pass

    def action_create_expense(self):
        pass

    def action_create_payment(self):
        pass

    def action_set_to_sold(self):
        print("I am in the inherited method")
        return super().action_set_to_sold()
