def main():
  read_file()

def read_file():
  file_path = "/home/claudia/github_projects/python/03-file-handling/demofile.txt"
  file = open(file_path, "r")
  print(file.read())

  file = open(file_path, "r")
  print(file.readline())

  file = open(file_path, "r")
  print(file.read(1))

  file.close()

if __name__ == "__main__":
  main()
