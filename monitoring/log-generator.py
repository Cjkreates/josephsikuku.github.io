#!/usr/bin/env python3
"""
Log Generation Script
Simulates application logging for observability
"""
import json
import time
from datetime import datetime
import random

def generate_application_logs():
    """Generate simulated application logs"""
    log_levels = ['INFO', 'DEBUG', 'WARN', 'ERROR']
    log_messages = {
        'INFO': [
            "User visited portfolio page",
            "Health check completed successfully",
            "Docker container started",
            "CI/CD pipeline initiated",
            "Infrastructure deployment started"
        ],
        'DEBUG': [
            "Processing request for /index.html",
            "Loading environment configuration",
            "Container health check in progress",
            "Metric collection started"
        ],
        'WARN': [
            "High response time detected",
            "Memory usage above 80% threshold",
            "Database connection slow",
            "CDN cache miss rate increasing"
        ],
        'ERROR': [
            "Failed to load configuration file",
            "Health check timeout",
            "Container failed to start",
            "Deployment rollback initiated"
        ]
    }
    
    logs = []
    
    # Generate random logs
    for _ in range(15):
        level = random.choice(log_levels)
        message = random.choice(log_messages[level])
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            "service": "portfolio-website",
            "environment": "production",
            "request_id": f"req-{random.randint(1000, 9999)}",
            "duration_ms": random.randint(10, 500) if level in ['INFO', 'DEBUG'] else None
        }
        
        # Add error details for ERROR logs
        if level == 'ERROR':
            log_entry["error_details"] = {
                "stack_trace": "Simulated stack trace for monitoring demo",
                "component": random.choice(["web-server", "database", "cdn", "auth"])
            }
        
        logs.append(log_entry)
        time.sleep(0.1)  # Simulate time passing
    
    return logs

def main():
    """Generate and save application logs"""
    print("📝 Generating application logs for observability...")
    
    logs = generate_application_logs()
    
    # Save logs to file
    with open('application-logs.json', 'w') as f:
        json.dump(logs, f, indent=2)
    
    # Print log summary
    print(f"✅ Generated {len(logs)} log entries")
    
    level_counts = {}
    for log in logs:
        level = log['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    print("📊 Log Level Distribution:")
    for level, count in level_counts.items():
        print(f"   {level}: {count} entries")
    
    print("💾 Logs saved to: application-logs.json")
    print("🔍 Use these for debugging and monitoring!")

if __name__ == "__main__":
    main()