from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_enigma = fields.Boolean(string="Este produs ENIGMA")
