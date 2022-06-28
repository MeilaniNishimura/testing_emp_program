try:
    pass
# You can out multiple exceptions, put more specific ones at the top
except ErrorName:
    pass
except Exception as e:
    pass
# You can account for specific errors or general ones
# You can print excpetion as a variable and that will print out 
# the specific error message as opposed to custom error message
# This will print actual error message
except Exception as e:
    print(e)
# Else accounts for if try block does not throw exception
else:
    pass
# raise your own exception
if (whatever exception you want to raise):
    raise Exception

# for example
if input = str:
    raise Error your input is invalid