-- CREATE OR REPLACE
CREATE OR REPLACE VIEW v_observabilidade_bitbot AS
SELECT 
    u.username AS usuario, 
    h.pergunta_usuario AS pergunta, 
    h.ip_origem AS ip, 
    EXTRACT(HOUR FROM h.data_interacao) AS hora_do_dia, 
    TO_CHAR(h.data_interacao, 'DD/MM/YYYY HH24:MI') AS data_formatada, 
    LENGTH(h.pergunta_usuario) AS tamanho_pergunta 
FROM 
    quiz_historicobot h 
JOIN 
    sensitive.auth_user u ON h.usuario_id = u.id 
ORDER BY 
    h.data_interacao DESC;