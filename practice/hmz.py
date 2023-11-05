def welcome():
  print("Hey you are welcome my friend")


hamza = "A good boy"

#this will be executed whenever this hmz module is imported to some other python file
print(__name__)

# doing this so that the welcome function have to be called rather than executing itself whenever this module is imported   
if __name__ == "__main__":
  welcome()