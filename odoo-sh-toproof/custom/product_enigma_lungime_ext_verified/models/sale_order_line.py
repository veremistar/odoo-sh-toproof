from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    lungime_m = fields.Float(string="Lungime (m)")

    @api.onchange("lungime_m", "product_id", "product_uom_qty")
    def _onchange_lungime_m(self):
        if self.product_id and self.lungime_m and self.product_id.list_price:
            self.price_unit = self.lungime_m * 1.176 * self.product_id.list_price * self.product_uom_qty
