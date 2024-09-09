import os

def main():

  file_path = "/home/claudia/github_projects/python/03-file-handling/demofile1.txt"
  if os.path.exists(file_path):
    os.remove(file_path)
  else:
    print("The file does not exist")

if __name__ == "__main__":
  main()
