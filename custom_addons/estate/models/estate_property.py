from odoo import fields,models,api

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
    state= fields.Selection(string="State",
                            selection=[('New','New'),('Offer Received','Offer Received'),('Offer Accepted','Offer Accepted'),('Sold','Sold'),('Canceled','Canceled')])
    property_type_id  = fields.Many2one("estate_property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner",string="Buyer")
    salesperson_id = fields.Many2one("res.users",string="Salesperson" , default = lambda self: self.env.user)
    tags_ids = fields.Many2many("estate_property.tag",string="Tags") 
    offer_ids = fields.One2many("estate_property.offer","property_id",string="Offers")
    
    

    garden_orientation= fields.Selection(string="Garden Orientation",selection=[('North','North'),('South','South'),('East','East'),('West','West')])
    total_area = fields.Integer(compute="_compute_total_area", string="Total Area") 
    highest_offer = fields.Integer(compute="_compute_highest_offer", string="Best Offer") 
    
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area 
    
    @api.depends('offer_ids.price')
    def _compute_highest_offer(self):
        for record in self:
            if record.offer_ids:
                record.highest_offer = max(record.offer_ids.mapped('price'))
            else:
                record.highest_offer = 0.0
                
    @api.onchange('garden')
    def onchange_garden(self):
        if self.garden: 
            self.garden_area = 10
            self.garden_orientation = 'North'
        else:
            self.garden_area = 0
            self.garden_orientation = ''
            
    def action_set_cancel(self):
        for record in self:
            record.state="Canceled"
        return True