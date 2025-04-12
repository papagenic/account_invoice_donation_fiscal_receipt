# account_invoice_donation_fiscal_receipt
Odoo donation management with invoicing; generate fiscal receipt
# goal

This is an odoo module which can be used to manage donations for charity associations or else.

There is already an OCA donation module, but I find this module is focused on the description of the donations and generation of fiscal receipts. It assumes a donation is entered when it is paid

For the usage, a donation starts with a donation promise that may materialize into a payment or not. So I needed something to be able to track payments on a day to day bases... something pretty much like the accounting module is doing for customer invoices. 

So this module is adding an is-donation checkbox to a customer invoice. When the checkbox is set, the send and print button will not generate a customer invoice but rather a fiscal receipt

# Install
during install the module will create:

A py3o report template based upon the template Inv Donation Certificate FR.odt  file located in the report folder. This file need to be changed acoording to your needs

A py3o report based on the previous template that will be used to generate the fiscal receipt. This should not need customization

A template for the thanks email used as a wrapper when sending fiscal receipts.This is located in data/email_donation_template and can be customized according to your needs
