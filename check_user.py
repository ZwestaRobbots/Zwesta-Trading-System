import psycopg2
import os
from dotenv import load_dotenv

load_dotenv('C:/backend/.env')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

cur.execute("SELECT * FROM users LIMIT 1")
columns = [desc[0] for desc in cur.description]
print(f"Columns: {columns}")

cur.execute("SELECT * FROM users WHERE name ILIKE %s OR email ILIKE %s", ('%Max%Mabuti%', '%max%mabuti%'))
rows = cur.fetchall()

if rows:
    print('\n✓ User Found:')
    for row in rows:
        user_data = dict(zip(columns, row))
        print(f"  User ID: {user_data['user_id']}")
        print(f"  Name: {user_data['name']}")
        print(f"  Email: {user_data['email']}")
        print(f"  Created: {user_data['created_at']}")
        print(f"  Commission: {user_data['total_commission']}")
else:
    print('\n✗ User not found in database')

conn.close()
