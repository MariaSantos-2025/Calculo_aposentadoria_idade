# Calculo_aposentadoria_idade
Este projeto destina-se à realizar cálculo de tempo de contribuição e da idade do trabalhador.
Cálculo de Tempo de Contribuição para Aposentadoria por Idade. 

Este projeto tem como objetivo auxiliar trabalhadores a verificarem se já atendem aos requisitos mínimos para solicitar aposentadoria por idade, conforme as regras do INSS. A aplicação coleta dados pessoais e históricos de trabalho, calcula o tempo total de contribuição e a idade atual, e gera um relatório em PDF com os resultados. Observação : Este projeto não substitui a análise de  um Profissional da área ou da autarquia responsável (INSS).

---
## Funcionalidades

- Cálculo da idade atual com base na data de nascimento
- Registro de múltiplos vínculos empregatícios
- Cálculo do tempo total de contribuição
- Verificação dos requisitos mínimos:
  - Tempo de contribuição: 15 anos
  - Idade mínima: 65 anos (homens) / 62 anos (mulheres)
- Geração de relatório em PDF com todos os dados e status de elegibilidade

---

## Bibliotecas Utilizadas

- `datetime` e `timedelta` (módulos padrão) — manipulação de datas
- `dateutil.relativedelta` — cálculo preciso de diferenças entre datas
- `fpdf` — geração de documentos PDF

---

## Como Usar

Instale as dependências:


pip install python-dateutil fpdf

## Licença

Este projeto está sob licença MIT. - Sinta-se livre para usá-lo  e modificá-lo. 

