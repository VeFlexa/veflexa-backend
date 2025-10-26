def generate_plan(fleet_id: int):
    # Mock plan — reemplazaremos por heurístico real
    hours = range(24)
    plan = [
        {"hour": h, "charger_id": 1, "status": "on" if h in [1,2,3,4] else "off"}
        for h in hours
    ]
    return plan
