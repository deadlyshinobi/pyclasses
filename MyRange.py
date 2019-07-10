class Range:
  """ A class that mimic's the built-in range class."""
  
  def __init__(self, start, stop = None, step = 1):
    """Initializr a Range instance.
    
    Semantics is similar to built-in range class.
    """
    if step == 0:
      raise ValueError('step cannot be 0')
    
    if stop is None:
      start , stop = 0 , start

    self._length = max(0, (stop - start + step - 1)// step)
    self._start = start
    self._step = step

  def __len__(self):
    """Return number of entities in the range."""
    return self._length
  

  def __getitem__(self,k):
    """Return entry at the index."""
    if k < 0:
      k +=len(self)
    
    if not 0 <= k <self._length:
      raise IndexError("Index out of range")
    
    return self._start + k * self._step

