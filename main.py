from ticket_manager import TicketManager

def main():
    print("===============================================================")
    print("Welcome to the IT Helpdesk Ticketing System")
    print("===============================================================")

    manager = TicketManager()
    print(f"System initialized. Total tickets loaded:{len(manager.tickets)}")
    print("-"*60)
    while True:
        print("================ MENU ================")
        print("1. Add New Ticket")
        print("2. Search by ID")
        print("3. Search by Department")
        print("4. Update Ticket Status")
        print("5. Show All Tickets")
        print("6. Exit")
        print("--------------------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            employee_name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            issue_type = input("Enter Issue Type: ")
            description = input("Enter Description: ")
            priority = input("Enter Priority (Low/Medium/High): ")
            ticket = manager.add_ticket(employee_name, department, issue_type, description, priority)
            print(f"Ticket {ticket.ticket_id} created successfully.")
        
        elif choice == "2":
            ticket_id = input("Enter Ticket ID to search: ").strip().upper()
            result = manager.search_by_id(ticket_id)
            if result:
                print(f" Ticket Found: {result.employee_name} *** Dept: {result.department} *** Status: {result.status}")
            else:
                print("Ticket not found.")

        elif choice == "3":
            department = input("Enter Department to search: ").upper()
            results = manager.search_by_department(department)
            if results:
                print(f"Tickets in Department Found {department}:")
                for ticket in results:
                    print(f" - ID: {ticket.ticket_id}, Employee: {ticket.employee_name}, Status: {ticket.status}")
            else:
                print("No tickets found for this department.")

        elif choice == "4":
            ticket_id = input("Enter Ticket ID to update: ").strip().upper()
            ticket = manager.search_by_id(ticket_id)
            if not ticket:
                print("Ticket not found.")
                continue
            print(f"Current Status: {ticket.status}")
            new_status = input("Enter new status (valid options: Open/In Progress/Closed/On Hold): ")
            try:
                success =manager.ticket_update_status(ticket_id, new_status)
                if success:
                    print("Ticket status updated successfully.")
                else:
                    print("Failed to update ticket status.")
            except ValueError as e:
                print(e)
            
        elif choice == "5":
            if not manager.tickets:
                print("No tickets available.")
            else:
                print("All Tickets:")
                for ticket in manager.tickets:
                    print(f" *** ID: {ticket.ticket_id}, *** Employee: {ticket.employee_name}, *** Dept: {ticket.department}, *** Status: {ticket.status}")

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
