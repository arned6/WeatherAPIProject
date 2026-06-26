

class Comparator:
    """Comparator Engine for weather providers A and B."""
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.compare= {}


    def comparison(self):
        """Compares raw data from providers A and B and creates a new dictionary with the differences between them."""
        self.compare = {
            k: float(abs(self.d1.get(k, 0) - self.d2.get(k, 0)))
            if isinstance(self.d1.get(k, 0), (int, float)) and isinstance(self.d2.get(k, 0), (int, float))
            else self.d1.get(k, None)
            for k in set(self.d1) | set(self.d2)
        }
        return self.compare