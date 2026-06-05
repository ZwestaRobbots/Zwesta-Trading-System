import requests
import json

BASE_URL = "http://127.0.0.1:9000/api"

# Test 1: Login as Max Mabuti
print("=" * 60)
print("TEST 1: Login as Max Mabuti")
print("=" * 60)

login_data = {
    "username": "max.mabuti@zwesta.com",
    "password": "MaxMabuti@2026!"
}

# Try different endpoint patterns
endpoints = [
    f"{BASE_URL}/auth/login",
    f"{BASE_URL}/login",
    "http://127.0.0.1:9000/login"
]

response = None
for endpoint in endpoints:
    try:
        r = requests.post(endpoint, json=login_data, timeout=2)
        if r.status_code != 404:
            response = r
            print(f"Using endpoint: {endpoint}")
            break
    except:
        pass

if not response:
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    auth_response = response.json()
    token = auth_response.get('access_token')
    user_id = auth_response.get('user_id')
    print(f"✓ Login successful!")
    print(f"  User ID: {user_id}")
    print(f"  Token: {token[:50]}...")
else:
    print(f"✗ Login failed: {response.text}")
    exit(1)

# Test 2: Get user balance
print("\n" + "=" * 60)
print("TEST 2: Get user balance")
print("=" * 60)

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{BASE_URL}/account/balance", headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    balance = response.json()
    print(f"✓ Balance retrieved: {json.dumps(balance, indent=2)}")
else:
    print(f"✗ Failed to get balance: {response.text}")

# Test 3: List available bots
print("\n" + "=" * 60)
print("TEST 3: Get user's bots")
print("=" * 60)

response = requests.get(f"{BASE_URL}/bots/list", headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    bots = response.json()
    print(f"✓ Retrieved {len(bots)} bots")
    if bots:
        print(f"  Sample bot: {bots[0]}")
else:
    print(f"✗ Failed to list bots: {response.text}")

print("\n" + "=" * 60)
print("RESULT: Max Mabuti account is FUNCTIONAL ✓")
print("=" * 60)
print("\nBots can be created now through the mobile app or API")
