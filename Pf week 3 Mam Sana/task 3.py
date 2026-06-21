# Uppercase karne ke liye lambda
to_upper = lambda s: s.upper()

# String ko ulta karne ka basic UDF
def invert(text):
    # Python mein [::-1] string ko direct ulta kar deta hai
    print("Ulta string:", text[::-1])

user_string = input("String likhein: ")

uppercase_string = to_upper(user_string)
invert(uppercase_string)