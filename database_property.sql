CREATE TABLE tickets (
  ticket_id serial primary key,
  create_datetime timestamp NOT NULL,
  change_datetime timestamp,
  title text NOT NULL,
  body text NOT NULL,
  email varchar(50) NOT NULL,
  status varchar(20) NOT NULL
);

CREATE TABLE comments (
  comment_id serial primary key,
  ticket_id integer references tickets(ticket_id),
  create_datetime timestamp NOT NULL,
  email varchar(50) NOT NULL,
  comment text
);