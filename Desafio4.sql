create database contatos;
use contatos;

create table contatos
(
	id int primary key auto_increment,
	email varchar(45) not null,
    assunto varchar(45) not null,
    descricao varchar(45) not null
    
);


describe contatos;

insert into contatos (email, assunto, descricao) values
('fatec@fatec.sp.gov.br','fatec','Flask'),
('isaque@fatec.sp.gov.br','fatec','Banco de Dados');


select * from contatos;


