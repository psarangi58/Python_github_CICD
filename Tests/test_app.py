from Src.app import home,index


def test_flaskapp():
    print("Hello world")
    assert home()=="Hello World"
