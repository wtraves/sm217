#!/usr/bin/env python
# coding: utf-8

# ## SEAL GRADER: An automated grading system
# By Prof. Will Traves (USNA)
#  
# STEP A: 
# To use the autograder, first make a folder and store the following files in that folder:   
# (1) This file  
# (2) The ...SOLUTIONS.ipynb file to the assignment  
# (3) The ...LASTNAME(S).ipynb file to the assignment  
# (4) The downloaded student ....ipynb files from Blackboard  
# (5) A blank Excel file called grading_data.xlsx  
# (6) An Excel file containing the word Alphas in cell A1 and the alphas of midshipmen in your class in cells A2 and below. It is best if this file also contains the first names of the midshipmen in column C (starting in C2). Or you can enter MIDN Jones in that cell if you address MIDN Felix Jones as MIDN Jones. CAREFUL: The autograder will eventually overwrite any material in column B next to the alphas.   
# 
# STEP B: 
# Open both files (5) and (6) and run the cell below. 
# 
# The autograder will populate the grading_data.xlsx file with various data. Most of this includes material that is already
# graded but it will also include questions that need to be manually graded. These tend to be text answers that can't be 
# easily graded by the computer or pictures (e.g. a histogram). You'll need to complete the rows in the spreadsheet labeled
# q...:credit by assigning a grade to each of these questions. When you first look at the spreadsheet after allowing the 
# autograder to complete writing to the file, type CTRL-A (to select all) and then hit the button for WRAP TEXT (roughly about
# 40% of the way to the right, on the Home ribbon.) Save the completed Excel file. 
# 
# STEP C: 
# Replace ... in the next cell with your Excel file's name (file 6, above) where you want the grades to be written. Run
# the cell and wait for your grades to appear in the proper location. 

# In[10]:


import matplotlib
matplotlib.use('Agg')
from datascience import *
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
import os as os
import xlwings as xw
import nbformat
import math
import statsmodels.api as sm 
from scipy.stats import binom

def ellipses_present(s):
    """return True if ... is in a non-commented part of the code string s"""
    s1 = s.split('\n') # one element for eachc line in the string s
    s2 = [p.split('#')[0] for p in s1] # replace each line with the part of the string to the left of the # 
    s3 = ['...' in p for p in s2] # element will be True if ... present
    return any(s3)

def seal_grader(single_file=None):
    """ Runs the autograder. This file should be in the same directory as the two input files and the 
    assignments downloaded from Blackboard.
    
    Grades will appear in mids_file (first Column should have header Alphas and mids alphas
    should appear below in the order that is convenient for gradebook entry).  
    
    The file spreadsheet_file is an Excel file with responses available for fast manual grading. It will include 
    all the automatically graded questions too. 
    
    If you want to run the autograder on all the files in the current directory, don't enter any arguments. If you 
    only want to run the autograder on a single file, then enter the file name in quotes (file name only, no directory info). 
    """
    
    current_working_directory = os.getcwd()
    spreadsheet_file = current_working_directory+'\\grading_data.xlsx'
    wbss = xw.Book(spreadsheet_file)
    sht = wbss.sheets[0]
    
    if single_file == None:
        list_of_nbs = [f for f in os.listdir(current_working_directory) if f[-5:]=='ipynb' 
                       and f.rfind('LASTNAME')<0 and f.rfind('SOLUTIONS')<0 and len(f)>50 
                       and f.rfind('grader')<0 and f.rfind('LitC')<0]
    else: 
        list_of_nbs = [current_working_directory+"\\"+single_file]
    solutions_file = [f for f in os.listdir(current_working_directory) if f.rfind('SOLUTIONS')>=0][0]
    gi = get_answers(solutions_file)
    set_up_spreadsheet(spreadsheet_file,gi)
    current_cell = 'C2'
    
    skip_files = []
    for response_file in list_of_nbs:
        try:
            gr = get_responses(response_file,gi)
            process_responses(gr,gi,spreadsheet_file,current_cell)
            update_cell = sht.range(current_cell).offset(0,1)
            cola = str(update_cell).split('$')[1]
            rowa = str(update_cell).split('$')[2][:-1]
            current_cell = cola+rowa
        except:
            print(f"RAN INTO SERIOUS ERROR IN {response_file}. SKIPPING file and continuing.")
            skip_files.append(response_file)
            
    if len(skip_files)>0:
        for response_file in skip_files:
            print(f'We skipped {response_file} in grading.')
            
