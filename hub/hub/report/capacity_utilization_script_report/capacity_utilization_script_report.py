import frappe

def execute(filters=None):
    columns = [
        {"label": "Event", "fieldname": "name", "fieldtype": "Link", "options": "Event Doctype", "width": 150},
        {"label": "Capacity", "fieldname": "capacity", "fieldtype": "Int", "width": 100},
        {"label": "Registered", "fieldname": "registered", "fieldtype": "Int", "width": 100},
        {"label": "Utilization %", "fieldname": "utilization", "fieldtype": "Float", "width": 120},
    ]

    events = frappe.db.get_all("Event Doctype", fields=["name", "capacity"])

    data = []
    for e in events:

        # Convert capacity to int safely
        capacity = int(e.capacity or 0)

        # Count participants
        registered = frappe.db.count("Participants Doctype", {"event": e.name})

        utilization = 0
        if capacity > 0:
            utilization = (registered / capacity) * 100

        data.append({
            "name": e.name,
            "capacity": capacity,
            "registered": registered,
            "utilization": utilization
        })

    return columns, data
