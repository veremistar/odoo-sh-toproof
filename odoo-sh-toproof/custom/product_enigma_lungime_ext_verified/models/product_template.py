from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_lungime_metri = fields.Float(string="Lungime (m)")
    x_latime_fixa = fields.Float(string="Latime fixa (m)", default=1.176, readonly=True)
    x_pret_pe_m2 = fields.Float(string="Pret pe m²")

    @api.onchange("x_lungime_metri", "x_pret_pe_m2")
    def _onchange_lungime_automat(self):
        for rec in self:
            if rec.x_lungime_metri and rec.x_pret_pe_m2:
                rec.list_price = rec.x_lungime_metri * rec.x_latime_fixa * rec.x_pret_pe_m2
