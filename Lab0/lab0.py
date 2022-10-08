import math
class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.

    This includes the lcm (least common multiple) and 
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        '''Set the values of u and v to be used in the math operations.'''
        self.u = u
        self.v = v
    
    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)
    
    def valid(self):
        '''True if both u and v are integers.'''
        return isinstance(self.u, int) and isinstance(self.v, int)
    
    def __euclid(self, u, v):
      """
      Returns the greatest common divisor of u and v using Euclid's algorithm.
      
        Parameters:
          u (int) : An integer
          v (int) : Another integer

        Returns:
          gcd (int) : greatest common divisor of u and v
      """
      gcd, remainder = (u, v) if u > v else (v, u)

      while remainder != 0:
        temp = remainder
        remainder = gcd % remainder
        gcd = temp

      return gcd

    def gcd(self):
      '''Compute the greatest common divisor of member variables u and v.'''
      tempU = self.u
      tempV = self.v
        
      try:
        
        # Handle inf inputs
        if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
          raise OverflowError

        # Handle bad inputs
        if not self.valid() and not (isinstance(tempU, float) and isinstance(tempV, float)):
          raise TypeError
        
        # Handle floats and negatives
        # Note: this comes before handling zero, as 0.0 and -0.0 are potental inputs
        tempU, tempV = abs(math.ceil(tempU)), abs(math.ceil(tempV))

        # Handle Zero Cases
        if tempU == 0 or tempV == 0:
          return max(tempU, tempV)

        return self.__euclid(tempU, tempV)

      except OverflowError:
        print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
        raise OverflowError
          
      except TypeError:
        print(f"one or both the values of {tempU} and {tempV} are not equal to numbers")
        raise TypeError
             

        
    def lcm(self):
      '''Compute the least common multiple of member variables u and v.'''

      try:
        tempU = self.u
        tempV = self.v
        if tempU in [0, 0.0, -0.0] or tempV in [0, 0.0, -0.0]:
          raise ValueError
        
        # gcd should handle remaining errors
        return abs(math.ceil(tempU) * math.ceil(tempV)) / self.gcd()
      
      except ValueError:
          print(f"The least common multiple of {tempU} and {tempV} is not defined. Is one of these 0?")
          raise ValueError

