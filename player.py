class Player:

  def __init__(self, name, hp, pilule, attackSP):
    self.name = name
    self.hp = hp
    self.pilule = pilule
    self.attackSP = attackSP

  def get_name(self):
    return self.name

  def set_name(self, name):
    self.name = name

  def get_hp(self):
    return self.hp

  def set_hp(self, hp):
    self.hp = hp

  def get_pilule(self):
    return self.pilule

  def set_pilule(self, pilule):
    self.pilule = pilule

  def get_attackSP(self):
    return self.attackSP

  def set_attackSP(self, attackSP):
    self.attackSP = attackSP