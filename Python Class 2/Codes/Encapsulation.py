class Account:
    def __init__(self, balance):
        self._balance = balance  # private variable
    
    def get_balance(self):
        return self._balance