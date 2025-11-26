// Copyright (c) 2025, keerthi and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Participant Doctype", {
    validate(frm) {
        if (!frm.doc.event) return;

        // Step 1: Get Event details
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Event",
                name: frm.doc.event
            },
            callback(r) {
                if (!r.message) return;

                const capacity = r.message.capacity;
                if (!capacity) return;

                // Step 2: Count participants already registered
                frappe.call({
                    method: "frappe.db.count",
                    args: {
                        doctype: "Participant",
                        filters: { event: frm.doc.event }
                    },
                    callback(res) {
                        const registered = res.message || 0;

                        // Allow editing existing record
                        if (frm.is_new() && registered >= capacity) {
                            frappe.msgprint(
                                __("Event capacity is full ({0}). No more registrations allowed.", [capacity])
                            );
                            frappe.validated = false; // Stop saving
                        }
                    }
                });
            }
        });
    },

    // ---------------------------------------------
    // 2️⃣ Add "Generate Certificate" Button
    // ---------------------------------------------
    refresh(frm) {
        // Button only visible when doc is saved
        if (!frm.is_new()) {
            frm.add_custom_button("Generate Certificate", () => {
                frappe.call({
                    method: "control.control.doctype.ParticipantsDoctype.participant.generate_certificate",
                    args: { participant: frm.doc.name },
                    callback(r) {
                        if (r.message) {
                            frappe.msgprint("Certificate Created: " + r.message);
                            frappe.set_route("Form", "Event Certificate", r.message);
                        } else {
                            frappe.msgprint("Could not generate certificate.");
                        }
                    }
                });
            });
        }
    }
});
