# Copyright (c) 2025, keerthi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EventDoctype(Document):

    def validate(self):
        # Convert capacity to int safely
        capacity = frappe.utils.cint(self.capacity)

        # If capacity is zero or missing, skip checks
        if not capacity:
            return

        # Count participants linked to this event
        registered = frappe.db.count("Participant Doctype", {"event": self.name})

        # Update status based on capacity
        if registered >= capacity:
            self.status = "Full"
        else:
            self.status = "Open"

