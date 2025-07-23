#  Projeto : Calculo_aposentadoria_idade
Este projeto destina-se à realizar cálculo de tempo de contribuição e da idade do trabalhador.

## Cálculo de Tempo de Contribuição para Aposentadoria por Idade

Este projeto Python realiza o cálculo do tempo de contribuição e idade do usuário. Para
verificação se os requisitos mínimos de aposentadoria por idade foram atendidos, será gerado automaticamente 
um relatório em PDF.


## Funcionalidades
• Coleta de informações do usuário: nome, sexo, data de nascimento , data atual , empresas e períodos trabalhados.

• Cálculo total de tempo de contribuição.

• Verificação dos requisitos da aposentadoria por idade (idade mínima e tempo mínimo
de contribuição).

• Gera um relatório em PDF , de acordo com  os dados informados, informando o tempo de contribuição e idade do trabalhador. Informa se já poderá requer a aposentadoria ou o tempo faltante para os requisitos mínimos (tempos em anos, meses e dias).


## Requisitos
Certifique-se de ter o Python instalado (recomenda-se Python 3.7+) e os seguintes  **pacotes**:

### Módulos padrão

from datetime import datetime, timedelta   -    # Manipula datas e cálculo de intervalo em dias


### Bibliotecas externas

from dateutil.relativedelta import relativedelta   -   # Cálculo de diferenças entre datas

from fpdf import FPDF    -   # Criação de documentos PDF de forma programada


**Pacotes necessários**:

pip install python-dateutil

pip install datetime

pip install fpdf


## Ехесução 

1. Execute o script:
python aposentadoria.py

2. Responda às perguntas no terminal, como:  nome, data de nascimento, empresas
trabalhadas, etc.

3. Após completar as informações, um PDF chamado relatorio_aposentadoria_idade.pdf será gerado com o resumo completo.

## Estrutura do Relatório PDF conterá:

• Dados pessoais

• Histórico de trabalho

• Tempo total de contribuição

• Verificação de requisitos mínimos (idade e tempo). Caso não tenha cumprido os requisitos mínimos , então informará quanto tempo falta para cumprir o tempo mínimo de contribuição e idade mínima.


## Requisitos Legais Considerados  até 12/11/2019:

**Sexo Feminino**:Tempo mínimo de contribuição : 15 anos e ter 62 anos de idade (a partir de 2023	)

**Sexo Masculino**:Tempo mínimo de contribuição : 15 anos  e ter 65 anos de idade 

## Personalização
Você pode ajustar:

• A data fictícia de início da contribuição poderá ser alterada.


## ! Observações
Na Reforma da Previdência (a partir de 13/11/2019), foram alterados alguns requisitos legais,  que não estão inclusos nessa simulação, portanto,  este script **não substitui** uma consulta oficial ao INSS ou  à um profissional habilitado.

## Autora

Este projeto foi desenvolvido por **Maria** , com o objetivo de auxiliar no cálculo do tempo de contribuição para aposentadoria por idade no Brasil.

Sinta-se à vontade para explorar, utilizar e adaptar o código conforme sua necessidade.

---

## Contribuições

Contribuições são **muito bem-vindas**! Caso queira colaborar com melhorias, correções ou novas funcionalidades, basta seguir os passos:

1. Faça um **fork** do repositório.
2. Crie uma **branch** com sua melhoria:
   ```bash
   git checkout -b minha-melhoria
