from .app import create_database, delete_database

# Delete any previous
# data in the database along with
# its tables
delete_database()

# Create the database
create_database()
