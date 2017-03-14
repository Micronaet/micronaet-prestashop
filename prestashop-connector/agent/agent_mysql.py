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
from datetime import datetime, timedelta

# -----------------------------------------------------------------------------
#                                MYSQL CLASS
# -----------------------------------------------------------------------------
class mysql_connector():
    ''' MySQL connector
    '''
    
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
        
        res = 'Connected'
        try:            
            import MySQLdb, MySQLdb.cursors
                        
            self.connection = MySQLdb.connect(
                host=self.server,
                user=self.user,
                passwd=self.password,
                db=self.database,
                cursorclass=MySQLdb.cursors.DictCursor,
                charset=self.charset,
                )        
        except:
            res = 'Error no module MySQLdb installed!'
        return res
    
# -----------------------------------------------------------------------------
#                                 MAIN PROCEDURE    
# -----------------------------------------------------------------------------
def main():
    ''' Main procedure
    '''
    # TODO read condig PHP file
    database = 'database'
    user = 'usar'
    password = 'password'
    server = 'localhost'
    port = 3306
    
    mysql_ps = mysql_connector(database, user, password, server, port)
    return

if __name__ == '__main__':
    main()
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
