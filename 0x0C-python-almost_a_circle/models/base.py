#!/usr/bin/python3
"""Base class"""
import json
import csv


class Base:
    """class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation for the class

        Args:
            id (int, optional): id of object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts object to json string

        Args:
            list_dictionaries (object): object to be coverted

        Returns:
            str: string representation
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string to a file

        Args:
            list_objs (objcet): object to convert to string
        """
        ls = []
        if list_objs:
            ls = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), mode='w') as fd:
            fd.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """converts json string to object

        Args:
            json_string (str): string representation of object

        Returns:
            object: object representation of json string
        """
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new object with dictionary values

        Returns:
            object: new created object
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads a dictionary from a file and converts it to an instance

        Returns:
            object: new object that was created from dict in file
        """
        try:
            with open("{}.json".format(cls.__name__)) as fd:
                return [cls.create(**i) for i in
                        cls.from_json_string(fd.read())]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        with open("{}.csv".format(cls.__name__), mode="w") as fd:
            if list_objs:
                writer = csv.DictWriter(fd, fieldnames=fieldnames)
                writer.writeheader()
                for line in list_objs:
                    writer.writerows([line.to_dictionary()])
            else:
                writer = csv.writer(fd)
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open("{}.csv".format(cls.__name__), newline='') as fd:
                reader = csv.DictReader(fd)
                ls = []
                for line in reader:
                    for key, value in line.items():
                        line[key] = int(value)
                    ls.append(line)
                return [cls.create(**i) for i in ls]
        except Exception:
            return []
