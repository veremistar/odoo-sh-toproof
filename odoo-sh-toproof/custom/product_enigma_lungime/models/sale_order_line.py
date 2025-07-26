from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lungime_enigma = fields.Float(string="Lungime (m)", help="Introduceți lungimea în metri pentru Enigma.")
    latime_enigma = fields.Float(string="Lățime (m)", default=1.176, readonly=True)

    @api.onchange('lungime_enigma', 'product_id')
    def _onchange_lungime_enigma(self):
        if self.product_id and self.lungime_enigma and self.product_id.product_tmpl_id.price_per_sqm:
            suprafata = self.lungime_enigma * self.latime_enigma
            pret_m2 = self.product_id.product_tmpl_id.price_per_sqm
            self.price_unit = suprafata * pret_m2
