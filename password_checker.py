
#---------------------------
#    Funções Auxiliares
#---------------------------

def colorir (texto: str, cor: str) -> str:
  """Aplica cor ANSI ao texto."""
  return f"{CORES.get(cor, '')}{{texto}{CORES"['reset']}"

def banner() -> None:
   """Exibe o banner da Feramenta."""
   print(colorir("""
======================================
     Password Strangth Checker
         Security tools
======================================
""", "ciano"))

def barra_forca(score: int, maximo: int = 7) -> str:
   """Gera barra visual de força de senha."""
   proporcao = score / maximo
   blocos_cheios = int(proporcao *20)
   blocos_vazios = 20 - blocos_cheios

   if proporcao < 0.4:
      cor = "vermelho"
   elif proporcao < 0.7:
      cor = "amarelo"
   else:
      cor = "verde"

   barra = "█" * blocos_cheios + "░" * blocos_vazios
   return colorir(f"[{barra}]", cor)
