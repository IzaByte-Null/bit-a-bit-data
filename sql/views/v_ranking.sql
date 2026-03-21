CREATE OR REPLACE VIEW v_ranking_global AS
SELECT 
    u.id AS user_id, 
    u.username, 
    p.foto_perfil, 
    SUM(pt.pontos_totais) AS score_acumulado, 
    COUNT(pt.id) AS partidas_jogadas, 
    MAX(h.data_interacao) AS ultima_atividade_bot 
FROM 
    sensitive.auth_user u 
LEFT JOIN 
    sensitive.usuarios_perfil p ON u.id = p.user_id 
LEFT JOIN 
    quiz_pontuacao pt ON u.id = pt.usuario_id 
LEFT JOIN 
    quiz_historicobot h ON u.id = h.usuario_id 
GROUP BY 
    u.id, u.username, p.foto_perfil 
ORDER BY 
    score_acumulado DESC;