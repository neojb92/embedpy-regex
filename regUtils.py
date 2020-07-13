#!/usr/bin/python
#import pandas as pd
#import numpy as np
import re
import functools

def error_sink(func):
    @functools.wraps(func)
    def inner_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return 'Error : '+str(e)
    return inner_wrapper

def regSearch(string,pattern,flags=0):
    assert type(pattern) is str, 'pattern must be a string type'
    assert type(string) is str, 'string input is not of string type'
    res = re.search(pattern,string,flags)
    if res:
        return res.group(0)
    else:
        return ''

#@error_sink
def regMatch(string,pattern,flags=0):

    assert type(pattern) is str, 'pattern must be a string type'
    if type(string) is list:
        assert all([type(i) is str for i in string]), 'string input contains elements which are not of string type'
        prog = re.compile(pattern,flags)
        return [bool(prog.fullmatch(i)) for i in string]

    else:
        assert type(string) is str, 'string input is not of string type'
        return bool(re.fullmatch(pattern,string,flags))



def regSub(string,pattern,repl,count=0,flags=0):
    assert type(pattern) is str, 'pattern must be a string type'
    assert type(repl) is str, 'replacement value must be a string type'
    if type(string) is list:
        assert all([type(i) is str for i in string]), 'string input contains elements which are not of string type'
        prog = re.compile(pattern,flags)
        return [prog.sub(repl,i,count) for i in string]

    else:
        assert type(string) is str, 'string input is not of string type'
        return re.sub(pattern,repl,string,count,flags)

def regFormat(string,pattern):
   
    if not type(pattern) is list: pattern=[pattern]
    return string.format(*pattern)
