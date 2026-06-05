import psycopg2
import os
from dotenv import load_dotenv
import json

load_dotenv('C:/backend/.env')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# First, get schema info
cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='user_bots' ORDER BY ordinal_position")
columns = cur.fetchall()
print("user_bots table columns:")
for col_name, col_type in columns:
    print(f"  - {col_name}: {col_type}")
print()

# Get all bots
cur.execute("""
    SELECT * FROM user_bots 
    ORDER BY created_at DESC
    LIMIT 15
""")

bots = cur.fetchall()
print("=" * 80)
print(f"RECENT BOTS ({len(bots)} total)")
print("=" * 80)

# Get column names for reference
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='user_bots' ORDER BY ordinal_position")
col_names = [row[0] for row in cur.fetchall()]

for bot in bots:
    bot_dict = dict(zip(col_names, bot))
    bot_id = bot_dict.get('bot_id', 'N/A')
    user_id = bot_dict.get('user_id', 'N/A')
    is_active = bot_dict.get('is_active', False)
    created = bot_dict.get('created_at', 'N/A')
    
    status = "✓ ACTIVE" if is_active else "✗ INACTIVE"
    print(f"\n{status}")
    print(f"  Bot ID: {bot_id}")
    print(f"  User: {user_id}")
    print(f"  Created: {created}")
    for key, value in bot_dict.items():
        if key not in ['bot_id', 'user_id', 'is_active', 'created_at']:
            if value and str(value).strip():
                print(f"  {key}: {str(value)[:60]}")

# Count active bots
print("\n" + "=" * 80)
cur.execute("SELECT COUNT(*) FROM user_bots WHERE is_active = true")
active_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM user_bots")
total_count = cur.fetchone()[0]

print(f"SUMMARY: {active_count} active out of {total_count} total bots")
print("=" * 80)

if active_count == 0 and total_count > 0:
    print("⚠️  NO ACTIVE BOTS - They need to be activated!")
elif active_count > 0:
    print(f"✓ {active_count} bots should be trading")

conn.close()
