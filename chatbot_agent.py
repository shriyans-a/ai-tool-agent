# Import the tools necessary for routing user input.
from tools import calculator, file_reader, weather

# Define function 
def route_command(command: str) -> str:
  command = command.strip().lower()

  if command.startswith("calculate"):
    return calculator.calculate()

  elif command.startswith("read file"):
    return file_reader.fileread()
  
  elif command.startswith("weather"):
    return weather.weather_lookup()

  else:
    return "Unknown command. Try 'calculate', 'weather', or 'read file'."




