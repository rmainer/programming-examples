#!/usr/bin/python3

# access a windows domain controller via ldaps

import ldap
import sys

from pprint import pprint

ldap_uri = 'ldaps://dc1.acme.local:636'
bind_dn = 'ACME\\sam'
bind_pw = 'Secret123'
base_dn = 'CN=users,DC=acme,DC=local'

scope = ldap.SCOPE_SUBTREE
attributes = ['displayName', 'mail']
search_filter = '(&(objectClass=person)(sAMAccountName=rm))'

try:
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    l = ldap.initialize(ldap_uri)
    l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
    l.simple_bind_s(bind_dn, bind_pw)
    rst = l.search_s(base_dn, scope, search_filter, attributes)
    pprint(rst)
    print('mail: {}'.format(rst[0][1]['mail'][0].decode('UTF-8')))
except (KeyError, IndexError, ldap.LDAPError) as e:
    print(e)
    sys.exit(1)
