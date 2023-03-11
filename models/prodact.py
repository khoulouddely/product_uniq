from odoo import api, fields, models

class ProdactUnique (models.Model): 
    _inherit = 'product.template'



_sql_constraints = [
    ('cne_unique', 'unique(cne)', 'cne already exists!')

    
]