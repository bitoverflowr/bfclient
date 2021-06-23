import json
class Client:

  def create(self,clientname,details):
    self.name = clientname
    self.details  = details
  
  def passer(self):
    return { "name" : self.name , "details" : self.details }
  
  def acknowledge(self,data):
     self.name =  data["name"]
     self.details =  data["details"] 
     
  def connected(self, clt):
    self.clientobject = clt
    
  def getdisplayname(self):
    try:
      return self.name
    except:
      return "Unnamed"
  
  
