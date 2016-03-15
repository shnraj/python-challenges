# CLOSURES IN PYTHON

# Nested functions that
# 1) access variables that are local to enclosing scopes,
# 2) do so when they are executed outside of that scope.

def makeClo(x):
    def clo(y):
        # x is "closed" in the definition of clo
        return y + x
return clo

clo5 = makeClo(5)
clo10 = makeClo(10)

clo5(5) # returns 10
clo10(5) # returns 15
