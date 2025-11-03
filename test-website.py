#!/usr/bin/env python3
"""
CI/CD Test Script for Portfolio Website
"""
import os
import sys

def main():
    print("🚀 Testing Portfolio Website for CI/CD")
    print("=" * 50)
    
    # Check essential files
    required_files = ['index.html', 'README.md']
    all_good = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Missing")
            all_good = False
    
    # Check file sizes (basic validation)
    if os.path.exists('index.html'):
        size = os.path.getsize('index.html')
        if size > 100:  # At least 100 bytes
            print(f"✅ index.html has content ({size} bytes)")
        else:
            print(f"⚠️  index.html seems very small ({size} bytes)")
    
    print("=" * 50)
    
    if all_good:
        print("🎉 All checks passed! Ready for deployment!")
        sys.exit(0)
    else:
        print("❌ Some checks failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
EOF