'''
Example postmortem
`python3 -m pdb -c continue my_script.py`
Note - this will not postmortem on top level script issues - the error must be at least one function call deep
https://docs.python.org/3/library/pdb.html
https://stackoverflow.com/a/2438834/3356840
'''
def my_func():
    print('hello')
    aa = [1,2,3]
    aa[4] = 4
    print('world')
if __name__ == '__main__':
    my_func()