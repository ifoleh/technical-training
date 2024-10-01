{
    "name": "Estate",  # The name that will appear in the App list
    "version": "17.0.10.1.49",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tags_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_salesman_commission_views.xml",
        "views/estate_property_menu.xml",
        "views/res_users_form_with_estate.xml"
    ],
    "installable": True,
    'license': 'LGPL-3',
}
