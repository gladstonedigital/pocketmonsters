from enum import Enum

class STATUS(Enum):
   OK = 0
   FAINT = 1

class PocketMonster:
   class Move:
      def __init__(self, name, element, damage, uses):
         self.name = name
         self.element = element
         self.damage = damage
         self.uses = uses

   def __init__(self, name, element, level, health, moves):
      self.name = name
      self.element = element
      self.level = level
      self.health = health
      self.moves = moves
      self.status = STATUS.OK

   def take_hit(self, opponent, move):
      print("%s hit %s for %d damage" % (opponent.name, self.name, move.damage))
      self.health -= move.damage
      if self.health <= 0:
         print("%s fainted!" % (self.name))
         self.health = 0
         self.status = STATUS.FAINT

      move.uses -= 1