def tally_points(mids_file):
    print("Gathering grading data.")
    current_working_directory = os.getcwd()
    spreadsheet_file = current_working_directory+'\\grading_data.xlsx'
    mids_grades = {}
    wb = xw.Book(spreadsheet_file)
    sht = wb.sheets[0]
    titles = sht.range('A2').expand('down')
    offs_list_for_credit = []
    rng = sht.range('A2')
    for offs in range(len(titles)):
        title = rng.offset(offs,0).value.split(":")
        if len(title)==1:
            if title[0]=='Subtotal':
                offs_subtotal = offs
            elif title[0]=='Early bonus':
                offs_early_bonus = offs
            elif title[0]=='Late penalty':
                offs_late_penalty = offs
            elif title[0]=='Total':
                offs_total = offs
        elif len(title)==2:
            if title[1]=='credit':
                offs_list_for_credit.append(offs)
    rng = sht.range('C2').expand('right')
    num_submissions = len(rng)
    print("Tallying grades on grading document.")
    rng = sht.range('C2')
    for subm in range(num_submissions):
        cred = 0
        for offs in offs_list_for_credit:
            cred += rng.offset(offs,subm).value
        cred += rng.offset(offs_early_bonus,subm).value
        rng.offset(offs_subtotal,subm).value = cred
        if rng.offset(offs_late_penalty,subm).value=='no penalty' or rng.offset(offs_late_penalty,subm).value==0:
            rng.offset(offs_late_penalty,subm).value=0
        else:
            rng.offset(offs_late_penalty,subm).value=-0.25*cred
            cred = 0.75*cred
        rng.offset(offs_total,subm).value=cred
        for alpha in eval(rng.offset(0,subm).value):
            mids_grades[str(alpha)] = cred
    print("Printing grades to spreadsheet.")
    wb2 = xw.Book(mids_file)
    sht2 = wb2.sheets[0]
    alphas_list = sht2.range('A2').expand('down').value # note: this breaks if there is only 1 person in the class list
    alphas_list = [str(int(alpha)) for alpha in alphas_list]
    grades_list = sht2.range('B2',f'B{1+len(alphas_list)}').value
    alphas_in_grades = [str(alpha) for alpha in list(mids_grades.keys())]
    for i in range(len(alphas_list)):
        if alphas_list[i] in alphas_in_grades: # need to update grade
            grades_list[i]= mids_grades[alphas_list[i]]
    solutions_file = [f for f in os.listdir(current_working_directory) if f.rfind('SOLUTIONS')>=0][0]
    assn_name = solutions_file.split("-")[0]
    sht2.range('B1').value = assn_name + "/" + str(int(sht.range('A2').offset(offs_total,1).value))
    grades_list = [[gr] for gr in grades_list]
    sht2.range('B2').value = grades_list

    

def short_string(instring):
    if len(instring)<600:
        return instring
    else:
        return instring[:300]+" ... "+instring[-300:]
    
