"""
    Copyright 2010 CNRS

    Author: Florent Lamiraux
"""
import wrap as stw
import dynamic_graph.entity as dge

class InvertedPendulum (dge.Entity):
    """
    This class binds dynamicgraph::tutorial::InvertedPendulum C++ class
    """
    def __init__(self, name):
        """
        Constructor: if not called by a child class, create and store a pointer
        to a C++ InvertedPendulum object.
        """
        if not self.object :
            self.object = stw.createInvertedPendulum(name)
        # Call parent constructor
        dge.Entity.__init__(self, name)

    @property
    def cart_mass(self):
        """
        Get mass of the cart
        """
        return stw.invertedPendulumGetCartMass(self.object)

    @cart_mass.setter
    def cart_mass(self, mass):
        """
        Set mass of the cart
        """
        return stw.invertedPendulumSetCartMass(self.object, mass)

    @property
    def pendulum_mass(self):
        """
        Get mass of the pendulum
        """
        return stw.invertedPendulumGetPendulumMass(self.object)

    @cart_mass.setter
    def pendulum_mass(self, mass):
        """
        Set mass of the pendulum
        """
        return stw.invertedPendulumSetPendulumMass(self.object, mass)
