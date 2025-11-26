import frappe

def execute(filters=None):
    columns = [
        {"label": "Event", "fieldname": "event", "fieldtype": "Link", "options": "Event", "width": 150},
        {"label": "Participant Name", "fieldname": "participant_name", "fieldtype": "Data", "width": 200},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data", "width": 200},
        {"label": "Checked In", "fieldname": "checked_in", "fieldtype": "Check", "width": 100},
    ]

    data = frappe.db.get_all(
        "Participants Doctype",
        fields=["event", "participant_name", "email", "checked_in"],
        order_by="event, participant_name"
    )

    return columns, data
