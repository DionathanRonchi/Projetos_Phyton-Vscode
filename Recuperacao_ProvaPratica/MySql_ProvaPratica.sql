-- Criação do banco
create database petshop;

-- selecionar o banco
use petshop;

-- criar a tabela do cardápio
create table pets (
id int auto_increment primary key,
nome varchar(100) not null,
especie varchar(50),
dono varchar(100)
);

-- A) inserir 4 animais no petshop
insert into pets (nome, especie, dono) values
('Bob', 'Cachorro', 'João'),
('Docinho', 'Gato', 'Robson'),
('Laguna', 'Cachorro', 'Pedro'),
('Sturt', 'hamester', 'Enzo'),
('Serpente', 'Cobra', 'Felipe');

-- B) Listar os pets por nome
select * from pets
order by nome asc;

-- C) listar os pets da especie cachorro
select * from pets
where especie = 'Cachorro';

-- D) atualizar o nome de um  dono de pet pelo id
update pets
set dono = 'juquinha'
where id = 1;
