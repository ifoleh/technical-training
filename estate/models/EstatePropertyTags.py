from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property.tags"
    _description = "Tags for properties"
    
    name = fields.Char(required = True, string='Name')
    description = fields.Text(string='Beschreibung', copy=False)
    