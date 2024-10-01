from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of Properties (House, Flat, ...)"
    
    name = fields.Char(required = True, string='Name')
    description = fields.Text(string='Beschreibung')
    properties_count = fields.Integer(string="Anzahl der Immobilien", compute="_compute_properties_count")
    property_ids = fields.One2many("estate.property", "type", string="Immobilien")

    def _compute_properties_count(self):
        for property_type in self:
            property_type.properties_count = len(property_type.property_ids)       

    def action_show_offers(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Estate Properties Show Action",
            "res_model": "estate.property",
            "view_mode": "list,form"
        }

    # <record id="action_show_offers" model="ir.actions.act_window">
    #     <field name="name">Estate Properties Show Action</field>
    #     <field name="res_model">estate.property</field>
    #     <field name="view_mode">list,form</field>
    # </record>

