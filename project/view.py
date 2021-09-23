from app import app, database
from tables import tickets, comments
from flask import jsonify


url = '/tickets/'


@app.route(f'{url}/ticket', methods=['POST'])
def create_ticket():
    pass


@app.route(f'{url}/ticket/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    print(tickets.query.all())
    return jsonify({"ticket": ticket_id}), 200


@app.route(f'{url}/ticket/<int:ticket_id>', methods=['PUT'])
def change_ticket_status(ticket_id):
    pass


@app.route(f'{url}/comment/<int:ticket_id>', methods=['POST'])
def add_ticket_comment(ticket_id):
    pass


@app.route('/')
def index():
    return 'Hello!'
