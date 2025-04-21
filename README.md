# account_invoice_donation_fiscal_receipt
Odoo donation management with invoicing; generate fiscal receipt
# goal

This is an odoo module which can be used to manage donations for charity associations or else.

There is already an OCA donation module, but  this module is focused on the description of the donations and generation of fiscal receipts. It assumes a donation is entered when it is paid, and hence does allow to track payment status, partial payments and so on.

For the usage considered, a donation starts with a donation promise that may materialize into a payment or not. So we  needed something to be able to track payments on a day to day basis... something pretty much like the accounting module is doing for customer invoices. 

So this module is adding an is-donation checkbox to a customer invoice. When the checkbox is set for an invoice, this invoice is considered as a donation. Then:
- The send and print button will not generate a customer invoice but rather a fiscal receipt
- Another button "annual fiscal report" will appear next to the "send & print" button. It will be used to generate an annual fiscal report for the partner summarizing all paid donations duing the selected fiscal year. the fiscal year  is defined in the settings of the accounting application.

# Install
during install the module will create:

- A py3o report template based upon the template "Inv Donation Certificate FR.odt"  file located in the report folder. This file can  be customized if needed
- A py3o report template based upon the template "annual_fiscal_receipt_template.odt" also located in the reports folder. This will be used to generate the annual fiscal report
- two  py3o reports based on the previous templates that will be used to generate the fiscal receipt for the selected donation and the annual fiscal report. This should not need customization
- two  templates for the thanks email used as a wrapper when sending fiscal receipts.and annual fiscal reports. They are  located in data/email_donation_template and can be customized if needed
