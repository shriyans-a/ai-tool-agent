from chatbot_agent import route_command

def main():
  
  print("Welcome to the AI Tool Agent!")
  print("Available commands: calculate <expr>, weather <location>, read file <filename>")
  print("Type 'exit' to quit.")

  while True:
    user_input = input(">> ")
    if user_input.strip().lower() in ["exit", "quit"]:
      print("Session terminated")
      break
    response = route_command(user_input)
    print(response)

if __name__ == "__main__":
  main()
    

