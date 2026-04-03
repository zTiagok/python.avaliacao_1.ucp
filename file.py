# Aluno: Tiago Braga Costa
# Disciplina: Introdução à Programação 
# Professor: Marcelo Collares 
# Data: 03/Abril/2026

def main():
  answer: int = 0
  students: list[dict] = [{
    "name": "Tiago",
    "grade1": 1,
    "grade2": 2
  },
  {
    "name": "Tiago 2",
    "grade1": 5,
    "grade2": 5
  },
  {
    "name": "Alice",
    "grade1": 5,
    "grade2": 5
  },
  {
    "name": "Laranja",
    "grade1": 5,
    "grade2": 5
  },
  ]

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
      case 2:
        listarAlunos(students)
      case 4:
        procurarAluno(students)
        

def cadastrarAluno(students: list[dict]):
  student_name = input("\nNome do aluno: ")
  student_grade_1 = input("Nota 1 do aluno: ")
  student_grade_2 = input("Nota 2 do aluno: ")

  # Adiciona as informações do aluno no array de objetos.
  students.append({
    "name": student_name,
    "grade1": float(student_grade_1),
    "grade2": float(student_grade_2),
    })


def listarAlunos(students: list[dict]):
  # Adiciona um espaço para melhor visualização da listagem.
  print("\n")

  for student in students:
    result = calcularMedia(student["grade1"], student["grade2"])
    print(f"Nome: {student["name"]} | Média: {result["average_grade"]} | Situação: {result["status"]}")


def procurarAluno(students: list[dict]) -> str:
  name = input("\nDigite o nome do aluno: ")
  search: list[dict] = []

  # Procura e lista todos os nomes no range da procura.
  for student in students:
    if name.lower() in str(student["name"]).lower():
      search.append(student)

  listarAlunos(search)


def calcularMedia(grade1: float, grade2: float) -> dict:
  average_grade = (grade1 + grade2) / 2
  status = None

  if (average_grade >= 7):
    status = "Aprovado"
  elif (average_grade >= 5 and average_grade < 7):
    status = "Recuperação"
  else:
    status = "Reprovado"

  return {
    "status": status, 
    "average_grade": average_grade
  }




# Inicia o programa principal.
if __name__ == "__main__":
  main()