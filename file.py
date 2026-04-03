# Aluno: Tiago Braga Costa
# Disciplina: Introdução à Programação 
# Professor: Marcelo Collares 
# Data: 03/Abril/2026

def main():
  answer: int = 0
  students: list[dict] = []

  while (int(answer) != 5):
    print("\n1 - Cadastrar aluno\n" \
          "2 - Listar alunos\n" \
          "3 - Calcular média da turma \n" \
          "4 - Buscar aluno por nome \n" \
          "5 - Sair")

    answer = int(input("Selecione uma opção: "))

    match(answer):
      case 1:
        insertStudent(students)
      case 2:
        listStudents(students)
      case 4:
        searchStudent(students)
        

def insertStudent(students: list[dict]):
  student_name = input("\nNome do aluno: ")
  student_grade_1 = input("Nota 1 do aluno: ")
  student_grade_2 = input("Nota 2 do aluno: ")

  # Adiciona as informações do aluno no array de objetos.
  students.append({
    "name": student_name,
    "grade1": float(student_grade_1),
    "grade2": float(student_grade_2),
    })
  
  writeFile(students)


def listStudents(students: list[dict]) -> list:
  studentList: list = []

  # Salva os estudantes em um array.
  for student in students:
    result = calculateAverage(student["grade1"], student["grade2"])
    studentList.append(f"Nome: {student["name"]} | Média: {result["average_grade"]} | Situação: {result["status"]}")

  # Printa todos os alunos dentro do array caso não esteja vazio.
  if len(studentList) > 0:
    # Adiciona um espaço para melhor visualização da listagem.
    print("\n")
    for item in studentList:
      print(item)
  else:
    print("\nErro: Aluno(s) não encontrado(s).")

  # Retorna o array.
  return studentList


def searchStudent(students: list[dict]) -> str:
  name = input("\nDigite o nome do aluno: ")
  search: list[dict] = []

  # Procura e lista todos os nomes no range da procura.
  for student in students:
    if name.lower() in str(student["name"]).lower():
      search.append(student)

  # Verifica o tamanho do array, caso seja 0 então mostrar erro.
  if len(search) == 0:
    print("\nErro: Aluno(s) não encontrado(s).")
  else:
    listStudents(search)


def calculateAverage(grade1: float, grade2: float) -> dict:
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


def writeFile(students: list[dict]):
  with open("students.txt", "w", encoding="utf-8") as file:
    file.write(str(students))

def readFile():
  try:
    with open("students.txt", "r", encoding="utf-8") as file:
      return file.read()
    
  except FileNotFoundError:
    return []
    

# Inicia o programa principal.
if __name__ == "__main__":
  main()