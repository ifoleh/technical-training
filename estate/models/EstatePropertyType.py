from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of Properties (House, Flat, ...)"
    
    name = fields.Char(required = True, string='Name')
    description = fields.Text(string='Beschreibung')
    properties_count = fields.Integer(string="Anzahl der Immobilien", compute="_compute_properties_count")

    def _compute_properties_count(self):
        for property_type in self:
            property_type.properties_count = len(property_type.property_ids)       
