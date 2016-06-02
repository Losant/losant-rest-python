""" Module containing the LosantError class """

class LosantError(Exception):
    """ Exception class for any Losant API errors """

    def __init__(self, status, data):
        Exception.__init__(self)
        self.status = status
        self.data = data
        self.args = [status, data]

    def __str__(self):
        return str(self.status) + " " + str(self.data)
