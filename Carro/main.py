def calcular_preco_final(valor_carro, desconto=20):
  """
  Calcula o preço final para compra à vista, aplicando um desconto.

  Parâmetros:
      valor_carro (float): O valor inicial do carro.
      desconto (float): O percentual de desconto para compra à vista.

  Retorna:
      float: O preço final para compra à vista.
  """
  desconto_percentual = desconto / 100
  preco_final = valor_carro * (1 - desconto_percentual)
  return preco_final

def calcular_preco_parcelado(valor_carro, percentual_acrescimo):
  """
  Calcula o preço final para compra parcelada, aplicando o percentual de acréscimo.

  Parâmetros:
      valor_carro (float): O valor inicial do carro.
      percentual_acrescimo (float): O percentual de acréscimo para a quantidade de parcelas.

  Retorna:
      float: O preço final para compra parcelada.
  """
  acrescimo_percentual = percentual_acrescimo / 100
  preco_final = valor_carro * (1 + acrescimo_percentual)
  return preco_final

def main():
  # Solicita ao usuário o valor do carro
  valor_carro = float(input("Informe o valor do carro: R$ "))

  # Cria um dicionário com os percentuais de acréscimo para cada quantidade de parcelas
  percentuais_acrescimo = {
      6: 3,
      12: 6,
      18: 9,
      24: 12,
      30: 15,
      36: 18,
      42: 21,
      48: 24,
      54: 27,
      60: 30
  }

  # Calcula o preço final para compra à vista (desconto de 20%)
  desconto_avista = 20
  preco_final_avista = calcular_preco_final(valor_carro, desconto_avista)

  print(f"Preço final para compra à vista: R$ {preco_final_avista:.2f}")

  print("\nQuantidade de parcelas | Preço final parcelado | Valor de cada parcela")
  print("-" * 54)

  # Itera sobre as quantidades de parcelas e percentuais de acréscimo
  for parcelas, percentual_acrescimo in percentuais_acrescimo.items():
      # Calcula o preço final para a quantidade de parcelas
      preco_final_parcelado = calcular_preco_parcelado(valor_carro, percentual_acrescimo)

      # Calcula o valor de cada parcela
      valor_parcela = preco_final_parcelado / parcelas

      # Exibe os resultados
      print(f"{parcelas:>20} | R$ {preco_final_parcelado:>15.2f} | R$ {valor_parcela:>16.2f}")

# Executa o programa
main()