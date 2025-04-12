from odoo import models, fields, api
from base64 import b64encode
import pkg_resources

class Py3oTemplate(models.Model):
    _inherit = 'py3o.template'
    #Declare custom field
    py3o_template_fallback = fields.Char("Fallback path")
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            fallback_path =  vals.get("py3o_template_fallback")
            if fallback_path:
                module_name = self._get_module_name()
                flbk_filename = pkg_resources.resource_filename(
                    f'odoo.addons.{module_name}', fallback_path
                )
                with open(flbk_filename, "rb") as f:
                    vals["py3o_template_data"] = b64encode(f.read())
        return super().create(vals_list)
    def _get_module_name(self):
        """Extract the name of the current module automatically."""
        return self._module