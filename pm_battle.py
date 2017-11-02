from pm_monster import PocketMonster
from pm_monster import STATUS
import itertools

def main():
   player1 = {}
   player1["monsters"] = []
   player2 = {}
   player2["monsters"] = []

   player1["monsters"].append(PocketMonster(
      name="Pikachu", 
      element="electric", 
      level=5, 
      health=30, 
      moves=[
         PocketMonster.Move(name="Thundershock", damage=10, uses=10, element="electric"),
         PocketMonster.Move(name="Swipe", damage=7, uses=15, element="neutral")
      ]
   ))

   player2["monsters"].append(PocketMonster(
      name="Rattata", 
      element="neutral", 
      level=5, 
      health=25, 
      moves=[
         PocketMonster.Move(name="Burrow", damage=0, uses=10, element="neutral"),
         PocketMonster.Move(name="Swipe", damage=7, uses=15, element="neutral")
      ]
   ))

# TODO
"""
   player = player1
   opponent = player2
   while True:
"""

if __name__ == "__main__":
   main()