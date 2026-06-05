import psycopg2
import os
from dotenv import load_dotenv

load_dotenv('C:/backend/.env')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# Check Max's user
cur.execute("SELECT user_id, name, email FROM users WHERE email ILIKE '%max%mabuti%'")
max_user = cur.fetchone()
if max_user:
    print(f'✓ Max found: {max_user[1]} ({max_user[2]})')
    max_id = max_user[0]
    
    # Check bots for Max
    cur.execute('SELECT bot_id, name, enabled FROM user_bots WHERE user_id = %s', (max_id,))
    bots = cur.fetchall()
    print(f'  Bots: {len(bots)}')
    for bot in bots:
        status = "✓ ON" if bot[2] else "✗ OFF"
        print(f'    {status} | {bot[0]} | {bot[1]}')
else:
    print('✗ Max not found')

# Check the specific bot by ID
print('\nSearching for bot 1780668929413...')
cur.execute("SELECT bot_id, user_id, name, enabled FROM user_bots WHERE bot_id LIKE '%1780668929413%'")
result = cur.fetchone()
if result:
    print(f'✓ Bot found: {result}')
else:
    print('✗ Bot not found')

# Show all bots
print('\n' + '=' * 80)
print('ALL BOTS IN DATABASE:')
cur.execute("SELECT user_id, bot_id, name, enabled, created_at FROM user_bots ORDER BY created_at DESC LIMIT 20")
for row in cur.fetchall():
    enabled = "✓" if row[3] else "✗"
    print(f"{enabled} {row[1][:20]:20} | {row[2][:20]:20} | {row[4]}")

conn.close()
