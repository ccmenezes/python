def main():
  write_file()

def write_file():
  file_path = "/home/claudia/github_projects/python/03-file-handling/demofile.txt"
  file = open(file_path, "a")
  file.write("Now the file has more content!")
  file.close()

  file = open(file_path, "r")
  print(file.read())

if __name__ == "__main__":
  main()
