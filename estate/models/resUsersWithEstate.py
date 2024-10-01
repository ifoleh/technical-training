from odoo import fields, models

class ResUsersWithEstate(models.Model):
    _inherit = "res.users"
    
    estate_property_ids = fields.One2many("estate.property", "salesman", string="Properties")