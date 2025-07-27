from odoo import models, fields, api

class ProductQuotation(models.Model):
    _name = 'product.quotation'
    _description = 'Product Quotation'

    name = fields.Char(string='Quotation Reference', required=True)
    length = fields.Float(string='Length (m)', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price_per_sqm = fields.Float(string='Price per Square Meter', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.company.currency_id.id)
    total_price = fields.Monetary(string='Total Price', currency_field='currency_id', compute='_compute_total_price', store=True)

    @api.depends('length', 'quantity', 'price_per_sqm')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.length * rec.quantity * 1.178 * rec.price_per_sqm