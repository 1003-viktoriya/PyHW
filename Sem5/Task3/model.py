field = ['1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']
mark = 'X'
# def switch_mark():
#     global mark
#     if mark == 'X':
#         mark = '0'
#     else:
#         mark = 'X'
def get_mark():
    global mark
    return mark
def get_field():
    global field
    return field
def set_field(index: int):
    global field
    global mark
    field[index-1] = mark
    switch_mark()
def switch_mark():
    global mark
    if mark == 'X':
        mark = '0'
    else:
        mark = 'X'
        