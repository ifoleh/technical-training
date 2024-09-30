from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of Properties (House, Flat, ...)"
    
    name = fields.Char(required = True, string='Name')
    description = fields.Text(string='Beschreibung')
