SELECT T.CODIGO_TAREFA,
       T.TITULO,
       T.DESCRICAO,
       T.DATA_CRIACAO,
       T.DATA_CONCLUSAO,
       CASE 
           WHEN T.STATUS = 0 THEN 'Pendente'
           WHEN T.STATUS = 1 THEN 'Concluída'
           ELSE 'Outro'
       END AS STATUS,
       T.CPF
       FROM TAREFAS T
       ORDER BY T.DATA_CRIACAO;