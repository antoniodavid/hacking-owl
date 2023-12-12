from odoo import fields, models


class IrFrontend(models.Model):
    _name = 'ir.frontend'

    name = fields.Char()
