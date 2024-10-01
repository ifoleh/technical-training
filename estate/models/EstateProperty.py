from odoo import api, fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a test model for Odoo Masterclass Dev Intro"
    
    # non computed fields
    name = fields.Char(required = True, string='Name')
    description = fields.Text(string='Beschreibung', copy=False)  # copy: ob beim Kopieren dieser Wert kopiert wird
    postcode = fields.Char(string="PLZ")
    date_availability = fields.Date(string='Verfügbar ab', default=fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(string='Erwarteter Verkaufspreis')
    bedrooms = fields.Integer(string="Anzahl Zimmer")
    garden = fields.Boolean(string="Garten vorhanden")
    garden_orientation = fields.Selection([("N","Nord"),("O","Ost"),("S","Süd"),("W","West")], string="Garten Ausrichtung")
    activeForSale = fields.Boolean(default=False, string="Aktiviert für Verkauf")
    state = fields.Selection(selection=[("new","Neu"),("offer_received","Angebot erhalten"),("offer_accepted","Angebot angenommen"),("sold","Verkauft"),("cancelled","Storniert")], default="new", copy=False, required=True)
    type = fields.Many2one("estate.property.type", string="Typ")
    salesman = fields.Many2one("res.users", string="Salesmanager", default=lambda self: self.env.user)
    customer = fields.Many2one("res.partner", string="Customer")
    tags = fields.Many2many("estate.property.tags", string="Stichwörter")
    living_area = fields.Float(string="Wohnfläche M2")
    garden_area = fields.Float(string="Gartenfläche M2")
    commission_for_sale = fields.Float(string="Provision für Verkauf")
    commission_for_marketing = fields.Float(string="Provision für Marketing")

    # computed fields
    total_area = fields.Float(string="Gesamtfläche M2", readonly=True, compute="_onchange_total_area")
    commission_total = fields.Float(string="Gesamtprovision", compute="_onchange_commission_total", inverse="_onchange_commission_total_inverse")

    # logic for computed fields
    @api.onchange("living_area","garden_area")
    def _onchange_total_area(self):  # private methods start with _
        self.total_area = self.living_area + self.garden_area

    @api.depends("commission_for_sale","commission_for_marketing")
    def _onchange_commission_total(self):
        self.commission_total = self.commission_for_sale + self.commission_for_marketing

    @api.depends("commission_total")
    def _onchange_commission_total_inverse(self):
        self.commission_for_sale = self.commission_total * 0.6
        self.commission_for_marketing = self.commission_total * 0.4