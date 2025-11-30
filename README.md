#### IT Helpdesk Ticketing System ####
This application provides an interactive Command-Line Interface (CLI) for efficient management of IT support requests

### Key Project Requirements Covered:
1. Object-Oriented Programming (OOP)
2. File Processing (JSON)
3. Error Handling and Exceptions


### Key Features :
* **Ticket Creation:** Automatically generates unique ticket IDs (e.g., `TK001`, `TK002`).
* **Data Persistence:** Tickets are automatically saved to and loaded from a `tickets.json` file upon system startup and closure.
* **Status Management:** Allows updating a ticket's status to valid, case-sensitive options: ('Open', `In Progress', 'Closed', 'On Hold').
* **Search Functionality:** Supports searching for tickets by their ID or filtering all tickets by Department.
* **Robust Error Handling:** Implements validation to ensure data integrity, preventing the entry of invalid status values. If you enter closed (lowercase), the system will output an error message (Invalid status: closed. Must be one of [...]) and return to the main menu without crashing


### Installation and Usage


*** 1. Prerequisites

Ensure you have Python (version 3.6 or higher) installed.

*** 2. Setup


# Clone the repository
git clone [C-MohamedEid/-IT-HelpDesk-system]
cd [IT_helpdesk_System]

# If external requirements are added later, install them:
# pip install -r requirements.txt

Author: 

Prepared by : [Mohamed_Eid]