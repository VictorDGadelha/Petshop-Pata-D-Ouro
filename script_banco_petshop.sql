--  Tabela de Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(150) NOT NULL,
    cpf_cliente VARCHAR(20) UNIQUE NOT NULL, 
    tel_cliente VARCHAR(20),               
    email_cliente VARCHAR(100),            
    endereco_cliente TEXT
);

--  Tabela de Pets 
CREATE TABLE IF NOT EXISTS pets (
    id_pet SERIAL PRIMARY KEY,
    nome_pet VARCHAR(100) NOT NULL,
    especie_pet VARCHAR(50) NOT NULL,
    cor_pet VARCHAR(50),                   
    peso_pet DECIMAL(5, 2),                  
    dono_id INTEGER NOT NULL,               
    CONSTRAINT fk_cliente FOREIGN KEY (dono_id) REFERENCES clientes(id_cliente) ON DELETE CASCADE
);

--  Tabela de Serviços
CREATE TABLE IF NOT EXISTS servicos (
    id_servico SERIAL PRIMARY KEY,
    tipo_servico VARCHAR(100) NOT NULL,     
    valor_servico DECIMAL(10, 2) NOT NULL,   
    data_hora_agenda TIMESTAMP               
);

-- 4. Tabela de Produtos
CREATE TABLE IF NOT EXISTS produtos (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    categoria_produto VARCHAR(50),           
    valor_produto DECIMAL(10, 2) NOT NULL    