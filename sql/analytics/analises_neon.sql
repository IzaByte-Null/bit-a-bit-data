-- ANALISE 01: 
--              horário de maior atividade do Bot 
SELECT 
    hora_do_dia, 
    COUNT(*) AS total_interacoes 
FROM 
    v_observabilidade_bitbot 
GROUP BY 
    hora_do_dia 
ORDER BY 
    total_interacoes DESC;

-- ANALISE 02: 
--             requisições da API do Gemini 
SELECT 
    endpoint, 
    status_code, 
    mensagem_erro, 
    data_erro 
FROM 
    log_erros_api 
WHERE 
    status_code != 200
ORDER BY 
    data_erro DESC;