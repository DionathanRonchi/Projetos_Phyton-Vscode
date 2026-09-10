create database barbearia;
use barbearia;

create table agendamentos( 
id int auto_increment primary key,
cliente varchar(100) not null, 
telefone varchar(20),
servico varchar(100),
preco decimal(10,2),
barbeiro varchar(50),
data date not null,
horario varchar(5),
status varchar(20) default 'Agendado',
check (status in ('Agendado', 'Concluído', 'Cancelado'))
);

insert into agendamentos values
(1, 'Robson', 4232458963, 'Corte cabelo simples', 50, 'Carlos', '2026-08-09', '15:30', 'Agendado'),
(2, 'Pedro', 2458642594, 'Barba e cabelo', 60, 'Gabriel', '2025-04-09', '10:50', 'Concluido'),
(3, 'Felipe', 1254896359, 'Depilação(nariz e orelha)', 30, 'Bruno', '2026-02-09', '18:45', 'Agendado'),
(4, 'Joao', 1478523659, 'Cabelo, Barba e Sombrancelha', 60, 'Lucas', '2025-10-09', '20:00', 'Agendado'),
(5, 'Samuel', 1578542369, 'Corte cabelo simples', 50, 'Matheus', '2026-05-09', '17:30', 'Concluido'),
(6, 'Abnner', 1245896535, 'Combo(cabelo, barba, sombrancelha e depilação)', 80, 'Rafel', '2025-01-09', '13:40', 'Cancelado'),
(7, 'Dionathan', 1457853596, 'Barba', 40, 'Gustavo', '2026-11-09', '16:30', 'Agendado'),
(8, 'Enzo', 1547852359, 'Corte com desenho', 55, 'Miguel', '2025-12-09', '21:00', 'Cancelado');

select*from agendamentos;
