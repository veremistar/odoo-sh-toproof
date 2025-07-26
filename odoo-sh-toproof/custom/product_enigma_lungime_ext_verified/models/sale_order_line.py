from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lungime_enigma = fields.Float(string="Lungime (m)", help="Introduceți lungimea în metri.")
    latime_enigma = fields.Float(string="Lățime (m)", default=1.176, readonly=True)
    suprafata_enigma = fields.Float(string="Suprafață (m²)", compute="_compute_suprafata", store=True)

    @api.depends('lungime_enigma', 'latime_enigma')
    def _compute_suprafata(self):
        for line in self:
            line.suprafata_enigma = (line.lungime_enigma or 0.0) * (line.latime_enigma or 1.176)

    @api.onchange('lungime_enigma', 'product_id')
    def _onchange_lungime_enigma(self):
        for line in self:
            if (
                line.product_id
                and line.lungime_enigma
                and line.product_id.product_tmpl_id.price_per_sqm
            ):
                line.suprafata_enigma = line.lungime_enigma * line.latime_enigma
                pret_m2 = line.product_id.product_tmpl_id.price_per_sqm
                line.price_unit = line.suprafata_enigma * pret_m2
