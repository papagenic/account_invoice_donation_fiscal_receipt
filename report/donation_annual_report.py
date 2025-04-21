from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class ReportAnnualFiscalReceipt(models.AbstractModel):
    _name = 'report.aidfr.annual_fiscal_receipt'
    _description = 'Annual Fiscal Receipt Py3o Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        year = self.env.context.get('year', 'N/A')

        # Use partner from invoice
        partner = docs.partner_id

        donations = self.env['account.move'].search([
            ('partner_id', '=', partner.id),
            ('move_type', '=', 'out_invoice'),
            ('is_donation', '=', True),
            ('invoice_date', '>=', f'{year}-01-01'),
            ('invoice_date', '<=', f'{year}-12-31'),
            ('state', '=', 'posted'),
            ('payment_state', 'in', ['paid', 'partial', 'in_payment']),
        ])
        total_donation = sum(donations.mapped("amount_total"))-sum(donations.mapped("amount_residual"))
        _logger.info(f">>> Injecting year {year} and donations count {len(donations)} for partner {partner.name}")
        _logger.info(">>> Donation invoices: %s", donations.mapped("name"))
        _logger.info(">>> amount_total: %s", donations.mapped("amount_total"))
        _logger.info(">>> Payment states: %s", donations.mapped("payment_state"))
        return {
            'doc_ids': docs.ids,
            'doc_model': 'account.move',
            'docs': docs,
            'year': year,
            'partner': partner,
            'donations': donations,
            'total_donation': total_donation,
        }
        
