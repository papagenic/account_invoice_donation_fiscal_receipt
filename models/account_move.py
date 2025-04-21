from odoo import models, fields,api
from odoo.exceptions import UserError
import pprint
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_donation = fields.Boolean(
        string="Is Donation?",
        help="Check this box if this invoice is a donation. Used to generate fiscal receipts.",
        tracking=True,
    )
    def action_invoice_sent(self):
        self.ensure_one()

        if self.is_donation:
            # Set the donation-specific email template
            template = self.env.ref('account_invoice_donation_fiscal_receipt.email_template_send_fiscal_receipt', raise_if_not_found=False)        
        else:
            # Use the default invoice email template
            template = self.env.ref('account.email_template_edi_invoice', raise_if_not_found=False)
        _logger.info(f"payment state for invoice is  {self.payment_state}")
        _logger.info(">>>>>>>>>>>>>>>>>>>> Template used for send&print: %s", template)
        # Return the email composition wizard action
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': {
                'default_model': 'account.move',
                'default_res_id': self.id,
                'default_use_template': bool(template),
                'default_template_id': template.id if template else False,
                'default_composition_mode': 'comment',
                'mark_invoice_as_sent': True,
            },
        }
    def action_send_annual_receipt(self):
        self.ensure_one()
        #the fiscal year to use is defined in the settings of the customer bills
        year = self.env['ir.config_parameter'].sudo().get_param('account_invoice_donation_fiscal_receipt.donation_fiscal_year') or str(fields.Date.today().year)        # Use the send annual receipt  email template
        template = self.env.ref('account_invoice_donation_fiscal_receipt.email_annual_donation_receipt', raise_if_not_found=False)
        
 
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': {
                'default_model': 'account.move',
                'default_res_id': self.id,
                'default_use_template': True,
                'default_template_id': template.id if template else False,
                'default_composition_mode': 'comment',
                'mark_invoice_as_sent': True,
                'year': year,
                'partner_id': self.partner_id.id,
            },
        }
    def action_open_annual_fiscal_receipt_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'name': "Annual Fiscal Receipt",
            'res_model': 'annual.fiscal.receipt.wizard',
            'target': 'new',
            'view_id': self.env.ref('account_invoice_donation_fiscal_receipt.view_annual_fiscal_receipt_wizard_form').id,            
            'context': {
                'default_partner_id': self.partner_id.id,
            }
        }
    def action_send_annual_fiscal_report(self):
        # Placeholder logic
        for move in self:
            if move.is_donation:
                _logger.info(f"Sending annual receipt for partner {move.partner_id.name}")
        return True
    def print_fiscal_receipt(self):
        self.ensure_one()
        return self.env.ref('__custom__.inv_fiscal_receipt').report_action(self)