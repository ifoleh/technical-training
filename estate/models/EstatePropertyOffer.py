from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "There are the offers for the properties"
    
    # non computed fields
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    name_of_buyer = fields.Char(string="Name des Käufers", required=True)
    price = fields.Float(string="Angebotener Preis", required=True)
    date = fields.Date(string="Datum", default=fields.Date.today())
    accepted = fields.Boolean(string="Angebot angenommen")
   
    # computed fields
  
    # logic for computed fields
 