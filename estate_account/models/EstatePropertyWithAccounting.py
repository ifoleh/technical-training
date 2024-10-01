from odoo import _, models, fields, Command
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

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
        _logger.info("I am in the inherited method")
        self.createCustomerInvoice()
        return super().action_set_to_sold()

    def createCustomerInvoice(self):
        vals_list = []
        # journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()

        for property in self:
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': self.partner_invoice_id.id,
                # 'journal_id': journal.id,  # company comes from the journal
                'journal_id': 1,
                'invoice_line_ids': [
                    Command.create({
                        "name": property.name,
                        "quantity": 1,
                        "price_unit": property.best_price * 0.06}),
                    Command.create({
                        "name": "Administrationsgebühr",
                        "quantity": 1,
                        "price_unit": 200}),
                ],
            }
            vals_list.append(invoice_vals)
        self.env['account.move'].create(vals_list)
        


