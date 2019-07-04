class Vector:
  """Represents a vector in multidimensional space."""

  def __init__(self,d):
    """ Create d-dimension vector of zeros."""
    self._coords=[0] * d

    def __len__(self):
      """Return the dimension of the vector."""
      return len(self._coords)

    def __getitem__(self,j):
      """Return jth coordinate of vector."""
      return self._coords[j]

    def __setitem__(self,j,val):
      self._coords[j]=val

    def __add__(self,second_vector):
      """Return sum of two vectors."""
      if len(self) != len(second_vector):
        raise ValueError('Dimesions must be same')
      result = Vector(len(self))
      for j in range(len(self)):
        result[j] = self[j] + second_vector[j]

      return result


    def __eq__(self,second_vector):
      """Return True if vector has same coodinates as other."""
      return self._coords == second_vector._coords


    def __ne__(self,second_vector):
      """Return True if vectors differs from other."""
      return not self == second_vector


    def __str__(self):
      """Produces string representative of vector."""
      return '<' + str(self._coords)[1:-1] +'>'
