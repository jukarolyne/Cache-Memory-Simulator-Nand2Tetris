#!/usr/bin/env python3
"""
Demo: Upload .asm file via API

Shows how to upload a Hack assembly file to the converter API.
"""

import requests
import sys
from pathlib import Path

BASE_URL = "http://127.0.0.1:5000"
USERNAME = "admin"
PASSWORD = "admin"

def get_token():
    """Login and get authentication token."""
    response = requests.post(f"{BASE_URL}/api/login", json={
        "username": USERNAME,
        "password": PASSWORD
    })
    data = response.json()
    if not data.get("ok"):
        raise Exception(f"Login failed: {data.get('error')}")
    return data["token"]

def upload_and_convert_file(token, file_path):
    """Upload and convert a Hack assembly file."""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return False
    
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(
            f"{BASE_URL}/api/convert-hack-file",
            headers={"Authorization": f"Bearer {token}"},
            files=files
        )
    
    result = response.json()
    
    if result.get("ok"):
        print(f"Conversion successful!")
        print(f"  File: {result.get('filename')}")
        print(f"  Sequences: {result.get('count')}")
        print(f"\n  Generated sequences:")
        for i, seq in enumerate(result.get('sequences', []), 1):
            print(f"    {i:2d}. {seq}")
        return True
    else:
        print(f"Conversion failed: {result.get('error')}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"""
Usage: python upload_hack_file.py <file.asm>

Example:
    python upload_hack_file.py example_program.asm
    python upload_hack_file.py my_program.asm

Requirements:
    • Flask server must be running: python web_backend.py
    • Server must have admin user (default: admin/admin)
    • File must be readable text (.asm, .hack, or .txt)
        """)
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        print("Logging in...")
        token = get_token()
        print("Logged in\n")
        
        print(f"Uploading and converting: {file_path}")
        upload_and_convert_file(token, file_path)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
