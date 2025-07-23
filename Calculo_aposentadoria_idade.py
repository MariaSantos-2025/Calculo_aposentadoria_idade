#Cálculo de tempo de contribuição para aposentadoria por idade

#Módulos padrão
from datetime import datetime, timedelta  #Manipulação de  datas e cálculo de intervalo em dias

#Bibliotecas externas
from dateutil.relativedelta import relativedelta   # Cálculo de diferenças entre datas
from fpdf import FPDF   #Criação de documentos PDF de forma programada

# Inputs iniciais
nome = input("Digite o Nome: ")
sexo= input("Sexo (MYF): ").strip().upper()
data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
data_atual = input("Data atual (DD/MM/AAAA): ")

# Conversão para datetime
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.strptime(data_atual, "%d/%m/%Y")

# Cálculo da idade
idade = relativedelta(data_atual, data_nascimento)

# Tempo de contribuição
historico_empresas = []
dias_totais = 0

while True:
    empresa = input("\nNome da empresa: ")
    entrada = input("Data de entrada (DD/MM/AAAA): ")
    saida = input("Data de saida (DD/MM/AAAA): ")

    data_entrada = datetime.strptime(entrada, "%d/%m/%Y")
    data_saida = datetime.strptime(saida, "%d/%m/%Y")

    tempo_trabalhado = data_saida - data_entrada
    dias = tempo_trabalhado.days
    anos = dias // 365
    meses = (dias % 365) // 30

    dias_totais += dias

    print(f"Tempo de trabalho na {empresa}: {anos} anos e {meses} meses")
    historico_empresas.append({
        "Empresa": empresa,
        "Entrada": entrada,
        "Saída": saida,
        "Tempo": f"{anos} anos e {meses} meses"
    })

    escolha = input("Deseja inserir outra empresa? (S/N): ").strip().upper()
    if escolha != "S":
       break

#Cálculo do tempo total de contribuição
inicio_contribuicao = datetime(1980, 1, 1) # Data ficticia
tempo_contribuicao = inicio_contribuicao + timedelta(days=dias_totais)
total_contrib = relativedelta(tempo_contribuicao, inicio_contribuicao)

print("\nTempo total de contribuição:")
print(f"{total_contrib.years} anos, {total_contrib.months} meses e {total_contrib.days} dias")
print("Mínimo exigido: 15 anos")

if total_contrib.years >= 15:
   print(f"{nome} já atingiu os 15 anos mínimos de contribuição. Verifique a idade mínima.")
else:
    falta = relativedelta(inicio_contribuicao + timedelta(days=15*365), tempo_contribuicao)
    print(f"Faltam {falta.years} anos, {falta.months} meses e {falta.days} dias para completar os 15 anos.")

# Verificação de idade
print( f"A idade mínima para homens: 65  anos ")
print( f"A idade mínima para mulheres: 62  anos ")
print(f"Idade de {nome}: {idade.years} anos, {idade.months} meses e {idade.days} dias")
idade_minima = 65 if sexo == "M" else 62

if idade.years >= idade_minima:
  print("Idade mínima para aposentadoria por idade já atingida.")
else:
  data_aposentadoria = data_nascimento.replace(year=data_nascimento.year + idade_minima)
  tempo_falta = relativedelta(data_aposentadoria, data_atual)
  print(f"Faltam {tempo_falta.years } anos, {tempo_falta.months} meses e {tempo_falta.days} dias para atingir idade minima.")

# Verificação final para aposentadoria
if idade.years >= idade_minima and total_contrib.years >= 15:
    print(" Poderá solicitar aposentadoria por idade.")
    status = "Pode solicitar aposentadoria por idade."
else:
    print("Ainda não atingiu os critérios para aposentadoria por idade.")
    status = "Ainda não atingiu os critérios para aposentadoria por idade."

# Gera relatório PDF atualizado com requisitos mínimos
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Relatorio de Aposentadoria por Idade", ln=True, align="C")
pdf.ln(10)

# Inserindo dados no PDF
pdf.cell(200, 10, txt=f"Nome: {nome}", ln=True)
pdf.cell(200, 10, txt=f"Sexo: {sexo}", ln=True)
pdf.cell(200, 10, txt=f"Data de Nascimento: {data_nascimento.strftime('%d/%m/%Y')}", ln=True)
pdf.cell(200, 10, txt=f"Data Atual: {data_atual.strftime("%d/%m/%Y")}", ln=True)
pdf.cell(200, 10, txt=f"Idade: {idade.years} anos, {idade.months} meses, {idade.days} dias", ln=True)
pdf.cell(200, 10, txt=f"Tempo de Contribuição: {total_contrib.years} , anos {total_contrib.months} meses, {total_contrib.days} dias", ln=True)

pdf.ln(10)
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt="Requisitos para Aposentadoria por Idade:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="-Tempo mínimo de contribuição: 15 anos", ln=True)

pdf.cell(200, 10, txt="-Idade mínima para homens: 65 anos", ln=True)
pdf.cell(200, 10, txt="-Idade mínima para mulheres: 62 anos", ln=True)
pdf.ln(10)
pdf.cell(200, 10, txt="Histórico de Trabalho:", ln=True)
for empresa in historico_empresas:
     pdf.cell(200, 10, txt=f"- {empresa ['Empresa']}: {empresa ['Tempo']} ({empresa['Entrada']} até {empresa['Saída']})", ln=True)
pdf.ln(10)
pdf.cell(200, 10, txt=f"Status: {status}", ln=True)

#Faltam para completar os 15 anos de contribuição
if total_contrib.years < 15:
    pdf.cell(200, 10, txt=f"Faltam {falta.years} anos, {falta.months} meses, {falta.days} dias para completar os 15 anos de contribuição.", ln=True)
#Faltam para atingir idade minima
if idade.years < idade_minima:
    pdf.cell(200, 10, txt=f"Faltam {tempo_falta.years} anos, {tempo_falta.months} meses {tempo_falta.days} dias para atingir a \nidade minima de aposentadoria.", ln=True)
pdf.output("relatorio_aposentadoria_idade.pdf")
