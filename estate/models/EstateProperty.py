from odoo import _, api, fields, models
from odoo.exceptions import UserError

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
    best_price = fields.Float(string="Bester Preis", compute="_compute_best_price", readonly=True)

    # relational fields, these are not stored in the database
    property_offer_ids = fields.One2many("estate.property.offer", "property_id", string="Angebote")
    salesman_commission_ids = fields.Many2one("estate.salesman.commission", 
                                              string="Provisionen",
                                              domain="[('salesman', '=', 'salesman'),('customer', '=', 'customer')]")

    # computed fields
    total_area = fields.Float(string="Gesamtfläche M2", readonly=True, compute="_compute_total_area")
    commission_total = fields.Float(string="Gesamtprovision", compute="_compute_commission_total", inverse="_compute_commission_total_inverse")

    # logic for computed fields
    @api.onchange("living_area","garden_area")
    def _compute_total_area(self):  # private methods start with _
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.depends("commission_for_sale","commission_for_marketing")
    def _compute_commission_total(self):
        for property in self:
            property.commission_total = property.commission_for_sale + property.commission_for_marketing

    def _compute_commission_total_inverse(self):
        for property in self:
            property.commission_for_sale = property.commission_total * 0.6
            property.commission_for_marketing = property.commission_total * 0.4

    def _compute_best_price(self):
        for property in self:
            if property.property_offer_ids:
                property.best_price = max(property.property_offer_ids.mapped("price"))  # TODO put in list
            else:
                property.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_orientation = "N"
            self.garden_area = 1000
        else:
            self.garden_orientation = False
            self.garden_area = 0

    # logic for buttons
    def action_set_to_available(self):
        self.state = "new"
        self.activeForSale = True

    def action_set_to_sold(self):
        for property in self:
            if property.state == "sold":
                raise UserError(_("A sold property cannot be sold again"))
            property.state = "sold"
            property.activeForSale = False
   
    # python constraints
    @api.constrains("garden_area")
    def _check_garden_area(self):
         for property in self:
              if property.garden_area < 0:
                raise UserError(_("The garden area cannot be less than zero M2"))
    
    @api.constrains("name")
    def _check_name(self):
        for property in self:
            if property.name and property.name[0].islower():
                raise UserError(_("The name of the property must start with an uppercase letter"))
            
    # sql constraints
    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The name of the property must be unique"),
        ("price_positive", "CHECK(expected_price >= 0)", "The expected price must be positive")
    ]
