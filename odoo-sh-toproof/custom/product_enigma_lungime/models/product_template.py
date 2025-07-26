from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_per_sqm = fields.Float(string="Preț pe m²", default=100.0,
                                 help="Prețul aplicat pe metrul pătrat.")
