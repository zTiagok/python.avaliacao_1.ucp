# Aluno: Tiago Braga Costa
# Disciplina: Introdução à Programação 
# Professor: Marcelo Collares 
# Data: 03/Abril/2026

answer: int = 0
student: list[dict] = {}

# Enquanto a resposta for menor que 1 ou maior que 5, será mostrado o print e o input.
while (int(answer) != 5):
  print("\n1 - Cadastrar aluno\n" \
        "2 - Listar alunos\n" \
        "3 - Calcular média da turma \n" \
        "4 - Buscar aluno por nome \n" \
        "5 - Sair")

  answer = input("Selecione uma opção: ")