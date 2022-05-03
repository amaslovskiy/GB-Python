simple_string = "Hey, You"
byte_string = b"Hey, You"
byte_array_string = bytearray(byte_string)

print(byte_string)
print(type(simple_string))
print(type(byte_string))
print(type(byte_array_string))

name = "John"
byte_name = name.encode()
print(type(byte_name))