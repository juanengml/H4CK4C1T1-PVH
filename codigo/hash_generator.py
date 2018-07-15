import random
import md5 

def sorted(data):
  d = random.choice(data)
  return data

def join_data():
  

  m = md5.new()
  m.update("Nobody inspects")
  m.update(" the spammish repetition")
  print m.digest()

def main():

