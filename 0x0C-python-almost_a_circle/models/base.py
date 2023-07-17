#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """defines the model base.

    Represents the "base" for all other classes in this project.

    Attributes:
        __nb_objects (int): The number of total instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base.

        Args:
            id (int): The id assigned to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialisation of list of dictionaries.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of the JSON string.

        Args:
            json_string (str): A JSON string of the list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): value pairs of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Return list of classes instantiated from a the file of JSON strings.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        namefile = str(cls.__name__) + ".json"
        try:
            with open(namefile, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Write CSV serialization of the list of objects into a file.

        Args:
            list_objs (list): list of inherited Base instances.
        """
        namefile = cls.__name__ + ".csv"
        with open(namefile, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ob in list_objs:
                    writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Return the list of classes instantiated from the CSV file.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        namefile = cls.__name__ + ".csv"
        try:
            with open(namefile, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): list of Rectangle objects.
            list_squares (list): list of Square objects.
        """
        turte = turtle.Turtle()
        turte.screen.bgcolor("#b7312c")
        turte.pensize(3)
        turte.shape("turtle")

        turte.color("#ffffff")
        for rec in list_rectangles:
            turte.showturtle()
            turte.up()
            turte.goto(rec.x, rec.y)
            turte.down()
            for n in range(2):
                turte.forward(rec.width)
                turte.left(90)
                turte.forward(rec.height)
                turte.left(90)
            turte.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
