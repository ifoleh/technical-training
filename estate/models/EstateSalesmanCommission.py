from odoo import fields, models

class EstateSalesmanCommission(models.Model):
    _name = "estate.salesman.commission"
    _description = "Commission for Salesman and Custoner"
    
    salesman = fields.Many2one("res.users", string="Salesmanager", required=True)
    customer = fields.Many2one("res.partner", string="Customer", required=True)
    commission_amount = fields.Float(string="Commission", required=True)
    property_id = fields.One2many("estate.property", domain=[('salesman_id', '=', salesman),('customer", "=", customer)]')], inverse_name="salesman_commission_ids")
