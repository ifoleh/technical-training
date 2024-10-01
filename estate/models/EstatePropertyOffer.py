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
 
    # logic for buttons
    def action_accept_offer(self):
        for offer in self:
            offer.property_id.state = "offer_accepted"
            offer.accepted = True
            for other_offer in offer.property_id.property_offer_ids:
                if other_offer != offer:
                    other_offer.accepted = False
                    # other_offer.property_id.state = "offer_received"

    def action_refuse_offer(self):
        for offer in self:
            offer.accepted = False
            # offer.property_id.state = "new"