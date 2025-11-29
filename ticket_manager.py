from ticket import Ticket


class TicketManager:
    def __init__(self, data_file="data/tickets.json"):
        self.tickets = []
        self.data_file = data_file
        self.next_ticket_id = 1
        self.load_tickets()


    def generate_ticket_id(self):
        ticket_id = f"TK{self.next_ticket_id:03d}"
        self.next_ticket_id += 1
        return ticket_id
    

    def add_ticket(self, employee_name, department, issue_type, description, priority):
        ticket_id = self.generate_ticket_id()
        ticket = Ticket(ticket_id, employee_name, department, issue_type, description, priority)
        self.tickets.append(ticket)
        self.save_tickets()
        return ticket
    
    def search_by_id(self,ticket_id):
        for ticket in self.tickets:
            if ticket_id == ticket.ticket_id:
                return ticket
        return None
    
    def search_by_department(self, department):
        result = []
        for ticket in self.tickets:
            if department == ticket.department:
                result.append(ticket)
                return result
        return None

    def ticket_updat_status(self, ticket_id, new_status):
        ticket = self.search_by_id(ticket_id)
        if ticket:
            ticket.update_status(new_status)
            self.save_tickets()
            return ticket
        return None


    

