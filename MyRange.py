class Range:
  """ A class that mimic's the built-in range class."""
  
  def __init__(self, start, stop = None, step = 1):
    """Initializr a Range instance.
    
    Semantics is similar to built-in range class.
    """
    if step == 0:
      raise ValueError('step cannot be 0')
