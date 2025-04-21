from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    donation_fiscal_year = fields.Char(
        string="Fiscal Year for Annual Donation Reports",
        config_parameter='account_invoice_donation_fiscal_receipt.fiscal_year'
    )