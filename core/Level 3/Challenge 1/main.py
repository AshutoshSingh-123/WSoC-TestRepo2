from type_of_sport import Outdoor, Indoor
# -------------------------------------------cricket extends outdoors class----------------------------------------
class Cricket(Outdoor):
 number_of_players=11 
 name='Cricket'
 def cricket_info(self):
  print("-------------------------------------x----------------------------")
  print("""The sport of cricket has a known history beginning in the late 16th century. Having originated in south-east England, it became the country's national sport in the 18th century and has developed globally in the 19th and 20th centuries.
   There are three formats:
     1. T20 --- 20 overs
     2. One Day --- 50 overs
     3. Test --- 450 overs""")
 def cricket_legends(self):
  print("-------------------- Gretest Cricket Players Of All TIme---------------------")
  print("""            Name       Country           Playing
        1. Sachin      India              No
        2. Kapil dev   India              No
        3. Brain Lara  West Indies        No""")
# ----------------------------- types of cricket------------------------------------------------
class T20(Cricket):
 time=3
 def t20_info(self):
  print("----------------------------------T20-------------------------------")
  print("DESCRIPTION------------->")
  print("""A newly-introduced variant of cricket from the general one-day matches, T20 cricket or Twenty20 cricket may be defined as a short cricket match limited to 20 overs of gameplay, lasting for about 80 minutes per innings, with half-an-hour interval in between. The beginnings of the T20 format can be traced to 2003 when it was introduced by the England and Wales Cricket Board. The format has met with mixed reactions from cricket experts and fans.""")
  
class Oneday(Cricket):
 time=6
 def oneday_info(self):
  print("----------------------------------One DAy-------------------------------")
  print("DESCRIPTION------------->")
  print("""A One Day International (ODI) is a form of limited overs cricket, played between two teams with international status, in which each team faces a fixed number of overs, currently 50 (used to be 60 overs until 1983). The Cricket World Cup, generally held every four years, is played in this format.""")
class Test(Cricket):
 time=35
 def test_info(self):
  print("----------------------------------Test -------------------------------")
  print("DESCRIPTION------------->")
  print("""Test cricket is the form of the sport of cricket with the longest match duration, and is considered the game's highest standard. Test matches are played between national representative teams that have been granted Test status, as determined and conferred by the International Cricket Council (ICC).""")

class Carrom(Indoor):
 name="Carrom"
 number_of_players=4
 def carrom_info(self):
  print("-------------------------------------x----------------------------")
  print("""Carrom is played on a square polished plywood board with a striker made of hard plastic and small circular wooden pieces called carrommen. The basic objective of carrom is to use the striker with a flick of the finger to drive the carrommen into any of the four corner pockets.""")
  print("-------------------- Gretest Carrom Players Of All TIme---------------------")
  print("""            Name                Country          Playing
        1. Maria Irudayam India              No
        2. Devendra       India              No
       """)

 
if __name__ == "__main__":
 print("Tpyes of sport you are interented in:  Indoors Or Outdoors ")
 typ = input("""Enter 'I' for Indoor
            and 'O' for Outdoor : """)
 if typ == 'I' :
  print('''Sports Info Availabel:
                1. Carrom
                
                Enter 1 for Carrom  :''')
  inp=int(input())
  if inp==1:
   c=Carrom()
   c.indoor_info()
   c.carrom_info()
  
 if typ == 'O':
  print('''Sports Info Availabel:
                1. Cricket
                
                Enter 1 for more info:''')
  inp=int(input())
  if(inp==1):
   c=Cricket()
   c.outdoor_info()
   c.cricket_legends()
   c.cricket_info()
   
   c.sport_info()
   print("""Enter : 1 for T20,
       2 for One day , 
       3 for Test :""")
   inp1=int(input())
   if(inp1==1):
    t=T20()
    t.t20_info()
   if(inp1==2):
    t=Oneday()
    t.oneday_info()
   if(inp1==3):
    t=Test()
    t.test_info()

