import math

def calcular_area_circulo(raio):
  """Calcula a área de um círculo dado o seu raio.

  Args:
    raio: O raio do círculo.

  Returns:
    A área do círculo.
  """
  return math.pi * (raio ** 2)

# Exemplo de uso
raio = 5
area = calcular_area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area}")