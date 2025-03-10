class Flight:
    """A class representing a flight and its main information.

    Attributes:
        number (str): A unique identifier for the flight.
        origin (str): The departure location of the flight.
        destination (str): The destination location of the flight.
        num_passengers (int): The number of passengers on the flight.
        _total_weight (float): The weight of the aircraft (must be positive).
        _pilot (str): The name of the pilot.
        _crew (list): A list of the names of the crew members.

    Methods:
        display_flight_data(): Prints the flight information to the console.
    """

    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """Initialize an instance of Flight.

        :param number: (string) A unique identifier of the flight.
        :param origin: (string) The name of the location where the flight takes off from.
        :param destination: (string) The name of the location where the flight lands.
        :param num_passengers: (int) The number of people who are boarding the flight.
        :param total_weight: (float) The weight of the aircraft.
        :param pilot: (string) The name of the pilot.
        :param crew: (list[string]) The names of the crew members.
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew

    @property
    def total_weight(self):
        """The weight of the aircraft the is used for this particular flight.

        It is represented as a float number and must be greater than zero.
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight

    @property
    def pilot(self):
        """The name of the person who is flying the aircraft.

        It is represented as a string.
        """
        return self._pilot

    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot

    @property
    def crew(self):
        """The names of the people who assist passengers and are responsible for the flight.

        They are represented as a list of strings.
        """
        return self._crew

    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew

    def display_flight_data(self):
        """Print the flight details, including number, passengers, weight, pilot, and crew."""
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self._total_weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)


help(Flight)