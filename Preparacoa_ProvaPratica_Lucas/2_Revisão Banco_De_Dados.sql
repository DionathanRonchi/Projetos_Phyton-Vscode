create database empresa;
use empresa;

create table clientes(
	id int auto_increment primary key,
	nome varchar(100),
	email varchar(100),
	telefone varchar(20)
);

# INSERIR 4 CLIENTES
insert into clientes values
(1, 'Robson', 'robson22@gmail.com', 743747382),
(2, 'Cleide', 'cleide13@yahoo.com', 575476786),
(3, 'Januario', 'januario38@gmail.com', 36346757),
(4, 'Francelino', 'francelino41yahoo.com', 9896748);

#LISTAR TODA A TABELA
select*from clientes;

#LISTAR TODOS ORDENADOS POR NOME
select*from clientes order by nome;

#BUSCAR CLIENTES CUJO EMAIL CONTENHA "GMAIL"
select*from clientes
where email like '%gmail%';

#ATUALIZAR TELEFONE DE UM CLINETE PELO ID
update clientes
set telefone = '47999999999'
where id = 1;

#EXCLUIR UM CLIENTE PELO ID
delete from clientes
where id = 1;



