-- DB = /flashcard
-- Creating the tables
create table person(
    id              serial primary key,
    username        text not null unique constraint blank_uname check (length(username) > 0),
    email           text not null unique constraint valid_email check (email ~ '\A\S+@\S+\.\S+\Z'),
    password_hash   integer not null
);

create table deck(
    id              serial primary key,
    name            text not null unique constraint blank_name check (length(name) > 0),
    num_cards_due   integer,
    person_id       integer,
);

create table card(
    id              serial primary key,
    front           text not null constraint blank_front check (length(front) > 0),
    back            text not null constraint blank_back check (length(back) > 0),
    created_date    timestamp default current_timestamp,
    due_date        timestamp default current_timestamp,
    due_category    integer default 1,
    deck_id         integer,
    person_id       integer
);

-- Setting the foreign keys
alter table deck
    add constraint user_to_deck_fk foreign key (person_id) references person (id);

alter table card
    add constraint user_to_card_fk foreign key (person_id) references person (id),
    add constraint deck_to_card_fk foreign key (deck_id) references deck (id);