import psycopg2
import os
from dotenv import load_dotenv
from uuid import uuid4
from werkzeug.security import generate_password_hash
from datetime import datetime

load_dotenv('C:/backend/.env')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# Create new user
user_id = str(uuid4())
name = "Max Mabuti"
email = "max.mabuti@zwesta.com"
password_hash = generate_password_hash("MaxMabuti@2026!")
referral_code = f"MM{uuid4().hex[:8].upper()}"
created_at = datetime.utcnow()

try:
    cur.execute("""
        INSERT INTO users (user_id, email, name, referrer_id, referral_code, created_at, total_commission, password_hash, internal_balance)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, email, name, None, referral_code, created_at, 0.0, password_hash, 0.0))
    
    conn.commit()
    print(f"✓ User created successfully!")
    print(f"  User ID: {user_id}")
    print(f"  Name: {name}")
    print(f"  Email: {email}")
    print(f"  Password: MaxMabuti@2026!")
    print(f"  Referral Code: {referral_code}")
    
except Exception as e:
    conn.rollback()
    print(f"✗ Error creating user: {e}")

conn.close()
