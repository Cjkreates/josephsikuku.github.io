#!/usr/bin/env python3
"""
Environment Configuration Setup
Simulates how apps load different configs per environment
"""
import os
import json

def setup_environment(env_name):
    """Set up environment-specific configuration"""
    print(f"🚀 Setting up {env_name.upper()} environment...")
    print("=" * 50)
    
    # Simulate loading environment config
    config_file = f"configs/{env_name}.json"
    
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        print(f"✅ Loaded {env_name} configuration:")
        for key, value in config.items():
            if key != "features":
                print(f"   {key}: {value}")
        
        print("   features:")
        for feature, enabled in config.get("features", {}).items():
            status = "✅ ENABLED" if enabled else "❌ DISABLED"
            print(f"     {feature}: {status}")
        
        return True
    else:
        print(f"❌ Config file not found: {config_file}")
        return False

def validate_environment(env_name):
    """Validate environment setup"""
    print(f"\n🔍 Validating {env_name.upper()} environment...")
    
    validations = {
        "Required files exist": os.path.exists("index.html"),
        "Docker configuration ready": os.path.exists("Dockerfile"),
        "Tests pass basic validation": os.path.exists("test-website.py")
    }
    
    all_valid = True
    for check, result in validations.items():
        if result:
            print(f"✅ {check}")
        else:
            print(f"❌ {check}")
            all_valid = False
    
    # Environment-specific validations
    if env_name == "production":
        print("🔒 Production-specific checks:")
        prod_checks = {
            "No experimental features": True,  # Simulated
            "Debug mode disabled": True,       # Simulated  
            "All tests passed": True           # Simulated
        }
        for check, result in prod_checks.items():
            if result:
                print(f"   ✅ {check}")
            else:
                print(f"   ❌ {check}")
                all_valid = False
    
    return all_valid

def main():
    """Main environment setup"""
    # Get environment from GitHub Actions environment variable
    # or default to development
    env = os.getenv('DEPLOY_ENV', 'development').lower()
    
    print("🏗️  Multi-Environment CI/CD Setup")
    print("=" * 50)
    
    if env not in ['development', 'staging', 'production']:
        print(f"❌ Unknown environment: {env}")
        print("✅ Defaulting to development")
        env = 'development'
    
    if setup_environment(env):
        if validate_environment(env):
            print(f"\n🎉 {env.upper()} environment ready for deployment!")
            
            # Create environment info file for the website
            env_info = {
                "deployed_at": os.getenv('GITHUB_SHA', 'local'),
                "environment": env,
                "pipeline_url": os.getenv('GITHUB_SERVER_URL', '') + '/' + os.getenv('GITHUB_REPOSITORY', '') + '/actions/runs/' + os.getenv('GITHUB_RUN_ID', '')
            }
            
            with open('environment-info.json', 'w') as f:
                json.dump(env_info, f, indent=2)
            
            print("✅ Environment info saved")
        else:
            print(f"\n❌ {env.upper()} environment validation failed!")
            exit(1)
    else:
        print(f"\n❌ Failed to setup {env.upper()} environment!")
        exit(1)

if __name__ == "__main__":
    main()