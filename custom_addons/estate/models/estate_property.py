from odoo import fields,models

class EstateProperty(models.Model):
    _name="estate_property"
    _description ="estate property"

    name = fields.Char()
    description=fields.Text()
    postcode = fields.Char()
    date_availabilty=fields.Date()
    expected_price= fields.Float()
    selling_price= fields.Float()
    bedrooms= fields.Integer()
    living_area=fields.Integer()
    facades= fields.Integer()
    garage= fields.Boolean()
    garden = fields.Boolean()
    garden_area=fields.Integer()

    garden_orientation= fields.Selection(string="Garden Orientation",selection=[('North','North'),('South','South'),('East','East'),('West','West')])