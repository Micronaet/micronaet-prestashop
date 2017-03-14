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
    def search(default_code):
        ''' Search product
        '''
        import pdb; pdb.set_trace()
        if not self.connection:
            return False
        
        self.connection.execute('''
            SELECT id_product
            FROM ps_product
            WHERE reference = '%s';
            ''' % default_code)

        return [item[0] for item in self.connection]

    # -------------------------------------------------------------------------
    # Constructor:
    # -------------------------------------------------------------------------
    def __init__(self, database, user, password, server='localhost', port=3306, 
            charset='utf8'):
        ''' Init procedure        
        '''
        # Save parameters:
        self.database = database
        self.user = user
        self.password = password
        self.server = server or 'localhost'
        self.port = port or 3306
        self.charset = charset
        self.status = 'connected'
        self.connected = True
        
        try:            
            error = 'Error no MySQLdb installed'
            import MySQLdb, MySQLdb.cursors

            error = 'Error connecting to database: %s:%s > %s [%s]' % (
                self.server,
                self.port,
                self.database,
                self.user,
                )
                
            self.connection = MySQLdb.connect(
                host=self.server,
                user=self.user,
                passwd=self.password,
                db=self.database,
                cursorclass=MySQLdb.cursors.DictCursor,
                charset=self.charset,
                )                        
        except:
            self.status = error
            self.connected = False
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
    if not mysql_ps.connected:
        print 'Not connected: %s' % mysql_ps.status
        sys.exit()
    else:    
        return 'Connected'

if __name__ == '__main__':
    main()
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