def process_responses(responses,grading_information,file,current_cell):
    """ Process student responses, storing in a spreadsheet for further work """
    wb = xw.Book(file)
    sht = wb.sheets[0]
    rng = sht.range(current_cell)
    rng.column_width=25
    rng.value = str(responses['alphas'])
    gik = list(responses.keys())
    gik.remove('alphas')
    gik.remove('early')
    gik.remove('late')
    num_questions = max([int(num) for num in gik])
    for i in range(1,num_questions+1):
        rng = rng.offset(1,0)
        rng.value = responses[str(i)]['credit']
        rng = rng.offset(1,0)
        rng.value = responses[str(i)]['points']
        if 'answer' in grading_information[str(i)].keys():
            rng = rng.offset(1,0)
            rng.value = short_string(str(responses[str(i)]['response']))
        if 'picture' in grading_information[str(i)]['type']:
            rng = rng.offset(1,0)
            rng.row_height=130
            if responses[str(i)]['response_file'] != "no answer":
                sht.pictures.add(responses[str(i)]['response_file'], top=rng.top+5, left=rng.left+5,height=120,width=120)
        if 'code' in responses[str(i)].keys():
            rng = rng.offset(1,0)
            rng.value = str(responses[str(i)]['code'])
        rng = rng.offset(1,0) # skip down to avoid writing in the feedback cell
    rng = rng.offset(1,0)
    rng.value = int(responses['early']) # 1 bonus point if early
    rng = rng.offset(1,0)
    rng.value = 'Subtotal'
    rng = rng.offset(1,0)
    if responses['late']:
        late_multiplier = '-25 percent'
    else:
        late_multiplier = 'no penalty'
    rng.value = late_multiplier
    rng = rng.offset(1,0)
    rng.value = 'Total'
    
def set_up_spreadsheet(file,grading_information):
    """ Set up the spreadsheet to receive grades data """
    wb = xw.Book(file)
    sht = wb.sheets[0]
    rng = sht.range('A1')
    rng.column_width=12
    rng.offset(0,1).column_width=28
    rng.value = 'Row value'
    rng.offset(0,1).value = 'Solutions'
    rng = rng.offset(1,0)
    rng.value = 'Alphas'
    gik = list(grading_information.keys())
    gik.remove('dates')
    num_questions = max([int(num) for num in gik])
    total_score = 0
    for i in range(1,num_questions+1):
        print(f'Setting up spreadsheet: Question {i}')
        rng = rng.offset(1,0)
        rng.value = f'q{str(i)}:credit'
        rng = rng.offset(1,0)
        rng.value = f'q{str(i)}:points'
        rng.offset(0,1).value = grading_information[str(i)]['points']
        total_score += grading_information[str(i)]['points']
        if 'answer' in grading_information[str(i)].keys():
            rng = rng.offset(1,0)
            rng.value = f'q{str(i)}:answer'
            rng.offset(0,1).value = str(grading_information[str(i)]['answer'])
        if 'picture' in grading_information[str(i)]['type']:
            rng = rng.offset(1,0)
            rng.value = f'q{str(i)}:answer'
            rng.offset(0,1).row_height=130
            rng.offset(0,1).column_width=25
            sht.pictures.add(grading_information[str(i)]['file'], top=rng.offset(0,1).top+5, left=rng.offset(0,1).left+5,height=120,width=120)
        if 'code' in grading_information[str(i)].keys():
            rng = rng.offset(1,0)
            rng.value = f'q{str(i)}:code'
            rng.offset(0,1).value = str(grading_information[str(i)]['code'])
        rng = rng.offset(1,0)
        rng.value = f'q{str(i)}:feedback'
    rng = rng.offset(1,0)
    rng.value = 'Early bonus'
    rng = rng.offset(1,0)
    rng.value = 'Subtotal'
    rng = rng.offset(1,0)
    rng.value = 'Late penalty'
    rng = rng.offset(1,0)
    rng.value = 'Total'
    rng.offset(0,1).value = total_score
    rng = rng.offset(1,0)
    rng.value = 'Feedback'

    
def get_date_from_file(file_name):
    """return month and day of submission e.g. (3,12) for March 12""" 
    date = file_name.split("_")[3][:10]
    return (int(date[5:7]),int(date[8:]))

def is_early(file_name,early_date):
    """return true if the file was submitted any time on or before the end of early_date"""
    return get_date_from_file(file_name)[0]<early_date[0] or (get_date_from_file(file_name)[0]==early_date[0] and get_date_from_file(file_name)[1]<=early_date[1])
