# Imagine we have a long list of codewords and each codeword triggers a specific function to be called.
# For example, we have the codewords 'go' which when seen calls the function handleGo, and another codeword 'ok' which when seen calls the function handleOk.
# We can use a dictionary to encode this.

def handleGo(x):
    return "Handling a go! " + x


def handleOk(x):
    return "Handling an ok!" + x


# This is dictionary:        
codewords = { 
  'go': handleGo,   # The KEY here is 'go' and the VALUE it maps to is handleGo (Which is a function!).
  'ok': handleOk,   
}
# This dictionary pairs STRINGS (codewords) to FUNCTIONS.


# Now, we see a codeword given to us:
codeword = "go"


# We can handle it as follows:
if codeword in codewords:
        answer = codewords[codeword]("Argument")
        print(answer)
else:
        print("I don't know that codeword.")
