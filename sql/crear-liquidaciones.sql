create table if not exists liquidaciones (
    id serial primary key,
    salario_hora decimal not null,
    dias_trabajados int not null,
    vacaciones_pendientes int not null,
    aplica_indemnizacion boolean not null,
    valor_indemnizacion decimal not null,
    total decimal not null
);
