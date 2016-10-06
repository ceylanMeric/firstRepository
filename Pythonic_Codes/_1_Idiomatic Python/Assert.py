def ex1():
    a=1
    def check_something(i):
        if i>0:
            return True
        else:
            return False

    assert check_something(a),  "There is a mistake happen, check fail"
    # Assert ler throw un en kolay hali
ex1()