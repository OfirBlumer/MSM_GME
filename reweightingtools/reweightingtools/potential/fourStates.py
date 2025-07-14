from openmm import CustomExternalForce

# openmm potential classes 
class fourStates(CustomExternalForce):

    def __init__(self):
        expression = "2.5 * (0.001 * (x^4) - 0.05 * (x^2) + 0.001 * (y^4) + 0.001 * (z^4) - 12.5 * exp(-0.2 * ((z - 3)^2) - 0.2 * ((x - 5)^2)) - "\
                     "10 * exp(-0.2 * ((z + 3)^2) - 0.2 * ((x - 5)^2)) - 11 * exp(-0.2 * ((y - 3)^2) - 0.2 * ((x + 5)^2)) - "\
                     "10 * exp(-0.2 * ((y + 3)^2) - 0.2 * ((x + 5)^2)))"
#        expression = "2.5 * (0.0000001 * (x^4) - 0.0005 * (x^2) + 0.0000001 * (y^4) + 0.0000001 * (z^4) - 12.5 * exp(-0.2 * ((0.1 * (z - 3))^2) - 0.2 * ((0.1 * (x - 5))^2)) - "\
#                     "10 * exp(-0.2 * ((0.1 * (z + 3))^2) - 0.2 * ((0.1 * (x - 5))^2)) - 11 * exp(-0.2 * ((0.1 * (y - 3))^2) - 0.2 * ((0.1 * (x + 5))^2)) - "\
#                     "10 * exp(-0.2 * ((0.1 * (y + 3))^2) - 0.2 * ((0.1 * (x + 5))^2)))"
        super(fourStates, self).__init__(expression)
