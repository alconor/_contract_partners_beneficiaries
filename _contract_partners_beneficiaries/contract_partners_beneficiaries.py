# -*- coding: utf-8 -*-
'''
Created on 05/08/2015

@author: alconor
'''
from openerp.osv import fields, osv, orm
from datetime import date, datetime
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

class contract_partners_beneficiaries(osv.osv):
    _name = 'contract.partners.beneficiaries'
    _description = 'Formulario de Beneficiarios de Contratos de Socios'
    _columns = {
              'name' : fields.char('Nombre del Beneficairio',size=256,required=True,help='Nombre y Apellido del Beneficiario'),
              'ruc': fields.char('RUC', size=45),
              'fecha_nacimiento': fields.date('Fecha de Nacimiento'),
              'parentesco': fields.selection([('0','Socio'),
                                              ('1','Hijo'),
                                              ('2','Hermano'),
                                              ('3','Abuelo'),
                                              ('4','Tio'),
                                              ('5','Sobrino'),
                                              ('6','Nieto'),
                                              ('7','Esposo'),
                                              ('8','Padre'),
                                              ('9','Primo'),
                                              ('10','Amigo')],'Parentesco', size=45, )
               }
    #contract_partners_beneficiaries()