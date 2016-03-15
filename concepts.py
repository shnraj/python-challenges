# Python concept examples


# CLOSURES IN PYTHON

# Nested functions that
# 1) access variables that are local to enclosing scopes,
# 2) do so when they are executed outside of that scope.
def makeClosure(x):
    def clo(y):
        # x is "closed" in the definition of clo
        return y + x
    return clo
