{
    "name": "Account Invoice Fiscal Receipt",
    "version": "16.0.1.0.0",
    "summary": "generates fiscal receipts for customer invoices marked as donations",
    "author": "ChatGPT",
    "category": "Accounting",
    "depends": ["account","report_py3o"],
    "data": [
      "security/ir.model.access.csv",
      "views/annual_fiscal_receipt_wizard_view.xml",
      "views/account_move_view.xml",
      "views/res_config_settings_view.xml",
      "data/py3o_template.xml",
      "data/email_donation_template.xml",
      "data/email_annual_donation_receipt.xml",
    ],
    "installable": True,
    "license": "AGPL-3"
}
