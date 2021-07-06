
#   This code is for making response  as  Initial email  for SR


sr_number = int(input("What is the SR you are working for? "))
print(sr_number)

#//https://csone.lightning.force.com/lightning/r/Case/5006R00001gw2Q0QAI/view?target=tab
#//https://scripts.cisco.com/app/quicker_csone/?sr=691687457


urlused = "https://scripts.cisco.com/app/quicker_csone/?sr="+str(sr_number)
import urllib

def read_text():
      quotes = urllib.urlopen(urlused)
      contents_file = quotes.read()
      print (contents_file)

read_text()