def is_late(file_name,late_after):
    """return true if the file was submitted any time after the late_after date"""
    date = get_date_from_file(file_name)
    return date[0]>late_after[0] or (date[0]==late_after[0]  and date[1]>late_after[1])

def get_responses(file,grading_instructions):
    """ returns a dictionary with information about the student's responses """
    global credit
    print(f'Getting responses from {file}.')
    my_notebook = nbformat.read(file, as_version=4) 
    response_information = {}
    response_information['early']=is_early(file,grading_instructions['dates']['early_date'])
    response_information['late']=is_late(file,grading_instructions['dates']['late_after'])
    
    num_cells = len(my_notebook.cells) # number of cells in the notebook
    for cell_num in range(num_cells):
        cell = my_notebook.cells[cell_num]
        if 'tags' in cell['metadata'].keys():    # first check that there *are* tags on the cell            
            tags = cell['metadata']['tags']
            if ellipses_present(cell['source']):
                        pass
            else: 
                varnamelist = [t[7:] for t in [ts for ts in tags if len(ts)>=7] if t[:7]=='_track:'] 
                if len(varnamelist)>0: # need to track at least one variable
                    for varname in varnamelist:
                        pre = f'global {varname}\n'
                        try: 
                            exec(pre + cell['source'],globals(),locals()) 
                        except:
                            pass   
            # see if there is a qxx tag on the cell
            qlist = [q[1:] for q in tags if q[0]=='q']
            if len(qlist)>0:
                qnum = qlist[0]
            else:
                qnum = None
            if '_alphas' in tags: # get list of midshipmen's alphas
                global alphas
                alphas = []
                if ellipses_present(cell['source']): 
                    alphas = [100001] # code for no alphas entered
                else:
                    exec("global alphas\n"+cell['source'],globals(),locals())
                response_information['alphas'] = globals()['alphas']
                print(f"Processing submission by MIDN in {response_information['alphas']}")
            elif 'skip' in tags and qnum == None: # then check for a skip tag; use this to pass on running cells that produce errors
                # for student answer cells we'll remove those tags when we make the lastnames file
                pass
            elif qnum != None: 
                qtype = grading_instructions[qnum]['type']
                if qtype == 'special-code':
                    pts = grading_instructions[qnum]['points']
                    if cell['cell_type']=='code':
                        try: 
                            exec(cell['source'],globals(),locals())
                        except:
                            pass
                    try: 
                        exec(grading_instructions[qnum]['code_for_credit'],globals(),locals())
                        credit = globals()['credit']
                    except:
                        credit = 0
                    response_information[qnum] = {'type': qtype, 'credit': credit, 'points': pts, 'code': cell['source']}
                elif qtype == 'markdown':
                    response = cell['source'].strip()
                    answer = grading_instructions[qnum]['answer'].strip()
                    pts = grading_instructions[qnum]['points']
                    if values_equal(answer,response):
                        credit = pts
                    else:
                        credit = 0
                    response_information[qnum] = {'type': qtype, 'credit': credit, 'points': pts, 
                                                  'response': response, 'answer': answer } # no code for markdown cells
                elif qtype == 'stdoutput':
                    outformat = grading_instructions[qnum]['outformat']
                    try:
                        response = cell['outputs'][0][outformat]
                    except:
                        response = "answer produces an error"
                    newformat = grading_instructions[qnum]['newformat']
                    if newformat != None:
                        try:
                            response = eval(f"{newformat}({response})")
                        except:
                            response = "answer produces an error"
                    pts = grading_instructions[qnum]['points']
                    answer = grading_instructions[qnum]['answer']
                    if values_equal(response,answer):
                        credit = pts
                    else:
                        credit = 0
                    response_information[qnum] = {'type': qtype, 'credit': credit, 'points': pts, 
                                                  'response': response, 'answer': answer, 'code': cell['source'] }
                elif qtype == 'picture':
                    pts = grading_instructions[qnum]['points']
                    answer_file = grading_instructions[qnum]['file']
                    try: 
                        exec(cell['source']) # produce response figure
                        pic_file = answer_file[:-4]+str(alphas)+".png"
                        execstr = "matplotlib.pyplot.savefig(f'{pic_file}',pad_inches=0.1,bbox_inches='tight')"
                        exec(execstr) # save image to picfile
                    except:
                        pic_file = "no answer"
                    response_information[qnum] = {'type': qtype, 'credit': 0, 'points': pts, 
                                                  'response_file': pic_file , 'answer_file': answer_file,
                                                   'code': cell['source']}
                elif qtype == 'var':
                    pts = grading_instructions[qnum]['points']
                    varname = grading_instructions[qnum]['varname']
                    answer = grading_instructions[qnum]['answer']
                    try:
                        exec("global "+varname+"\n"+cell['source'],globals(),locals())
                        response = globals()[varname]
                        if gradeq(response,answer):
                            credit = pts
                        else:
                            credit = 0
                    except:
                        credit = 0
                    response_information[qnum] = {'type': qtype, 'credit': credit, 'points': pts, 
                                                  'response': response, 'answer': answer, 'varname': varname,
                                                 'code': cell['source']}
            else: 
                if cell['cell_type'] == 'code': # just run the cell
                    if ellipses_present(cell['source']):
                        pass
                    else:
                        exec(cell['source'])
    return response_information

