# models/annual_fiscal_receipt_wizard.py
from odoo import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class AnnualFiscalReceiptWizard(models.TransientModel):
    _name = 'annual.fiscal.receipt.wizard'
    _description = 'Annual Fiscal Receipt Wizard'

    year = fields.Selection(
        [(str(y), str(y)) for y in range(datetime.now().year, datetime.now().year - 10, -1)],
        string="Year", required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, readonly=True)

    @api.model
    def default_get(self, fields):
        _logger.info(">>> default_get context: %s", self.env.context)
        res = super().default_get(fields)
        partner_id = self.env.context.get('default_partner_id')
        _logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>will print partner_id")
        _logger.info(">>> default partner_id from context: %s", partner_id)
        if partner_id:
            res['partner_id'] = partner_id
        return res
    def generate_report(self):
        return self.env.ref('account_invoice_donation_fiscal_receipt.action_report_annual_fiscal_receipt').report_action(self)