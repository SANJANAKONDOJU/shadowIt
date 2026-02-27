from collections import Counter
import random

def generate_dashboard_data(assets):

    risk_counts = Counter([a["risk"] for a in assets])
    port_counts = Counter([a["port"] for a in assets])

    return {
        "threats_detected": len(assets),
        "threat_level": min(100, risk_counts.get("High", 0) * 20),
        "devices_monitored": len(assets),
        "detection_rate": round(random.uniform(95, 99.9), 2),
        "response_time": round(random.uniform(0.5, 2.0), 2),
        "timeline_data": [random.randint(10, 50) for _ in range(6)],
        "open_ports_distribution": dict(port_counts),
        "threat_feed": [
            f"{a['risk']} risk exposure detected on {a['ip']}:{a['port']}"
            for a in assets[:5]
        ]
    }