#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Name_of_program: Scaner.py

Description: The finite state machine is implemented 
for analyzing and processing text of the programm written in the C language.
At the output, you get file with the internal view and file with the table of names.

Date_of_creation: 21.12.2017

Version: 3

Last_modification: 21.12.2017
"""

import sys

res_words = {'main':[ 1, 'main function'],
            'return':[2, 'return from function'],
            'int': [3, 'integer type'],
            'float': [4, 'float type'],
            'goto': [5, 'unconditional operator'],
            'for': [6, 'cycle operator'],
            'if': [7, 'conditional operator'],
            ';': [8, 'empty operator'],
            '{': [10, 'left brace'],
            '}': [11, 'right brace'],
            '(': [20,'left brackets'],
            ')':[21, 'right brackets'],
            '+':[-1, 'addition'],
            '-':[-2,'subtraction'],
            '*':[-3, 'multiplication'],
            '/':[-4,'division'],
            '++':[-5, 'prefix increment'],
            '--':[-6, 'prefix decrement'],
            '=':[-7, 'assignment'],
            '==':[30,'comparison: assignment'],
            '<=':[31,'less-equal'],
            '<':[32, 'less'],
            '>=':[33,'more-equal'],
            '>':[34, 'more'],
            '!=':[35,'not equal'],
            ',':[40, 'comma operator'],
            '//':[41, 'comment']}

string = ''
char = ''

#procedures:

def add(char, string):
    string = string + char    
    return string

def write_and_add_new(char, string):
    return 'write!', string, char

def nothing(char, string):
    string = ''
    return string

def add_and_write(char,string):
    return 'write!', string + char

#conditions:

def is_letter(char):
    return char.isalpha()

def is_letter_or_figure_or_underline(char):
    if char.isalnum() == True or char == '_':
        return True
       
def is_not_letter_or_figure_or_underline(char):
    if char.isalnum() != True and char != '_':
        return True
    
def is_not_letter_or_figure_or_underline_or_label(char):
    if char.isalnum() != True and char != '_' and char != ':':
        return True
    
def is_figure(char):
    return char.isdigit()

def is_not_figure(char):
    return not char.isdigit()

def is_point(char):
    if char == '.':
        return True
    
def is_label(char):
    if char == ':':
        return True
    
def is_more(char):
    if char == '<':
        return True
    
def is_h(char):
    if char == 'h':
        return True
    
def is_less(char):
    if char == '>':
        return True

def is_special_simbol(char):
    if char == '(' or char == ')' or
       char == '{' or char == '}' or
       char == ';' or char == ',' or
       char == '*':
        return True

def is_slash(char):
    if char == '/':
        return True
    
def is_not_slash(char):
    if char != '/':
        return True

def is_n(char):
    if char == 'n':
        return True
    
def is_not_n(char):
    if char != 'n':
        return True

def is_plus(char):
    if char == '+':
        return True
    
def is_not_plus(char):
    if char != '+':
        return True
    
def is_minus(char):
    if char == '-':
        return True
    
def is_not_minus(char):
    if char != '-':
        return True
    
def is_equal(char):
    if char == '=':
        return True
    
def is_not_equal(char):
    if char != '=':
        return True
    
def is_exc_p(char):
    if char == '!':
        return True
    
def is_space(char):
    if char == '\t' or char == ' ':
        return True
		
def is_string1(char):
	if char == "'":
		return True

def is_not_string1(char):
	if char != "'":
		return True
		
def is_string2(char):
	if char == '"':
		return True

def is_not_string2(char):
	if char != '"':
		return True

FSM_MAP = (

    #  {'откуда':, 'куда':, 'условие':, 'что делаем': },

    {'q1': 'S', 
     'q2': 'N1',
     'c': is_letter , 
     'proc': add},  # 0

    {'q1': 'N1',
    'q2': 'N1',
    'c': is_letter_or_figure_or_underline,
    'proc': add},  # 1

    {'q1': 'N1',
    'q2': 'S',
    'c': is_not_letter_or_figure_or_underline_or_label,
    'proc': write_and_add_new},  # 2

    {'q1': 'S',
    'q2': 'D1',
    'c': is_figure,
    'proc': add},  # 3

    {'q1': 'D1',
    'q2': 'D1',
    'c': is_figure,
    'proc': add},  # 4

    {'q1': 'D1',
    'q2': 'D2',
    'c': is_point,
    'proc': add},  # 5

    {'q1': 'D2',
    'q2': 'D2',
    'c': is_figure,
    'proc': add},  # 6
    
    {'q1': 'D1',
    'q2': 'S',
    'c': is_not_figure,
    'proc': write_and_add_new},  # 7

    {'q1': 'D2',
    'q2': 'S',
    'c': is_not_figure,
    'proc': write_and_add_new},  # 8

    {'q1': 'Z',
    'q2': 'N1',
    'c': is_letter,
    'proc': add},  # 9
    
    {'q1': 'N1',
    'q2': 'S',
    'c': is_label,
    'proc': add_and_write},  #10   
    
    {'q1': 'S',
    'q2': 'S',
    'c': is_special_simbol,
    'proc': add_and_write },  #11
    
    {'q1': 'S',
    'q2': 'C1',
    'c': is_slash,
    'proc': add},  #12
    
    {'q1': 'C1',
    'q2': 'C2',
    'c': is_slash,
    'proc': nothing},  #13
    
    {'q1': 'C2',
    'q2': 'C2',
    'c': is_not_slash,
    'proc': nothing}, #14 
    
    {'q1': 'C2',
    'q2': 'C3',
    'c': is_slash,
    'proc': nothing}, #15
    
    {'q1': 'C3',
    'q2': 'C2',
    'c': is_not_n,
    'proc': nothing}, #16
    
    {'q1': 'C3',
    'q2': 'S',
    'c': is_n,
    'proc': nothing}, #17
    
    {'q1': 'C1',
     'q2': 'S',
     'c': is_not_slash,
     'proc': write_and_add_new},  #18
    
    {'q1': 'S',
     'q2': 'P1',
     'c': is_plus,
     'proc': add},  #19
    
    {'q1': 'P1',
     'q2': 'S',
     'c': is_not_plus,
     'proc': write_and_add_new}, #20
    
    {'q1': 'P1',
    'q2': 'S',
    'c': is_plus,
    'proc': add_and_write}, #21
    
    {'q1': 'S',
     'q2': 'M1',
     'c': is_minus,
     'proc': add},  #22
    
    {'q1': 'M1',
     'q2': 'S',
     'c': is_not_minus,
     'proc': write_and_add_new}, #23
    
    {'q1': 'M1',
    'q2': 'S',
    'c': is_minus,
    'proc': add_and_write}, #24
     
    {'q1': 'S',
     'q2': 'E1',
     'c': is_equal,
     'proc': add},  #25
    
    {'q1': 'E1',
     'q2': 'S',
     'c': is_not_equal,
     'proc': write_and_add_new}, #26
    
    {'q1': 'E1',
    'q2': 'S',
    'c': is_equal,
    'proc': add_and_write}, #27
     
     {'q1': 'S',
     'q2': 'ME1',
     'c': is_more,
     'proc': add},  #28
    
    {'q1': 'ME1',
     'q2': 'S',
     'c': is_not_equal,
     'proc': write_and_add_new}, #29
    
    {'q1': 'ME1',
    'q2': 'S',
    'c': is_equal,
    'proc': add_and_write}, #30
     
    {'q1': 'S',
     'q2': 'LE1',
     'c': is_less,
     'proc': add},  #31
    
    {'q1': 'LE1',
     'q2': 'S',
     'c': is_not_equal,
     'proc': write_and_add_new}, #32
    
    {'q1': 'LE1',
    'q2': 'S',
    'c': is_equal,
    'proc': add_and_write}, #33
     
    {'q1': 'S',
    'q2': 'Ex1',
    'c': is_exc_p,
    'proc': add},  #34
    
    {'q1': 'Ex1',
    'q2': 'S',
    'c': is_equal,
    'proc': add_and_write},  #35
    
    {'q1': 'S',
    'q2': 'S',
    'c': is_space,
    'proc': nothing}, #36
	
	{'q1': 'S',
    'q2': 'St1',
    'c': is_string1,
    'proc': add}, #37
	
	{'q1': 'St1',
    'q2': 'St1',
    'c': is_not_string1,
    'proc': add}, #38
	
	{'q1': 'St1',
    'q2': 'S',
    'c': is_string1,
    'proc': add_and_write}, #39
	
	{'q1': 'S',
    'q2': 'St2',
    'c': is_string2,
    'proc': add}, #40
	
	{'q1': 'St2',
    'q2': 'St2',
    'c': is_not_string2,
    'proc': add}, #41
	
	{'q1': 'St2',
    'q2': 'S',
    'c': is_string2,
    'proc': add_and_write}, #42
	
)


def do_rule(fsm_map, line):
    words = []
    string = ''
    start = 'S'
    k=0
    while k<len(line)-1:
        char = line[k]  
        index = [i for i in range(len(fsm_map))
                 if fsm_map[i]['q1'] == start and fsm_map[i]['c'](char) is True]
        try:
            string = fsm_map[index[0]]['proc'](char,string)
            if type(string) == tuple:
                if len(string) == 2:
                    words.append(string[1])
                    string = ''
                    k=k+1
                if len(string) == 3:
                    words.append(string[1])
                    string = ''
            else:
                k=k+1
            start = fsm_map[index[0]]['q2']
        except:
            return 0, "Error in line " + str(k)
        
    return words, words.count('('), words.count(')'), words.count('{'), words.count('}')    


def make_NameTable_and_InternalRepresent(file_name):
    brackets_11 = 0
    brackets_12 = 0
    brackets_21 = 0
    brackets_22 = 0
    f = open(file_name)
    k=0
    number=100
    name_table = {}
    int_rep = []
    array = [] 
    l=1
    try:
        while l:
            l = f.readline()
            words, br_11, br_12, br_21, br_22 = do_rule(FSM_MAP, l)
            brackets_11 = brackets_11 + br_11
            brackets_12 = brackets_12 + br_12
            brackets_21 = brackets_21 + br_21
            brackets_22 = brackets_22 + br_22
            for i in words:
                if i in name_table.keys():
                    array.append(name_table.get(i)[0])
                else:
                    if i in res_words.keys():
                        name_table[i] = res_words.get(i)
                    else:
                        try:
                            try:
                                int(i)
                                type_ = 'const, int'
                            except:
                                float(i)
                                type_ = 'const, float'
                        except:
                            if i[-1]==':':
                                type_ = 'label'
                            else: 
                                type_ = 'string'
                        name_table[i] = [number, 'identifier, type:' + type_]
                        number = number + 1
                    array.append(name_table.get(i)[0])
            int_rep.append(array)
            array = []
    except:
        return do_rule(FSM_MAP, l)[1]
    if brackets_11 != brackets_12:
        print('Error with count of brackets ( )') 
    if brackets_21 != brackets_22:
        print('Error with count of brackets { }') 
    return name_table, int_rep 
	

def write_to_files(name_table, int_rep, name_table_file, int_rep_file):
    f1 = open(name_table_file, "w")
    for i in range(len(name_table)):
        f1.write(str(list(name_table.keys())[i]) + ' ' + str(list(name_table.values())[i]))
        f1.write('\n')
    f = open(int_rep_file, "w+")
    for i in range(len(int_rep)):
        for k in range(len(int_rep[i])):
            f.write(str(int_rep[i][k]) + ' ')
        f.write('\n')

        
def main():
    c_file = sys.argv[1]
    name_table_file = sys.argv[2]
    txt_file = sys.argv[3]
    try:
        write_to_files(make_NameTable_and_InternalRepresent(c_file)[0], 
					   make_NameTable_and_InternalRepresent(c_file)[1],
					   name_table_file, 
					   txt_file)
    except:
        print(make_NameTable_and_InternalRepresent(c_file))

if  __name__ ==  "__main__" :
    main()
#example of usage: python scaner.py main.c name_space.txt int_rep.txt
