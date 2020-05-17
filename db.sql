CREATE DATABASE dclean;
use dclean;


/*
Criação das tabelas de usuários
*/

create table usuarios
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(50) UNIQUE NOT NULL, 
    `first_name` VARCHAR(50) NOT NULL,
    `second_name` VARCHAR(100) NOT NULL,
    `photo_path` VARCHAR(100),
    `password` VARCHAR(1000) NOT NULL,
    `salt` VARCHAR(500) NOT NULL,
    `type` INT(12) NOT NULL -- Chave estrangeira de tipos_usuarios ID
)ENGINE = InnoDB;
--
create table tipos_usuarios -- Motorista, Cliente, ADM
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `descricao` TEXT
)ENGINE = InnoDB;


/*
Criação das tabelas de aplicação
*/

create table carros
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `placa` VARCHAR(12) NOT NULL,
    `caminho_qr` VARCHAR(100) NOT NULL,
    `usuario` INT(12) NOT NULL -- Chave estrangeira de usuarios ID 
)ENGINE = InnoDB;
--
create table carros_satisfacoes
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL, -- Chave estrangeira de carros ID
    `satisfacao` INT NOT NULL,
    `comentario` TEXT
)ENGINE = InnoDB;
--
create table limpezas
(   
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL, -- Chave estrangeira de carros ID
    `data` DATE NOT NULL
)ENGINE = InnoDB;
--
create table notificacoes 
/* 
Usado para enviar notificações. O app verifica aqui se possui alguma notificação que ainda não foi enviada com o carro em questão.

Ao enviar notificação, deve retornar ao backend esta informação, para que seja alterado o dado da coluna enviada para 1.

*/
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL, -- Chave estrangeira de carros ID
    `tipo` INT(12) NOT NULL, -- Chave estrangeira de notificacoes_tipos ID
    `usuario` INT(12) NOT NULL, -- Chave estrangeira de usuarios ID
    `corpo` TEXT,
    `enviada` BOOLEAN DEFAULT FALSE
)ENGINE = InnoDB;
--
create table notificacoes_tipos
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `descricao` TEXT
)ENGINE = InnoDB;
--
create table notificacoes_recusadas
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `notificacao` INT(12) NOT NULL, -- Chave estrangeira de notificacoes ID
    `tipo` INT(12) NOT NULL, -- Chave estrangeira de notificacoes_tipos ID
    `carro` INT(12) NOT NULL, -- Chave estrangeira de carros ID
    `data` DATE NOT NULL
)ENGINE = InnoDB;
--
ALTER TABLE carros_satisfacoes
ADD CONSTRAINT fk_carro FOREIGN KEY (carro) REFERENCES carros(id);
--
ALTER TABLE limpezas 
ADD CONSTRAINT fk_carro2 FOREIGN KEY (carro) REFERENCES carros(id);
--
ALTER TABLE notificacoes_recusadas 
ADD CONSTRAINT fk_carro3 FOREIGN KEY (carro) REFERENCES carros(id);
--
ALTER TABLE usuarios
ADD CONSTRAINT fk_tipos_usuarios FOREIGN KEY (type) REFERENCES tipos_usuarios(id);
--
ALTER TABLE carros
ADD CONSTRAINT fk_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id);
--
ALTER TABLE notificacoes
ADD CONSTRAINT fk_carro4 FOREIGN KEY (carro) REFERENCES carros(id),
ADD CONSTRAINT fk_notificacoes_tipos FOREIGN KEY (tipo) REFERENCES notificacoes_tipos(id),
ADD CONSTRAINT fk_usuarios2 FOREIGN KEY (usuario) REFERENCES usuarios(id);
--
ALTER TABLE notificacoes_recusadas
ADD CONSTRAINT fk_notificacoes FOREIGN KEY (notificacao) REFERENCES notificacoes(id),
ADD CONSTRAINT fk_notificacoes_tipos2 FOREIGN KEY (tipo) REFERENCES notificacoes_tipos(id),
ADD CONSTRAINT fk_carro5 FOREIGN KEY (carro) REFERENCES carros(id);