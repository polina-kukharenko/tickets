from tables import Tickets, Comments
from app import database
from datetime import datetime


def create_ticket(title: str, body: str, email: str) -> int:
    new_ticket = Tickets(title=title, body=body, email=email)
    database.session.add(new_ticket)
    database.session.commit()
    return new_ticket.ticket_id


def change_status(ticket_id: int, status: str) -> None:
    if status == 'opened':
        raise Exception(f'Ticket #{ticket_id} is already opened')
    if status in ['answered', 'awaiting', 'closed']:
        ticket = Tickets.query.filter(Tickets.ticket_id == ticket_id).first()
        if ticket.status == 'closed':
            raise Exception(f'Ticket #{ticket_id} is already closed and its status cannot be changed')
        else:
            if ticket.status == status:
                raise Exception(f'Ticket #{ticket_id} is already in <{status}> status')
            else:
                Tickets.query.filter(Tickets.ticket_id == ticket_id).update(
                    {Tickets.status: status, Tickets.change_datetime: datetime.now()}
                )
                database.session.commit()
    else:
        raise Exception(f'Unknown status <{status}>')


def show_ticket(ticket_id: int) -> Tickets:
    return Tickets.query.filter(Tickets.ticket_id == ticket_id).first()


def add_comment(ticket_id: int, comment_text: str, email: str) -> Comments:
    ticket = show_ticket(ticket_id=ticket_id)
    if not ticket:
        raise Exception(f'Ticket #{ticket_id} not found')
    if ticket.status == 'closed':
        raise Exception(f'Ticket #{ticket_id} is already closed and comment cannot be added')
    else:
        timestamp = datetime.now()
        new_comment = Comments(ticket_id=ticket_id, comment=comment_text, email=email, create_datetime=timestamp)
        database.session.add(new_comment)
        Tickets.query.filter(Tickets.ticket_id == ticket_id).update(
            {Tickets.change_datetime: timestamp}
        )
        database.session.commit()
        return new_comment
