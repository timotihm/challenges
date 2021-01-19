"""
Challenge :
    Find a number that is bigger than the given input and the most closest to it in a nested JSON.

Example:
    Input : 5
    Output : 9
    
    Input : 20
    Output : 25
    
    Input : 25
    Output : None
"""

array = {20:[{9:[5,{12:[11,14]}]}, 25]}

class RecursiveSearch:
    found = None
    
    def find(self, input, current_data):
        """
        Function to find closest bigger value of the input from the given nested JSON.
        """
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                self.find(input, key)
                self.find(input, value)
                return self.found
        elif isinstance(current_data, (list, tuple)):
            for record in current_data:
                self.find(input, record)
        elif isinstance(current_data, int):
            # you can modify line 23 - 26
            if current_data > input and self.found is None:
                self.found = current_data
            if current_data > input and current_data < self.found:
                self.found = current_data

print(RecursiveSearch().find(11, array))
