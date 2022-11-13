from dataclasses import dataclass, field

@dataclass
class CodeRunner():
    content : dict = field(default_factory=dict)
    location: list = field(repr=False,default_factory=list)
    
    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, key, value):
        self.set_value(key, value)

    def __contains__(self, key):
        return self.key_exists(key)

    # set_location :: str -> None
    def set_location(self, location: str):
        '''adds a location to the location list'''
        if not location in self.content and location != "":
            self.content[location] = {}
        self.location.append(location)

    # pop :: str -> any
    def pop(self, key: str) -> any:  # type: ignore
        '''removes a key from content with a location and a key and returns the value'''
        if self.location[-1] == "":
            return self.content.pop(key)
        return self.content[self.location[-1]].pop(key)

    # pop_location :: None -> None
    def pop_location(self):
        '''removes the last location from the location list thus going back one location'''
        self.location.pop()

    # get_location :: None -> None
    def get_location(self):
        '''returns the current location'''
        return self.location[-1]

    # set_value :: str -> any -> None
    def set_value(self, key: str, value: any):  # type: ignore
        '''sets a value in content with a key and value'''
        if self.location[-1] == "":
            self.content[key] = value
        else:
            self.content[self.location[-1]][key] = value

    # get_value :: str -> any
    def get_value(self, key: str) -> any:  # type: ignore
        '''gets a value from content with a key and value'''
        # If the key exists in the current location
        if self.location[-1] != "": 
            return self.content[self.location[-1]][key]
        # If the key exists in the global content
        elif self.key_exists(key):
            return self.content[key]
        else:
            raise KeyError(f"Key {key} does not exist in content")

    # key_exists :: str -> bool
    def key_exists(self, key: str) -> bool:
        '''checks if a key exists in content with a location and a key or in the global content'''
        if self.location[-1] != "":
            return key in self.content[self.location[-1]] or key in self.content
        return key in self.content