class EntityDoesNotExist(Exception):
    """
    Throw an exception when the data does not exist in the database
    """

    
class EntityAlreadyExists(Exception):
    """
    Throw an exception when the data already exists in the database
    """