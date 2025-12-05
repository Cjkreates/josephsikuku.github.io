#!/usr/bin/env python3
"""
Health Check and Monitoring Script
Simulates production monitoring and alerting
"""
import json
import time
import random
import os
from datetime import datetime

class PortfolioMonitor:
    def __init__(self):
        self.checks = []
        self.metrics = {}
        
    def check_website_health(self):
        """Check if website components are healthy"""
        print("🔍 Performing health checks...")
        
        health_checks = [
            {
                "name": "Website Availability",
                "check": lambda: os.path.exists("index.html"),
                "critical": True
            },
            {
                "name": "Docker Configuration", 
                "check": lambda: os.path.exists("Dockerfile"),
                "critical": False
            },
            {
                "name": "CI/CD Pipeline",
                "check": lambda: os.path.exists(".github/workflows/my-first-pipeline.yml"),
                "critical": True
            },
            {
                "name": "Infrastructure Code",
                "check": lambda: os.path.exists("terraform/main.tf"),
                "critical": False
            }
        ]
        
        all_healthy = True
        for check in health_checks:
            try:
                result = check["check"]()
                status = "✅ HEALTHY" if result else "❌ UNHEALTHY"
                critical = "🔴 CRITICAL" if check["critical"] else "🟡 NON-CRITICAL"
                print(f"   {status} - {check['name']} ({critical})")
                
                if not result and check["critical"]:
                    all_healthy = False
                    
                self.checks.append({
                    "name": check["name"],
                    "status": "healthy" if result else "unhealthy",
                    "critical": check["critical"],
                    "timestamp": datetime.now().isoformat()
                })
            except Exception as e:
                print(f"   ❌ ERROR - {check['name']}: {e}")
                all_healthy = False
        
        return all_healthy
    
    def collect_metrics(self):
        """Collect system and application metrics"""
        print("\n📊 Collecting performance metrics...")
        
        # Simulate metric collection
        self.metrics = {
            "response_time_ms": random.randint(50, 200),
            "uptime_percentage": random.uniform(99.5, 99.99),
            "memory_usage_mb": random.randint(100, 500),
            "cpu_usage_percent": random.uniform(10, 40),
            "active_connections": random.randint(5, 50),
            "error_rate_percent": random.uniform(0.1, 2.0),
            "throughput_rps": random.randint(100, 1000)
        }
        
        for metric, value in self.metrics.items():
            if "percent" in metric:
                print(f"   📈 {metric}: {value:.2f}%")
            else:
                print(f"   📈 {metric}: {value}")
        
        # Add timestamps
        self.metrics["last_updated"] = datetime.now().isoformat()
        self.metrics["collection_duration_seconds"] = random.uniform(0.1, 0.5)
    
    def generate_alerts(self):
        """Generate alerts based on metrics"""
        print("\n🚨 Generating alerts and notifications...")
        
        alerts = []
        
        # Check for critical conditions
        if self.metrics["error_rate_percent"] > 1.0:
            alerts.append({
                "level": "WARNING",
                "message": "Error rate above 1% threshold",
                "metric": "error_rate_percent",
                "value": self.metrics["error_rate_percent"],
                "timestamp": datetime.now().isoformat()
            })
            print("   🟡 WARNING: Error rate above 1%")
        
        if self.metrics["response_time_ms"] > 150:
            alerts.append({
                "level": "WARNING", 
                "message": "Response time above 150ms threshold",
                "metric": "response_time_ms",
                "value": self.metrics["response_time_ms"],
                "timestamp": datetime.now().isoformat()
            })
            print("   🟡 WARNING: Response time above 150ms")
        
        if self.metrics["uptime_percentage"] < 99.9:
            alerts.append({
                "level": "CRITICAL",
                "message": "Uptime below 99.9% SLA",
                "metric": "uptime_percentage", 
                "value": self.metrics["uptime_percentage"],
                "timestamp": datetime.now().isoformat()
            })
            print("   🔴 CRITICAL: Uptime below 99.9%")
        
        if not alerts:
            print("   ✅ No critical alerts - System healthy!")
            alerts.append({
                "level": "INFO",
                "message": "All systems operational",
                "timestamp": datetime.now().isoformat()
            })
        
        return alerts
    
    def create_monitoring_dashboard(self):
        """Create monitoring dashboard data"""
        print("\n📈 Generating monitoring dashboard...")
        
        dashboard_data = {
            "environment": os.getenv('DEPLOY_ENV', 'production'),
            "timestamp": datetime.now().isoformat(),
            "health_checks": self.checks,
            "metrics": self.metrics,
            "alerts": self.generate_alerts(),
            "system_info": {
                "monitoring_tool": "Portfolio Health Monitor",
                "version": "1.0",
                "checks_performed": len(self.checks),
                "monitoring_duration": f"{random.uniform(0.5, 2.0):.2f}s"
            }
        }
        
        # Save monitoring data
        with open('monitoring-dashboard.json', 'w') as f:
            json.dump(dashboard_data, f, indent=2)
        
        print("   ✅ Monitoring dashboard created: monitoring-dashboard.json")
        return dashboard_data
    
    def run_complete_monitoring(self):
        """Run complete monitoring suite"""
        print("🚀 Starting Comprehensive Monitoring Suite")
        print("=" * 50)
        
        start_time = time.time()
        
        # Run all monitoring steps
        health_ok = self.check_website_health()
        self.collect_metrics()
        dashboard = self.create_monitoring_dashboard()
        
        duration = time.time() - start_time
        
        print("\n" + "=" * 50)
        print("🎯 MONITORING SUMMARY")
        print("=" * 50)
        
        # Health status
        health_status = "✅ HEALTHY" if health_ok else "❌ UNHEALTHY"
        print(f"System Health: {health_status}")
        
        # Key metrics summary
        print(f"Response Time: {self.metrics['response_time_ms']}ms")
        print(f"Uptime: {self.metrics['uptime_percentage']:.2f}%")
        print(f"Error Rate: {self.metrics['error_rate_percent']:.2f}%")
        
        # Alert summary
        critical_alerts = len([a for a in dashboard['alerts'] if a['level'] == 'CRITICAL'])
        warning_alerts = len([a for a in dashboard['alerts'] if a['level'] == 'WARNING'])
        
        print(f"Alerts: {critical_alerts} Critical, {warning_alerts} Warning")
        print(f"Monitoring Duration: {duration:.2f}s")
        
        print("\n📊 Monitoring data saved for observability!")
        return health_ok

def main():
    """Main monitoring execution"""
    monitor = PortfolioMonitor()
    
    try:
        healthy = monitor.run_complete_monitoring()
        
        if healthy:
            print("\n🎉 Monitoring complete - System operational!")
            return True
        else:
            print("\n⚠️  Monitoring complete - Some issues detected!")
            return False
            
    except Exception as e:
        print(f"\n❌ Monitoring failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)