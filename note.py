common = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']

class Note:
  def __init__(self, noteName, octave=None):
    self.octave = octave
    if type(noteName) is int:
      offset, idx = divmod(noteName, 12)
      self.name = common[idx]
      self.octave = offset - 1
    else:
      self.name = noteName
    if self.octave is not None:
      self.scientific = self.name + str(self.octave)
