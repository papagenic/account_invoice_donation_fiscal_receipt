from odoo import models, fields
from odoo.exceptions import UserError
import pprint

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
            template = self.env.ref('__custom__.template_donation', raise_if_not_found=False)
        else:
            # Use the default invoice email template
            template = self.env.ref('account.email_template_edi_invoice', raise_if_not_found=False)

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
    def print_fiscal_receipt(self):
        self.ensure_one()
        return self.env.ref('__custom__.inv_fiscal_receipt').report_action(self)