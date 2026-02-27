# def calculate_risk(port):
#     if port in [22, 3389, 27017, 21]:
#         return "High"
#     elif port in [80, 443]:
#         return "Medium"
#     else:
#         return "Low"


# def enrich_assets_with_risk(assets):
#     enriched = []

#     for asset in assets:
#         risk = calculate_risk(asset["port"])
#         enriched.append({**asset, "risk": risk})

#     return enriched
def calculate_risk(port):
    high_risk_ports = [22, 3389, 27017, 21, 23]
    medium_risk_ports = [80, 443, 8080]

    if port in high_risk_ports:
        return "High"
    elif port in medium_risk_ports:
        return "Medium"
    else:
        return "Low"


def get_risk_reason(port):
    reasons = {
        22: "SSH exposed to internet",
        3389: "RDP exposed to internet",
        27017: "MongoDB database exposed",
        21: "FTP service exposed",
        23: "Telnet exposed (very risky)",
        80: "HTTP web service exposed",
        443: "HTTPS service exposed",
        8080: "Alternative HTTP service exposed"
    }

    return reasons.get(port, "Unknown service exposed")


def enrich_assets_with_risk(assets):
    enriched = []

    for asset in assets:
        risk = calculate_risk(asset["port"])
        reason = get_risk_reason(asset["port"])

        enriched.append({
            **asset,
            "risk": risk,
            "reason": reason
        })

    return enriched