class DataEntry:
    '''
    data: dict{param_name : value}
    '''
    def __init__(self, parameter: str, value: int):
        self.parameter = parameter
        self.value = value

    def commit_data(self):
        pass