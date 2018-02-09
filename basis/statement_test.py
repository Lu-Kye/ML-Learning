import typing

# Define method with parameters of clearly type
def echo(msg: str) -> typing.Any:
    print(msg)

# For
def foreach(collection: typing.Union[list, dict], 
            callback: callable = echo) -> typing.Any:
    for i in collection:
        # list element | dict key
        callback(i)
        # dict value
        if type(collection) == dict:
            callback(collection[i])

if __name__ == "__main__":
    echo("Hello World")
    foreach([1, 2, 3])
    foreach(dict(one=1, two=2))
