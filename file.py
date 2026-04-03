# Aluno: Tiago Braga Costa
# Disciplina: Introdução à Programação 
# Professor: Marcelo Collares 
# Data: 03/Abril/2026

def main():
  answer: int = 0
  students: list[dict] = []

  # Enquanto a resposta for menor que 1 ou maior que 5, será mostrado o print e o input.
  while (int(answer) != 5):
    print("\n1 - Cadastrar aluno\n" \
          "2 - Listar alunos\n" \
          "3 - Calcular média da turma \n" \
          "4 - Buscar aluno por nome \n" \
          "5 - Sair")

    answer = int(input("Selecione uma opção: "))

    match(answer):
      case 1:
        cadastrarAluno(students)


def cadastrarAluno(students: list[dict]):
  student_name = input("\nNome do aluno: ")
  student_grade_1 = input("Nota 1 do aluno: ")
  student_grade_2 = input("Nota 2 do aluno: ")

  # Adiciona as informações do aluno no array de objetos.
  students.append({
    "nome": student_name,
    "nota1": float(student_grade_1),
    "nota2": float(student_grade_2),
    })


# Inicia o programa principal.
if __name__ == "__main__":
  main()