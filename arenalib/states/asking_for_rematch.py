from arenalib import renderer

class AskingForRematch:
  def __init__(self, last_state):
    renderer.initialize()

    self.finished = False
    self.quitting = False

  def update(self, client_size):
    pass

  def is_finished(self):
    pass

  def is_quitting(self):
    pass