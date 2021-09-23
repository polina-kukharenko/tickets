from app import app
from functions import create_ticket, change_status, show_ticket, add_comment
from flask import jsonify, request

url = '/tickets/'


@app.route(f'{url}/ticket', methods=['POST'])
def r_create_ticket():
    if not {'title', 'body', 'email'} == request.form.keys():
        return jsonify({'Error': 'Fields expected: title, body, email'}), 400
    else:
        if request.form['title'] and request.form['body'] and request.form['email']:
            ticket_id = create_ticket(title=request.form['title'], body=request.form['body'], email=request.form['email'])
            return jsonify(request.form | {'ticket_id': ticket_id}), 201
        else:
            return jsonify({'Error': 'Fields expected: title, body, email'}), 400


@app.route(f'{url}/ticket/<int:ticket_id>', methods=['GET'])
def r_get_ticket(ticket_id):
    ticket = show_ticket(ticket_id=ticket_id)
    if not ticket:
        return jsonify({'Error': f'Ticket #{ticket_id} is not found'}), 404
    return jsonify(ticket.as_dict()), 200


@app.route(f'{url}/ticket/<int:ticket_id>', methods=['PUT'])
def r_change_ticket_status(ticket_id):
    if not {'status'} == request.form.keys():
        return jsonify({'Error': 'Fields expected: status'}), 400
    else:
        try:
            change_status(ticket_id=ticket_id, status=request.form['status'])
        except Exception as Err:
            return jsonify({'Error': str(Err)}), 400
        else:
            return jsonify({'ticket_id': ticket_id, 'status': request.form['status']}), 200


@app.route(f'{url}/comment/<int:ticket_id>', methods=['POST'])
def r_add_ticket_comment(ticket_id):
    if not {'comment', 'email'} == request.form.keys():
        return jsonify({'Error': 'Fields expected: comment, email'}), 400
    else:
        if request.form['comment'] and request.form['email']:
            try:
                comment = add_comment(
                    ticket_id=ticket_id, comment_text=request.form['comment'], email=request.form['email']
                )
            except Exception as Err:
                return jsonify({'Error': str(Err)}), 400
            else:
                return jsonify(comment.as_dict() | {'ticket_id': ticket_id}), 201
