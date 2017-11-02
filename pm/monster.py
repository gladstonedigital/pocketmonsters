#!/usr/bin/env python3

from enum import Enum

class Status(Enum):
    Ok = 0
    Faint = 1
    Poison = 2
    Sleep = 3
    Paralyzed = 4
    Frozen = 5
    Burn = 6

class PocketMonster:
    class Move:
        def __init__(self, name, element, damage, uses):
            self.name = name
            self.element = element
            self.damage = damage
            self.uses = uses

        def execute(self, user, target):
            effectiveness = 1.0
            self.uses -= 1
            return self.damage * effectiveness

    def __init__(self, name, element, level, health, moves):
        self.name = name
        self.element = element
        self.level = level
        self.health = health
        self.moves = moves
        self.status = Status.Ok

    def take_hit(self, opponent, move):
        damage = move.execute(opponent, self)
        print("%s hit %s for %d damage" % (opponent.name, self.name, damage))
        self.health -= damage
        if self.health <= 0:
            print("%s fainted!" % (self.name))
            self.health = 0
            self.status = Status.Faint

