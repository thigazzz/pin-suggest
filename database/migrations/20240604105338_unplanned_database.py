"""
This module contains a Caribou migration.

Migration Name: unplanned_database 
Migration Version: 20240604105338
"""

def upgrade(connection):
    # add your upgrade step here
    sql = 'CREATE TABLE IF NOT EXISTS favorites(id, title, link, topic)'
    connection.execute(sql)
    connection.commit()

def downgrade(connection):
    # add your downgrade step here
     connection.execute('DROP TABLE favorites')
