# SBC 2016 TEMPO

def main():
  creditos = str(input()).split(" ")
  for i in range(len(creditos)):
    creditos[i] = int(creditos[i])
  return "S" if ((creditos[0] == creditos[1]) or (creditos[1] == creditos[2]) or (creditos[0] == creditos[2]) or (creditos[0] + creditos[1] == creditos[2]) or (creditos[1] + creditos[2] == creditos[0]) or (creditos[0] + creditos[2] == creditos[1])
  ) else "N"

if __name__ == "__main__":
  print(main())