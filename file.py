# Aluno: Tiago Braga Costa
# Disciplina: Introdução à Programação 
# Professor: Marcelo Collares 
# Data: 03/Abril/2026

answer: int = 0

# Enquanto a resposta for menor que 1 ou maior que 5, será mostrado o print e o input.
while (int(answer) != 5):
  print("\n1 - Cadastrar aluno\n2 - Listar alunos\n3 - Calcular m" \
  "édia da turma\n4 - Buscar aluno por nome\n5 - Sair")

  answer = input("Selecione uma opção: ")