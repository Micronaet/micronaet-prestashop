# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import os
import sys

# -----------------------------------------------------------------------------
#                                MYSQL CLASS
# -----------------------------------------------------------------------------
class mysql_connector():
    ''' MySQL connector
    '''
    # -------------------------------------------------------------------------
    #                             Exported function:
    # -------------------------------------------------------------------------
    def create(self, record, lang_record=False):
        ''' Update record
            record: data of ps_product
            lang_record: dict with ID lang: dict of valued
        '''
        if not self._connection:
            return False
        if not lang_record:    
            {}

        # ---------------------------------------------------------------------
        # Fields validation:
        # ---------------------------------------------------------------------
        field_mandatory = ['reference', 'price']

        # Use quote:
        field_quote = [            
            # String:
            'ean13', 'upc', 'redirect_type', 'visibility',
            'condition', 'reference', 'supplier_reference',
            'unity', 'location',

            # Date:
            'available_date', 'date_add', 'date_upd',
            ]

        # ---------------------------------------------------------------------
        # Update numeric ps_product
        # ---------------------------------------------------------------------
        record_default = {
            #'id_product':
            'id_supplier': 0,
            'id_manufacturer': 0,
            'id_category_default': 0, # TODO
            'id_shop_default': 1,
            'id_tax_rules_group': 1,
            'on_sale': 0,
            'online_only': 0,
            'ean13': '', # TODO
            'upc': '',
            'ecotax': 0.0,
            'quantity': 0,
            'minimal_quantity': 1,
            'price': 0.0, # TODO
            'wholesale_price': 0.0,
            'unity': '',
            'unit_price_ratio': 0.0,
            'additional_shipping_cost': 0.0,
            'reference': '', # TODO
            'supplier_reference': '', # TODO
            'location': '',
            'width': 0.0, # TODO
            'height': 0.0, # TODO
            'depth': 0.0, # TODO
            'weight': 0.0, # TODO
            'out_of_stock': 2, # TODO
            'quantity_discount': 0,
            'customizable': 0,
            'uploadable_files': 0,
            'text_fields': 0,
            'active': 1, # TODO
            'redirect_type': '404',
            'id_product_redirected': 0,
            'available_for_order': 1, # TODO
            'available_date': '2014-02-21', # TODO
            'condition': 'new',
            'show_price': 1,
            'indexed': 1,
            'visibility': 'both',
            'cache_is_pack': 0,
            'cache_has_attachments': 0,
            'is_virtual': 0,
            'cache_default_attribute': 0, # TODO
            'date_add': '2017-01-01 10:00:00',
            'date_upd': '2017-01-01 10:00:00',
            'advanced_stock_management': 0,
            'pack_stock_type': 3,
            }
        
        record.update(record_default) # Add field passed from ODOO

        fields = values = ''
        for field, value in record.iteritems():
            if fields:
                fields += ', '
            fields += '`%s`' % field

            if values:
                values += ', '
            values += '%s%s%s' % (
                '\'' if field in field_quote else '',
                value,
                '\'' if field in field_quote else '',
                )
            
        cr = self._connection.cursor()
        query = 'INSERT INTO ps_product(%s) VALUES (%s);' % (fields, values)
        cr.execute(query)
        item_id = self._connection.insert_id()
        # Update lang ps_product_lang
        if not lang_record:
            return item_id
                    
        return item_id

    def write(self, **parameter):
        ''' Update record
        '''
        item_id = parameter['item_id']
        record = parameter['record']
        
        # Update numeric ps_product 
        
        # Update lang ps_product_lang
        
        return True        
        
    def search(self, domain):
        ''' Search product
            parameter = [('field', 'operator', 'value')]
        '''
        if not self._connection:
            return False
        cr = self._connection.cursor()
        query = '''
            SELECT id_product
            FROM ps_product
            WHERE %s %s '%s';
            ''' % (
                domain[0],
                domain[1],
                domain[2],                
                )
        if mysql_db._log:
            print query
        cr.execute(query)
        return [item['id_product'] for item in cr.fetchall()]

    # -------------------------------------------------------------------------
    # Constructor:
    # -------------------------------------------------------------------------
    def __init__(self, database, user, password, server='localhost', port=3306, 
            charset='utf8'):
        ''' Init procedure        
        '''
        # Save parameters:
        self._database = database
        self._user = user
        self._password = password
        self._server = server or 'localhost'
        self._port = port or 3306
        self._charset = charset
        self._status = 'connected'
        self._connected = True
        
        self._log = False # no log
        
        try:            
            error = 'Error no MySQLdb installed'
            import MySQLdb, MySQLdb.cursors

            error = 'Error connecting to database: %s:%s > %s [%s]' % (
                self.server,
                self.port,
                self._database,
                self.user,
                )
                
            self._connection = MySQLdb.connect(
                host=self._server,
                user=self._user,
                passwd=self._password,
                db=self._database,
                cursorclass=MySQLdb.cursors.DictCursor,
                charset=self._charset,
                )                        
        except:
            self._status = error
            self._connected = False
        return
    
# -----------------------------------------------------------------------------
#                                 MAIN PROCEDURE    
# -----------------------------------------------------------------------------
def main():
    ''' Main procedure
    '''
    # TODO read condig PHP file
    database = 'database'
    user = 'user'
    password = 'password'
    server = 'localhost'
    port = 3306
    
    mysql_ps = mysql_connector(database, user, password, server, port)
    if not mysql_ps._connected:
        print 'Not connected: %s' % mysql_ps._status
        sys.exit()
    else:    
        return 'Connected'

if __name__ == '__main__':
    main()
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