def get_answers(file):
    """ returns a dictionary with important information about the answers and how to process the student submissions """ 
    my_notebook = nbformat.read(file, as_version=4) 
    grading_instructions = {}
    for cell in my_notebook.cells:
        if 'tags' in cell['metadata'].keys():    # first check that there *are* tags on the cell            
            tags = cell['metadata']['tags']
            varnamelist = [t[7:] for t in [ts for ts in tags if len(ts)>=7] if t[:7]=='_track:'] 
            if len(varnamelist)>0: # need to track at least one variable
                for varname in varnamelist: 
                    pre = f'global {varname}\n'
                    try: 
                        exec(pre + cell['source'],globals(),locals()) # I'm not convinced this works when varname is a function
                    except:
                        print(f"COULDN'T DEFINE {varname}.")
                        pass
            if 'skip' in tags: # then check for a skip tag; use this to pass on running cells that produce errors
                # or to pass on cells that have ellipses (for student answers or alphas, though we'll remove those tags when 
                # we make the lastnames file)
                pass
            elif 'special-code' in tags:
                qnum = [qs[1:] for qs in tags if qs[0]=='a'][0]
                pts =  int([ps[1:] for ps in tags if ps[0]=='p'][0])
                code_string = cell['source']
                grading_instructions[qnum] = {'type': 'special-code', 'points': pts, 'code_for_credit': code_string, 'code': code_string}
                # for special code, run the cells up to and including the cell tagged qxx in the LASTNAMES file and then 
                # execute the code_for_credit code; then variable credit will have the correct value for the question
            elif len([ass for ass in tags if ass[0]=='a'])>0: # tagged axx
                if '_markdown' in tags: # in this case we want to store the text in the markdown cell as our answer
                    qnum = [qs[1:] for qs in tags if qs[0]=='a'][0]
                    pts =  int([ps[1:] for ps in tags if ps[0]=='p'][0])
                    answer = cell['source']
                    grading_instructions[qnum] = {'type': 'markdown', 'points': pts, 'answer': answer} # no code for a markdown cell
                elif '_stdoutput' in tags: # in this case we want to compare the mid answer to the output itself
                    # get the output format from the tags (this only works for some kinds of output, e.g. print statements)
                    outformat = [of[8:] for of in tags if of[:8]=='_format:'][0]
                    answer = cell['outputs'][0][outformat]
                    # determine if the text answer needs to be in a different format (e.g. an int or float)
                    # if so, then use tag e.g. _newformat:int
                    newformat = None
                    newformatlist = [nf[11:] for nf in tags if nf[:8]=='_newformat:']
                    if len(newformatlist)>0:
                        newformat = newformatlist[0]
                        answer = eval(f"{newformat}({answer})")
                    qnum = [qs[1:] for qs in tags if qs[0]=='a'][0]
                    pts =  int([ps[1:] for ps in tags if ps[0]=='p'][0])
                    grading_instructions[qnum] = {'type': 'stdoutput', 'points': pts, 'outformat': outformat, 
                                                  'newformat': newformat, 'answer': answer, 'code': cell['source']}
                elif '_picture' in tags: # in this case we want to capture the current figure and save it to the 
                    # excel spreadsheet
                    qnum = [qs[1:] for qs in tags if qs[0]=='a'][0]
                    pts =  int([ps[1:] for ps in tags if ps[0]=='p'][0])
                    exec(cell['source']) # run the answer cell -- producing the figure
                    cwd = os.getcwd()
                    execstr = "matplotlib.pyplot.savefig(f'{cwd}\\\\ans{qnum}.png',pad_inches=0.1,bbox_inches='tight')" 
                    exec(execstr)
                    grading_instructions[qnum] = {'type': 'picture', 'points': pts, 'file': f'{cwd}\\\\ans{qnum}.png', 
                                                  'code': cell['source']}
                elif '_var' in tags: # in this case we want to run code and obtain the variable as our answer
                    qnum = [qs[1:] for qs in tags if qs[0]=='a'][0]
                    pts =  int([ps[1:] for ps in tags if ps[0]=='p'][0])
                    # get varname from _varname:... tag
                    varname = [vn[9:] for vn in tags if vn[:9]=='_varname:'][0]
                    try:
                        pre = f'global {varname}\n'
                        exec(pre + cell['source'],globals(),locals())
                        answer = globals()[f'{varname}']
                    except:
                        print(f"FAILED TO EXECUTE CODE DEFINING {varname}")
                        answer = None
                    grading_instructions[qnum] = {'type': 'var', 'points': pts, 'varname': varname, 'answer': answer, 'code': cell['source']}
            elif len([qs for qs in tags if qs[0]=='q'])>0: # tagged qxx
                pass
            elif '_alphas' in tags:
                pass
            elif '_date' in tags: 
                early_date = (1,1)
                late_after = (12,31)
                exec(cell['source'],globals(),locals())
                early_date = globals()['early_date']
                late_after = globals()['late_after']
                grading_instructions['dates']={'early_date': early_date, 'late_after': late_after}
            elif cell['cell_type'] == 'code': # just run the cell
                exec(cell['source'],globals(),locals())
                
    return grading_instructions

