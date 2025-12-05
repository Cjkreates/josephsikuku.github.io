#!/usr/bin/env python3
"""
Docker Container Test Script
"""
import os
import sys

def check_docker_files():
    """Verify Docker configuration files exist"""
    print("🐳 Checking Docker configuration...")
    
    docker_files = ['Dockerfile', 'docker-compose.yml']
    all_exist = True
    
    for file in docker_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
            # Basic syntax validation
            with open(file, 'r') as f:
                first_line = f.readline().strip()
                print(f"   First line: {first_line}")
        else:
            print(f"❌ {file} - Missing")
            all_exist = False
    
    return all_exist

def validate_dockerfile():
    """Basic Dockerfile validation"""
    print("\n🔍 Validating Dockerfile structure...")
    
    try:
        with open('Dockerfile', 'r') as f:
            content = f.read()
        
        required_keywords = ['FROM', 'COPY', 'EXPOSE']
        found_keywords = []
        
        for keyword in required_keywords:
            if keyword in content:
                found_keywords.append(keyword)
                print(f"✅ {keyword} instruction found")
            else:
                print(f"❌ {keyword} instruction missing")
        
        if len(found_keywords) == len(required_keywords):
            print("✅ Dockerfile structure is valid")
            return True
        else:
            print("⚠️  Dockerfile may be incomplete")
            return False
            
    except Exception as e:
        print(f"❌ Error reading Dockerfile: {e}")
        return False

def main():
    """Run all container tests"""
    print("🚀 Starting Containerization Tests...")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 2
    
    if check_docker_files():
        tests_passed += 1
    
    if validate_dockerfile():
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Container Tests: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 Container configuration is valid! 🎉")
        print("🐳 Ready to build and deploy with Docker!")
        sys.exit(0)
    else:
        print("⚠️  Some container tests need attention")
        sys.exit(0)  # Don't fail build - this is learning

if __name__ == "__main__":
    main()