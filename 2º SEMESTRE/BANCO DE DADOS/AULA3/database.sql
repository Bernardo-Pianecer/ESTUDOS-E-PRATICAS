-- -- ROOT

CREATE DATABASE IF NOT EXISTS escola3;
use escola3;

CREATE TABLE IF NOT EXISTS funcionario (
    id_func INT PRIMARY KEY AUTO_INCREMENT,
    nome_func VARCHAR(500) NOT NULL,
    telefone_func VARCHAR(20) NOT NULL,
    email_func VARCHAR(100) NOT NULL,
    cargo_func INT NOT NULL DEFAULT 0,
    status BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (telefone_func)
);

CREATE TABLE IF NOT EXISTS aluno (
    id_aluno INT PRIMARY KEY AUTO_INCREMENT,
    nome_aluno VARCHAR(500) NOT NULL,
    telefone_aluno VARCHAR(20) NOT NULL,
    nota_aluno INT DEFAULT 0,
    status_aluno BOOLEAN NOT NULL DEFAULT TRUE,
    email_aluno VARCHAR(20) NOT NULL,
    id_func INT,
    UNIQUE (telefone_aluno),
    FOREIGN KEY (id_func)
        REFERENCES funcionario(id_func)
);

-- INSERT INTO funcionario(nome_func, telefone_func, email_func, cargo_func)
-- VALUES
-- ('Prof01','47999999999','Prof01@.com',1),
-- ('Prof02','47999999998','Prof02@.com',1),
-- ('Prof03','47999999997','Prof03@.com',1),
-- ('Prof04','47999999996','Prof04@.com',1),
-- ('Sec02','47999999995','Sec02@.com',2),
-- ('Ger01','47999999994','Ger01@.com',3);


-- UPDATE aluno WHERE status_aluno = 1
--     SET id_func = 'Prof01_id';
-- INSERT INTO aluno(nome_aluno, telefone_aluno, email_aluno, id_func)
-- VALUES
-- ('Alun01','47999999989','Alun01@.com',13),
-- ('Alun02','47999999988','Alun02@.com',13),
-- ('Alun03','47999999987','Alun03@.com',14),
-- ('Alun04','47999999986','Alun04@.com',14),
-- ('Alun05','47999999985','Alun05@.com',15),
-- ('Alun06','47999999984','Alun06@.com',15),
-- ('Alun07','47999999983','Alun07@.com',16),
-- ('Alun08','47999999982','Alun08@.com',16),
-- ('Alun09','47999999981','Alun09@.com',13),
-- ('Alun10','47999999980','Alun10@.com',14);

-- SELECT telefone_func, email_func FROM funcionario WHERE cargo_func = 1

-- SELECT nome_func FROM funcionario WHERE cargo_func = 2

-- SELECT email_aluno FROM aluno WHERE nome_aluno = 0

-- SELECT telefone_aluno FROM aluno WHERE id_func = 14

-- UPDATE aluno SET id_func = 15 WHERE nome_aluno = 'Alun07'

-- SELECT nome_aluno, telefone_aluno, email_aluno, id_func FROM aluno WHERE nome_aluno = 'Alun07'

-- UPDATE funcionario SET telefone_func = '4799999964' WHERE nome_func = 'Ger01'
-- SELECT nome_func, telefone_func, email_func, id_func FROM funcionario WHERE nome_func = 'Ger01'

-- DELETE FROM aluno WHERE nome_aluno = 'Alun04'
-- SELECT * from aluno

-- DELETE FROM funcionario WHERE id_func = 19
-- SELECT * from funcionario

UPDATE aluno SET telefone_aluno = '47999999999'

-- INSERT INTO funcionario(nome_func, telefone_func, email_func, cargo_func)
-- VALUES
-- ('Prof99','47899999999','Prof99@.com',99);
-- SELECT 
-- CREATE ROLE IF NOT EXISTS 'professores';
-- GRANT USAGE ON escola2.* TO 'professores';
-- GRANT SELECT (nome_aluno, nota_aluno) ON escola2.aluno TO 'professores'; 
-- GRANT UPDATE (nota_aluno) ON escola2.aluno TO 'professores';

-- CREATE ROLE IF NOT EXISTS 'secretarios';
-- GRANT USAGE ON escola2.* TO 'secretarios';
-- GRANT SELECT ON escola2.aluno TO 'secretarios';
-- GRANT SELECT ON escola2.funcionario TO 'secretarios';
-- GRANT UPDATE ON escola2.aluno TO 'secretarios';

-- CREATE ROLE IF NOT EXISTS 'gestores';
-- GRANT USAGE ON escola2.* TO 'gestores';
-- GRANT SELECT ON escola2.aluno TO 'gestores';
-- GRANT SELECT ON escola2.funcionario TO 'gestores';
-- GRANT UPDATE ON escola2.funcionario TO 'gestores';

-- CREATE ROLE IF NOT EXISTS 'alunos';
-- GRANT USAGE ON escola2.* TO 'alunos';
-- GRANT SELECT (nome_func, cargo_func) ON escola2.funcionario TO 'alunos';

-- CREATE USER IF NOT EXISTS 'prof'@'%' IDENTIFIED BY 'profprof';
-- GRANT 'professores' TO 'prof'@'%';
-- SET DEFAULT ROLE professores TO 'prof'@'%';

-- CREATE USER IF NOT EXISTS 'sec'@'%' IDENTIFIED BY 'secsec';
-- GRANT 'secretarios' TO 'sec'@'%';
-- SET DEFAULT ROLE secretarios TO 'sec'@'%';

-- CREATE USER IF NOT EXISTS 'ger'@'%' IDENTIFIED BY 'gerger';
-- GRANT 'gestores' TO 'ger'@'%';
-- SET DEFAULT ROLE gestores TO 'ger'@'%';

-- CREATE USER IF NOT EXISTS 'alu'@'%' IDENTIFIED BY 'alualu';
-- GRANT 'alunos' TO 'alu'@'%';
-- SET DEFAULT ROLE alunos TO 'alu'@'%';

-- INSERT INTO funcionario (nome_func, telefone_func) VALUES ('Prof01', '47999999999');
-- INSERT INTO funcionario (nome_func, telefone_func) VALUES ('Prof02', '47999999995');

-- SELECT * FROM funcionario;

-- INSERT INTO aluno (nome_aluno, telefone_aluno, id_func) VALUES ('Aluno01', '47999999997', 1);
-- INSERT INTO aluno (nome_aluno, telefone_aluno, id_func) VALUES ('Aluno02', '47999999998', 2);

-- SELECT * FROM aluno;

-- -- -- alu 

-- -- use escola;
-- -- SELECT nome_func FROM funcionario;

-- -- -- prof

-- -- use escola;
-- -- SELECT nome_aluno FROM aluno;

-- -- -- sec/ger 

-- -- use escola;
-- -- SELECT nome_func FROM funcionario;
-- -- SELECT nome_aluno FROM aluno;