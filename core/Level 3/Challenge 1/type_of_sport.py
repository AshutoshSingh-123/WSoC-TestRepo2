from sport import sports

# ------------------------------- for outdoors games extend sports class----------------------------------------------
class Outdoor(sports):
 def outdoor_info(self):
  print("----------------",self.name,"""IS A OUTDOORS GAME--------------------
  This category includes a class of games, sports or other recreational activities which take place outdoors and involve some form of navigation to locate a target place or object.""")
# -------------------------------for indoors games--------------------------------------------------
class Indoor(sports):
 def indoor_info(self):
  print("----------------",self.name,"""IS A INDOORS GAME--------------------
  This category includes a class of games, sports or other recreational activities which take place indoors and involve some form of navigation to locate a target place or object.""")