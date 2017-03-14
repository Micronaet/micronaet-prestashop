#!/usr/bin/python
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
import ConfigParser
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

# -----------------------------------------------------------------------------
#                                Parameters
# -----------------------------------------------------------------------------

config = ConfigParser.ConfigParser()
config.read(['./openerp.cfg'])

# XMLRPC server:
xmlrpc_host = config.get('XMLRPC', 'host') 
xmlrpc_port = eval(config.get('XMLRPC', 'port'))

ps_settings = config.get('Prestashop', 'settings') # Configuration file

# -----------------------------------------------------------------------------
#                         Restrict to a particular path
# -----------------------------------------------------------------------------
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# -----------------------------------------------------------------------------
#                                Create server
# -----------------------------------------------------------------------------
server = SimpleXMLRPCServer(
    (xmlrpc_host, xmlrpc_port), 
    requestHandler=RequestHandler,
    )
server.register_introspection_functions()

# -----------------------------------------------------------------------------
#                            Manifest function exported:
# -----------------------------------------------------------------------------
def execute(model, operation, parameter=None):
    ''' Collect a list of function for common operations            
    '''
    # Setup dict:
    res = {
        'result': False,
        'error': False,
        'note': False
        }
    
    if parameter in None:
        parameter = {}

    print '[INFO] Execute: Model %s - Operation %s - Parameter list: %s' % (
        model, operation, parameter.keys())

    # -------------------------------------------------------------------------
    #                           PRODUCT OPERATIONS:
    # -------------------------------------------------------------------------    
    if model == 'product':
        # ------------------
        # 1. Search product:
        # ------------------
        if operation == 'search':
            pass            
        
        # ------------------
        # 2. Create product:
        # ------------------
        elif operation == 'create':
            pass
        
        # ------------------
        # 3. Update product:
        # ------------------
        elif operation == 'write':
            pass
        
        # ------------------
        # 4. Delete product:
        # ------------------
        elif operation == 'unlink':
            pass
            
        else:
            res['error'] = 'Model %s operation %s not managed!' % (
                model, operation)            
    
    # -------------------------------------------------------------------------
    #                           CATEGORY OPERATIONS:
    # -------------------------------------------------------------------------    
    elif model == 'category':
        pass
    
    else:
        res['error'] = 'Model %s not managed!' % model
        
    # -------------------------------------------------------------------------
    #                           Return result:
    # -------------------------------------------------------------------------
    print '[INFO] End operation'
    return res

# -----------------------------------------------------------------------------
#                  Register Function in XML-RPC server:
# -----------------------------------------------------------------------------
server.register_function(execute, 'execute')

# -----------------------------------------------------------------------------
#                       Run the server's main loop:
# -----------------------------------------------------------------------------
# Log connection:
print 'Start XMLRPC server on %s:%s' % (
    xmlrpc_host,
    xmlrpc_port,
    )
    
server.serve_forever()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

