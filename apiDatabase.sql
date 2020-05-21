create database dcleanapi;
use dcleanapi;

create table connections(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `token` INT(12) NOT NULL, -- Chave estrangeira de tokens.id
    `active` BOOLEAN DEFAULT TRUE
)ENGINE = InnoDB;

create table tokens(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `user` INT(12) NOT NULL, -- Usuário que utiliza
    `token` TEXT NOT NULL, -- Token de autenticação
    `datetime` TIMESTAMP DEFAULT NOW() -- Data e hora de gerado
)ENGINE = InnoDB;

ALTER TABLE connections
ADD CONSTRAINT fk_tokens FOREIGN KEY (token) REFERENCES tokens(id);
