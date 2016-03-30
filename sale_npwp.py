from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = "sale.order"
    _description = "Sales NPWP"
    _columns = {
        'npwp': fields.char('NPWP'),
    }