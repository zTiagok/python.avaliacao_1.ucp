# Aluno: Tiago Braga Costa
# Disciplina: Introdução à Programação 
# Professor: Marcelo Collares 
# Data: 03/Abril/2026

def main():
  answer: int = 0
  students: list[dict] = readFile()

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
  newName = input("\nNome do aluno: ")
  error = False

  for student in students:
    if student["name"] == newName:
      print("\nErro: Aluno já cadastrado.")
      error = True
  
  if not error:
    newGrade1 = input("Nota 1 do aluno: ")
    newGrade2 = input("Nota 2 do aluno: ")

    # Adiciona as informações do aluno no array de objetos.
    students.append({
      "name": newName,
      "grade1": float(newGrade1),
      "grade2": float(newGrade2),
      })
    
    writeFile(students)


def listStudents(students: list[dict]) -> list:
  studentList: list = []

  # Salva os estudantes em um array.
  for student in students:
    result = calculateAverage(student["grade1"], student["grade2"])
    studentList.append(f"Nome: {student["name"]} | Média: {result["averageGrade"]} | Situação: {result["status"]}")

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
  averageGrade = (float(grade1) + float(grade2)) / 2
  status = None

  if (averageGrade >= 7):
    status = "Aprovado"
  elif (averageGrade >= 5 and averageGrade < 7):
    status = "Recuperação"
  else:
    status = "Reprovado"

  return {
    "status": status, 
    "averageGrade": averageGrade
  }


def writeFile(students: list[dict]):
  with open("students.txt", "w", encoding="utf-8") as file:
    for student in students:
      line = f"{student["name"]},{student["grade1"]},{student["grade2"]}\n"
      file.write(line)


def readFile():
  students = []

  try:
    with open("students.txt", "r", encoding="utf-8") as file:
      for line in file:
        name, grade1, grade2 = line.strip().split(",")

        students.append({
          "name": name,
          "grade1": grade1,
          "grade2": grade2,
        })
    
  except FileNotFoundError:
    return []
  
  return students
    

# Inicia o programa principal.
if __name__ == "__main__":
  main()