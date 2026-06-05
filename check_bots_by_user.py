import psycopg2
import os
from dotenv import load_dotenv

load_dotenv('C:/backend/.env')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# Get all users
cur.execute("SELECT user_id, name FROM users ORDER BY created_at DESC")
users = cur.fetchall()

print("=" * 80)
print("BOT STATUS BY USER")
print("=" * 80)

for user_id, user_name in users:
    # Count bots for this user
    cur.execute("SELECT COUNT(*) FROM user_bots WHERE user_id = %s", (user_id,))
    bot_count = cur.fetchone()[0]
    
    if bot_count == 0:
        continue
        
    print(f"\nUser: {user_name} ({user_id})")
    print(f"  Total Bots: {bot_count}")
    
    # Get bots for this user
    cur.execute("""
        SELECT bot_id, name, enabled, is_live, status, symbols
        FROM user_bots 
        WHERE user_id = %s
        ORDER BY created_at DESC
    """, (user_id,))
    
    for bot in cur.fetchall():
        bot_id, name, enabled, is_live, status, symbols = bot
        state = "✓ ON" if enabled else "✗ OFF"
        live = "LIVE" if is_live else "DEMO"
        print(f"    {state} {live} | {name or bot_id} | {status}")
        
conn.close()
