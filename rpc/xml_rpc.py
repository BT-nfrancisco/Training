import xmlrpc.client

# Indicate your HOST, PORT, DB, USER, PASS

root = 'http://%s:%d/xmlrpc/' % ('localhost', 8069)
uid = xmlrpc.client.ServerProxy(root + 'common').login('training', 'admin',
                                                       'admin')
print("Logged in as %s (uid: %d)" % ('frna1', uid))
print("\nList of sessions:\n")
# Read Demo User db id
sock = xmlrpc.client.ServerProxy(root + 'object')

session_ids = sock.execute('training', uid, 'admin', 'session', 'search',
                           [])

records = sock.execute_kw('training', uid, 'admin', 'session', 'read',
                          [session_ids])

print("\n Method 1:")

for record in records:
    print('\t- Session: ' + record['name'] + ' - Number of seats: ' + str(
        record['number_of_seats']))

print("\n Method 2:")

records2 = sock.execute_kw(
    'training', uid, 'admin', 'session', 'search_read',
    [], {'fields': ['name', 'number_of_seats']})

for record in records2:
    print('\t- Session: ' + record['name'] + ' - Number of seats: ' + str(
        record['number_of_seats']))

print("\nCreating new record")

courses_id = sock.execute('training', uid, 'admin', 'course', 'search',
                          [])

course_name = "Flying with your brain"

id = sock.execute_kw('training', uid, 'admin', 'session', 'create', [{
    'name': course_name, 'number_of_seats': 50,
    'course_id': courses_id[0], 'duration': '5'
}])

print("Added course " + course_name + " with id " + str(id))
print("Added course {} with id {}".format(course_name, id))
