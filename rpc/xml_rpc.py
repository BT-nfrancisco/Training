import xmlrpc.client

# Indicate your HOST, PORT, DB, USER, PASS

root = 'http://%s:%d/xmlrpc/' % ('localhost', 8069)
uid = xmlrpc.client.ServerProxy(root + 'common').login('training', 'admin',
                                                       'admin')
print("Logged in as %s (uid: %d)" % ('frna1', uid))

# Read Demo User db id
sock = xmlrpc.client.ServerProxy(root + 'object')
args = [('name', '=', 'Demo User')]
demo_user_id = sock.execute('training', uid, 'admin', 'res.partner', 'search',
                            args)
print(demo_user_id)

session_ids = sock.execute('training', uid, 'admin', 'session', 'search',
                           [])
for session in session_ids:
    print(session)

records = sock.execute_kw('training', uid, 'admin', 'session', 'read', [session_ids])

for record in records:
    print('Session: ' + record['name'] + ' - Number of seats: ' + str(
        record['number_of_seats']))
