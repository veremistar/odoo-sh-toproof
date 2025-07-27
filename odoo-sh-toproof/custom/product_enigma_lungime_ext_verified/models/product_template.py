from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    lungime_variabila = fields.Float(string="Lungime (m)", default=1.0)

    @api.depends('lungime_variabila', 'list_price')
    def _compute_surface_price(self):
        for product in self:
            product.price = product.lungime_variabila * 1.176 * product.list_price

    price = fields.Float(string="Preț calculat", compute="_compute_surface_price", store=True)
