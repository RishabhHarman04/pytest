import calculator

def test_add():
    x=20
    y=13
    result=calculator.add(x, y)
    assert x+y == result
def test_sub():
    x=20
    y=13
    result=calculator.sub(x, y)
    assert x-y == result
def test_mult():
    x=20
    y=13
    result=calculator.mult(x, y)
    assert x*y == result
def test_div():
    x=20
    y=13
    result=calculator.div(x, y)
    assert x/y == result