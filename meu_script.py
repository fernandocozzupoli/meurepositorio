import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("dados.xlsx")

# Exibir as primeiras linhas para conferência
print(df.head())

# Agrupar os dados por categoria
resumo = df.groupby("Categoria")["Valor"].sum()

# Calcular o total geral e a média
total_geral = df["Valor"].sum()
media_valores = df["Valor"].mean()

# Exibir os resultados
print(f"Total geral: R$ {total_geral:.2f}")
print(f"Média dos valores: R$ {media_valores:.2f}")
print(resumo)
import matplotlib.pyplot as plt

# Criar um gráfico de barras
plt.figure(figsize=(8, 4))
resumo.plot(kind="bar", color="skyblue")
plt.title("Total por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor (R$)")
plt.xticks(rotation=45)
plt.savefig("grafico.png")  # Salvar como imagem
plt.show()
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Criar o PDF
pdf_name = "relatorio.pdf"
c = canvas.Canvas(pdf_name, pagesize=letter)

# Adicionar título
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 750, "Relatório Financeiro")

# Adicionar os dados processados
c.setFont("Helvetica", 12)
c.drawString(100, 720, f"Total geral: R$ {total_geral:.2f}")
c.drawString(100, 700, f"Média dos valores: R$ {media_valores:.2f}")

# Adicionar o gráfico ao PDF
c.drawImage("grafico.png", 100, 500, width=400, height=200)

# Salvar o PDF
c.save()
print("Relatório gerado com sucesso!")
