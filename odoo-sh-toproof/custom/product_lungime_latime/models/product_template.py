from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('product_variant_ids')
    def _compute_list_price_by_length_and_width(self):
        for template in self:
            for variant in template.product_variant_ids:
                length_attr = variant.product_template_attribute_value_ids.filtered(
                    lambda x: x.attribute_id.name == 'Lungime'
                )
                if length_attr and length_attr.custom_value:
                    try:
                        length = float(length_attr.custom_value)
                        width = 1.176  # latime fixa
                        sqm = length * width
                        price_per_sqm = 100  # lei per m2
                        variant.list_price = sqm * price_per_sqm
                    except ValueError:
                        variant.list_price = 0.0

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.depends('product_template_attribute_value_ids')
    def _compute_list_price(self):
        super()._compute_list_price()
        for product in self:
            length_attr = product.product_template_attribute_value_ids.filtered(
                lambda x: x.attribute_id.name == 'Lungime'
            )
            if length_attr and length_attr.custom_value:
                try:
                    length = float(length_attr.custom_value)
                    width = 1.176
                    sqm = length * width
                    price_per_sqm = 100
                    product.list_price = sqm * price_per_sqm
                except ValueError:
                    product.list_price = 0.0
