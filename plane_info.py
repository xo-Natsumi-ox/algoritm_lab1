class Plane:
    def __init__(self, name="none", max_height=0, max_lifring_weight=0):
        self.name = name
        self.max_height = max_height
        self.max_lifring_weight = max_lifring_weight

    def __repr__(self):
        return "Name = {}, max height = {}, max lifring weight = {}".format(self.name, self.max_height,
                                                                            self.max_lifring_weight)