def gradeq(response,answer):
    if type(response)==type(type(3)): # type
        return values_equal(response,answer)
    if type(response)==type(""): # string
        return values_equal(response,answer)
    elif type(response)==type(3): # integer
        return values_equal(response,answer)
    elif type(response)==type(3.0): #float
        return values_equal_float(response,answer)
    elif type(response)== np.float32: #float32
        return values_equal_float(response,answer)
    elif type(response)== np.float64: #float64
        return values_equal_float(response,answer)
    elif type(response)==type([1]): #list
        return lists_equal(response,answer)
    elif type(response)==type(make_array(1,2)): #array
        return arrays_equal(response,answer)
    elif type(response)==type((1,2)): #tuple
        return arrays_equal(response,answer)
    elif type(response)==type(Table()): #table
        return tables_equal(response,answer)
    elif type(response)==np.int64: #int64
        return values_equal(response,answer)
    elif type(response)==np.int32: #int32
        return values_equal(response,answer)
    elif type(response)==np.str_: # a string from a numpy array
        return values_equal(response,answer)
    elif type(response)==type(True):
        return values_equal(response,answer)
    elif type(response)==np.bool_: # a Boolean in a numpy array
        return values_equal(response,answer)
    else:
        raise ValueError()

def values_equal_float(value0,value1,tol=10**(-8)):
    """ return True if the two values are equal up to tol. """
    return abs(value0-value1)<tol

