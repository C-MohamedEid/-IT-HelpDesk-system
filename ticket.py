from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, employee_name, department, issue_type, description, priority, date_created=None, status="Open"):
        self.ticket_id = ticket_id
        self.employee_name = employee_name
        self.department = department  
        self.issue_type = issue_type
        self.description = description
        self.priority = priority

        if date_created is None:
            self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.date_created = date_created
        self.status = status

    def update_status(self, new_status):
        valid_statuses = ["Open", "In Progress", "Closed", "On Hold"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}")
        self.status = new_status

    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "employee_name": self.employee_name,
            "department": self.department,
            "issue_type": self.issue_type,
            "description": self.description,
            "priority": self.priority,
            "date_created": self.date_created,
            "status": self.status
        }
    
