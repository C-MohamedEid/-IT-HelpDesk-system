from ticket import Ticket
import json
import os

class TicketManager:
    def __init__(self, data_file="data/tickets.json"):
        self.tickets = []
        self.data_file = data_file
        self.load_tickets()
        self.next_ticket_id = self.determine_next_id()
        

    def determine_next_id(self):
        current_ids = []
        for ticket in self.tickets:
            try:
                num_part = int(ticket.ticket_id[2:])
                current_ids.append(num_part)
            except ValueError:
                continue    
        if not current_ids:
            return 1
        else:
            return max(current_ids) + 1
        
    def generate_ticket_id(self):
        ticket_id = f"TK{self.next_ticket_id:03d}"
        self.next_ticket_id += 1
        return ticket_id
    
    def save_tickets(self):
        tickets_data = []
        folder_path = os.path.dirname(self.data_file)
        for ticket in self.tickets:
            ticket_dict = ticket.to_dict()
            tickets_data.append(ticket_dict)
        try:
            os.makedirs(folder_path, exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump(tickets_data, f, indent=5)
        except Exception as e:
                print(f"Error saving tickets to {self.data_file}: {e}")
                return False
        return True
    
    def load_tickets(self):
        if not os.path.exists(self.data_file):
            print("Data file not found. Creating a new one when first ticket is added.")
            return
        try:
            with open(self.data_file, "r") as f:
                tickets_data = json.load(f)
                for ticket_dict in tickets_data:
                    ticket = Ticket(**ticket_dict)
                    self.tickets.append(ticket)
        except json.JSONDecodeError:
            print(f"Error: The data file {self.data_file} is corrupted or not in valid JSON format.")
        except Exception as e:
            print(f"Error loading tickets from {self.data_file}: {e}")
            self.tickets = []


    def add_ticket(self, employee_name, department, issue_type, description, priority):
        ticket_id = self.generate_ticket_id()
        ticket = Ticket(ticket_id, employee_name, department, issue_type, description, priority)
        self.tickets.append(ticket)
        self.save_tickets()
        return ticket
    
    def search_by_id(self,ticket_id):
        for ticket in self.tickets:
            if ticket_id.upper() == ticket.ticket_id.upper():
                return ticket
        return None
    
    def search_by_department(self, department):
        result = []
        for ticket in self.tickets:
            if department.upper() == ticket.department.upper():
                result.append(ticket)
        return result
        
    def ticket_update_status(self, ticket_id, new_status):
        ticket = self.search_by_id(ticket_id)
        if ticket:
            ticket.update_status(new_status)
            self.save_tickets()
        return True
       


    

