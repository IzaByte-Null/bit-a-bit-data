--  Redes e Organização de Schemas
CREATE SCHEMA IF NOT EXISTS "sensitive";
CREATE SCHEMA IF NOT EXISTS "neon_auth";
CREATE SCHEMA IF NOT EXISTS "pgrst";

--  Tabelas de Identidade (Sensitive)
CREATE TABLE IF NOT EXISTS "sensitive"."auth_user" (
    "id" SERIAL PRIMARY KEY,
    "password" VARCHAR(128) NOT NULL,
    "last_login" TIMESTAMP WITH TIME ZONE,
    "is_superuser" BOOLEAN NOT NULL DEFAULT FALSE,
    "username" VARCHAR(150) NOT NULL UNIQUE,
    "first_name" VARCHAR(150),
    "last_name" VARCHAR(150),
    "email" VARCHAR(254) NOT NULL,
    "is_staff" BOOLEAN NOT NULL DEFAULT FALSE,
    "is_active" BOOLEAN NOT NULL DEFAULT TRUE,
    "date_joined" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

--  Tabelas de Aplicação (Public)
CREATE TABLE IF NOT EXISTS "quiz_pergunta" (
    "id" BIGSERIAL PRIMARY KEY,
    "texto" TEXT NOT NULL,
    "dificuldade" VARCHAR(1) NOT NULL,
    "categoria" VARCHAR(100) NOT NULL,
    "tempo_limite" INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "quiz_pontuacao" (
    "id" BIGSERIAL PRIMARY KEY,
    "pontos_totais" INTEGER NOT NULL,
    "data_conclusao" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    "dificuldade" VARCHAR(1) NOT NULL,
    "usuario_id" INTEGER NOT NULL REFERENCES "sensitive"."auth_user"("id")
);

-- CONSTRAINT DE UNICIDADE:
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
    "id" BIGSERIAL PRIMARY KEY,
    "user_id" INTEGER NOT NULL REFERENCES "sensitive"."auth_user"("id"),
    "group_id" INTEGER NOT NULL,
    CONSTRAINT "auth_user_groups_user_id_group_id_uniq" UNIQUE("user_id", "group_id")
);

--  Observabilidade e Logs
CREATE TABLE IF NOT EXISTS "log_erros_api" (
    "id" SERIAL PRIMARY KEY,
    "endpoint" VARCHAR(255),
    "status_code" INTEGER,
    "mensagem_erro" TEXT,
    "data_erro" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    "usuario_id" INTEGER REFERENCES "sensitive"."auth_user"("id")
);

CREATE TABLE IF NOT EXISTS "quiz_historicobot" (
    "id" BIGSERIAL PRIMARY KEY,
    "pergunta_usuario" TEXT NOT NULL,
    "resposta_bot" TEXT NOT NULL,
    "data_interacao" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    "ip_origem" INET,
    "usuario_id" INTEGER NOT NULL REFERENCES "sensitive"."auth_user"("id")
);