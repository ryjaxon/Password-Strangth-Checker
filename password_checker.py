
#-------------------------
#    Verificar Senha
#-------------------------

def verificar_senha(senha: str) -> dict:
   """Análisa a força de uma senha com base em 7 criterios."""
   score = 0
   feedbacks = []
   criterios = {}

   if len(senha) >= 8:
      score += 1
      criterios["comprimento_minimo"] = True
   else: 
      criterios["comprimento_minimo"] = False
      feedbacks.append("❌senha muito curta. Use pelo menos 8 caracteres.")

   if len(senha) >= 12:
      score += 1
      criterios["comprimento_ideal"] = True
   else:
      criterios["comprimento_ideal"] = False
      feedbacks.append("⚠️ ideal ter 12 ou mais caracteres.")

   if re.search(r"[a-z]", senha):
      score += 1
      criterios["minusculas"] = True
   else:
      criterios["minusculas"] = False
      feedbacks.append("❌adicione pelo menos uma letra minuscula (a-z).")

   if re.search(r"\d", senha): 
      score += 1
      criterios["numeros"] = True
   else: 
      criterios["numeros"] = False
      feedbacks.append("❌adicione caracteres especiais  (!@#$%&* etc.).")

   if senha.lower() not in SENHAS_COMUNS:
      score += 1
      criterios["nao_comum"] = True
   else:
      criterios["nao_comum"] = False
      feedbacks.append("Perigo: senha muito comum!")
   
   if score <= 2:
      classificacao = "MUITO FRACA"
      cor_classe = "vermelho"
   elif score <= 4: 
      classificacao = "FRACA"
      cor_classe = "amarelo"
   elif score <= 5: 
      classificacao = "MODERADA"
      cor_classe = "amarelo"
   elif score == 6:
      classificacao = "FORTE"
      cor_classe = "verde"
   else:
      classificacao = "MUITO FORTE"
      cor_classe = "verde"
   
   return {
     "score": score,
     "maximo": 7,
     "classificacao": classificacao,
     "cor_classe": cor_classe,
     "criterios": criterios,
     "feedbacks": feedbacks,
}
