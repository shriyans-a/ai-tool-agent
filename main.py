from chatbot_agent import route_command

def main(): # main function that users will run
  
  print("Welcome to the AI Tool Agent!")
  print("Available commands: calculate (expression), weather (location), read file (filename), or you can ask to search Opsera documentation for information.")
  print("Type 'exit' or 'quit' to terminate session.")

  while True: # keep asking for input unless they specifically exit or quit. 
    user_input = input(">> ")
    if user_input.strip().lower() in ["exit", "quit"]:
      print("Session terminated")
      break
    response = route_command(user_input) # use the route command function that will run the function from chatbot_agent.py
    print(response)

if __name__ == "__main__": # allows function to run after importing from another file. 
  main()
    

