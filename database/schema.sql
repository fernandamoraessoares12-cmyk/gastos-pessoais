create table gastos (
    id bigint generated always as identity primary key,
    descricao text not null,
    valor numeric not null,
    categoria text,
    created_at timestamp default now()
);