def values_equal(value0,value1):
    """ return True if the two values are equal. Works equally well on strings and numbers."""
    return value0==value1

def lists_equal(list0,list1):
    """ Test if two lists have all their elements equal. """
    if len(list0) != len(list1):
        value = False
    else:
        value = True
        for i in range(len(list0)):  # loop over all columns and ensure that they are the same
            value = value and gradeq(list0[i],list1[i])
    return value

def arrays_equal(array0,array1):
    """ Test if two arrays have all their elements equal. """
    if len(array0) != len(array1):
        value = False
    else:
        value = True
        for i in range(len(array0)):  # loop over all columns and ensure that they are the same
            value = value and gradeq(array0[i],array1[i])
    return value

def tables_equal(table0,table1,row0=0,row1=None):
    """Check if the rows in row0:row1 of two tables are equal. Column labels need not be equal, we check values only."""
    # subset tables:
    if row1==None: # if no endpoint, go to the end of the table
        table0 = table0.take(range(row0,table0.num_rows))
        table1 = table1.take(range(row0,table1.num_rows))
    else:
        table0 = table0.take(range(row0,row1))
        table1 = table1.take(range(row0,row1))
    r0 = table0.num_rows
    r1 = table1.num_rows
    if r0 != r1:   # check the two tables have the same number of rows
        value = False
    else:
        columns0 = table0.columns
        columns1 = table1.columns
        if len(columns0) != len(columns1): # check the two tables have the same number of columns
            values = False
        else: 
            value = True
            for i in range(len(columns0)):  # loop over all columns and ensure that they are the same
                value = value and gradeq(columns0[i],columns1[i])
    return value

def make_credit_yellow():
    current_working_directory = os.getcwd()
    spreadsheet_file = current_working_directory+'\\grading_data.xlsx'
    wbss = xw.Book(spreadsheet_file)
    sht = wbss.sheets[0]
    # Initialize a blank list of row indices
    row_idx_list = []
    # Create a range starting at A3 and expanding down the entire
    # column where there is data
    my_range = sht.range('A3').expand('down') 
    for i in range(len(my_range)):
        # First check to see if the cell contains a :
        if ':' in my_range[i].value:
            # If the cell contains a : see if credit is after the :
            if my_range[i].value.split(':')[1] == 'credit':
                # Append row index to the list row_idx_list
                row_idx_list.append(i)

    # Now loop over all the rows in row_idx_list
    for i in row_idx_list:
        # Set the rows in columns A and B to yellow if the
        # cell is a credit cell.  Note the plus 3 because
        # we technically start in row 3, but row_idx_list
        # starts with a zero index.
        sht.range(f'A{i+3}').color = (255,255,0)
        sht.range(f'B{i+3}').color = (255,255,0)
        # Do the same thing for column C, but now expand it
        # to the right to get ALL student submission rows to
        # be yellow as well.
        sht.range(f'C{i+3}').expand('right').color = (255,255,0)        

seal_grader()
print("Making all the credit rows yellow.")
make_credit_yellow()


# In[18]:


file = 'JASMINE-COX, [23,24]'
file[file.find(',')+2:]
rng.offset(0,subm).value[rng.offset(0,subm).value.find(',')+2:]


# In[15]:


# replace ... below with the file address of the gradebook where you'll write the grades (file 6 in the instructions)
tally_points("Gradebook Section 4002.xlsx")


