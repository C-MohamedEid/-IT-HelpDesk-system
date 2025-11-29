from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, employee_name, department, issue_type, description, priority):
        self.ticket_id = ticket_id
        self.employee_name = employee_name
        self.department = department  
        self.issue_type = issue_type
        self.description = description
        self.priority = priority
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = "Open"

    def update_status(self, new_status):
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
    
