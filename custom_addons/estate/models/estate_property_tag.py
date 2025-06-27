from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate_property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color Index")
    property_ids = fields.Many2many("estate_property", string="Properties")
    
    #def name_get(self):
    #    result = []
    #   for record in self:
    #      result.append((record.id, f"{record.name} ({len(record.property_ids)})"))
    # return result