# ## Appendix: Setting up an Assignment
# 
# In this appendix, I'll explain how to set up an assignment for use with the autograder. I assume that your assignment roughly follows the examples from SM219 in Spring 2020. Most importantly, your assignment is in an ipynb file with 
# LASTNAMES in the file name (for the student version) and SOLUTIONS in the ipynb file containing the solutions. 
# 
# When making the SOLUTIONS file, I always write the cell that I'll ask the midshipmen to complete (often
# pre-filled with some code and ... for places they need to add code). I then follow that cell with a similar cell containing my solution. Sometimes we sandwich a third cell between these two cells, as explained below. 
# 
# In any case, we add *tags* to each of these cells (and some others). To add tags, click on View and select Cell Toolbar. Then select Tags. When the cell collects the midshipmen's alpha codes, we tag it with \_alphas (that is the underscore followed by alphas). That cell should look like: 
# 

# In[ ]:


global alphas # leave this line alone but replace the ... in the following line with your alpha numbers
alphas = [...,...,...]


# I always include a cell tagged \_date with the early date (if midshipmen turn in the assignment by 2359 on the early date then they earn 1 bonus point) and the due date (called late\_after). If midshipmen turn in the assignment past 2359 on that date they lose 25% of the points they earned. Dates are recorded as (month, day) so that Jan 15 is (1,15). Here's an example:

# In[ ]:


global early_date
global late_after
early_date = (1,15)
late_after = (1,17)


# Some cells should be skipped by the autograder. For example, the cells might deliberately produce an error (e.g. to show midshipmen the way to read the error message). Such cells should not be executed by the autograder. We tag those cells with the skip tag. 
# 
# Cells containing the code that should be evaluated to assess the student answer (usually a code cell with ...'s) should be tagged qx or qxx, where x or xx stands for the question number. For some reason I always start the question numbering at 1 though I really ought to start at 0 to obey our Python overlords. 
# 
# Cells with answers should be tagged ax or axx (with x or xx giving the question number). They should also be tagged px and pxx (with the x or xx giving the number of points the answer is worth). Furthermore, the cell should have an additional tag. 
# Use \_markdown if the answer is a markdown cell (e.g. edit a markdown cell to make an answer). Use \_stdoutput and \_format:text if the answer is given by the (text) output of the answer cell. the \_format:xx tag is used to show the format of the output but you can use the \_newformat:xx tag to give another format you want the answer in (e.g. int from a string answer). Use \_picture if the answer is a picture produced by the cell's code (e.g. a histogram). Use \_var and \_varname:xx (where xx is a variable name) if the answer is the value of variable xx after running the answer cell's code. [Currently we can only track one variable per cell and we need both the _var and _varname:xx tags; it would be better to just have to use the _varname:xx tag.]
# 
# Sometimes there is a variable produced in one cell that you want to use in another cell but not a variable that is being checked using a \_var tag. In that case, use a \_track:varname tag, where varname is the variable name you'd like to continue to store. This is particularly usefull in cells where we load a table for later use. You need to put this tag on both the qxx and axx cells if you need to track in both the student answers and solutions (as you usually do). 
# 
# Sometimes we need to give special instructions on how to grade a question. For example, we might want to give partial credit or we might want to look in an unusual place for the answer (e.g. looking at two different variable values or using code spread out over two different cells). In this case, we sandwich a code cell between the question cell and the answer cell with the tag special-code. That cell should contain the code *global credit* and the credit variable should be assigned in the cell. You can use cell\_num to refer to the current cell (the cell tagged qxx) and cell\_num-1 to refer to the previous cell, etc. In accessing portions of the cells, you'll probably want to know how the cell's code appears when it is being read by the seal_grader program. The program uses the nbformat library. Use the following code to print out the 11th cell in the file "SOLUTIONS.ipynb".

# In[3]:


import nbformat
my_notebook = nbformat.read(".\\LAB09 - SOLUTIONS.ipynb", as_version=4)
print(my_notebook.cells[18]['source'])


# After tagging all cells, I make a copy of the SOLUTIONS file and rename it LASTNAME. In the LASTNAME file I cut all the cells with special instructions or answers to the questions. I also cut the date cell and clear all output. Then hide tags and save the file for the midshipmen. 
