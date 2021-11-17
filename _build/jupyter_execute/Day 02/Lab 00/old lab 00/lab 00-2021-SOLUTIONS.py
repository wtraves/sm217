#!/usr/bin/env python
# coding: utf-8

# <span class='note'><i>Make me look good.</i> Click on the cell below and press <kbd>Ctrl</kbd>+<kbd>Enter</kbd>.</span>

# In[1]:


import warnings
warnings.simplefilter('ignore', FutureWarning)
from IPython.core.display import HTML
HTML('''<link href='http://fonts.googleapis.com/css?family=Lora:400,700,400i,700i' rel='stylesheet'><link href='https://fonts.googleapis.com/css?family=Lato:300,400,700,300i,400i,700i' rel='stylesheet'><link href='https://fonts.googleapis.com/css?family=Inconsolata:400' rel='stylesheet'><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"><style>h1, h2, h3, h4, h5 { font-family: 'Lato', sans-serif; } h5 { font-style: normal; } kbd { font-family: Lato, serif; } hr { border-width: 2px; border-color: #a9a9a9; } .cite { font-size: 85%; text-align: right; margin-top: 10px; } .note { font-family: Lora, serif; font-size: 10pt; font-weight: 400; margin-top: 0; margin-bottom: 0; } h5.prehead { font-family: Lato, serif; font-style: normal; font-size: 14pt; font-weight: 300; margin-bottom: 15px; margin-top: 30px; } h5.lesson { font-family: Lato, serif; font-weight: 400; font-size: 15pt; font-style: normal; margin-top: 0px; margin-bottom: 5px; } h1.lesson_title { font-family: Lato, serif; font-weight: 300; font-size: 32pt; line-height: 110%; color:#CD2305; margin-top: 0px; margin-bottom: 15px; } div.cell{ max-width: 1120px; margin-left: auto; margin-right: auto; } div.text_cell_render { font-family: Lora, serif; line-height: 160%; font-size: 13pt; } .rendered_html pre, .rendered_html code  { font-family: Inconsolata, monospace !important; font-size: 13pt; } div.CodeMirror, div.output_area pre, div.prompt { font-family: Inconsolata, monospace !important; font-size: 125%; } .rendered_html ul li { margin-top: 0.75em; margin-bottom: 0.75em; } .rendered_html ul li ul li { margin-top: 0.5em; margin-bottom: 0.5em; } .rred { color: #a00000; } </style> <script> MathJax.Hub.Config({ TeX: { extensions: ["AMSmath.js"] }, tex2jax: { inlineMath: [ ['$','$'], ["\\(","\\)"] ], displayMath: [ ['$$','$$'], ["\\[","\\]"] ] }, displayAlign: 'center', // Change this to 'center' to center equations. "HTML-CSS": { styles: {'.MathJax_Display': {"margin": "0.75em 0"}} } }); </script>''')


# # Lab 00: Your First Data Science Notebook
# 
# You will often complete lab assignments like this one.  You can't learn technical subjects without hands-on practice, so labs are an important part of the course. This lab is due by 2359 on 30 AUG. You will get a bonus point if you submit by 2359 on 29 AUG.
# 
# Collaborating on labs is more than okay -- it's encouraged! We'll work in groups of two or three midshipmen. You should each type answers on your own laptop. Just watching someone else type is not going to help you as much as entering things on your own. You'll often submit just one file for your entire group though. You should rarely be stuck for more than a few minutes on questions in labs, so ask the instructor for help if you need it. (Explaining things is beneficial, too -- the best way to solidify your knowledge of a subject is to explain it.) 
# 
# 
# #### Today's lab
# 
# In today's lab, you'll learn how to:
# 
# 1. navigate Jupyter notebooks (like this one);
# 2. evaluate and evaluate some basic *expressions* in Python, the computer language of the course;
# 3. call *functions* to use code other people have written, and 
# 4. break computations down into smaller parts to make them more manageable. 
# 
# This lab covers parts of [Chapter 3](http://www.inferentialthinking.com/chapters/03/programming-in-python.html) of the online textbook. Think of this lab as an introduction to that material. You should read the book, but not right now. Instead, let's get started!

# In[2]:


global early_date
global late_after
early_date = (8,29)
late_after =  (8,30)


# # 1. Jupyter notebooks
# This webpage is called a Jupyter notebook. A notebook is a place to write programs and view their results.
# 
# ## 1.1. Text cells
# In a notebook, each rectangle containing text or code is called a *cell*.
# 
# Text cells (like this one) can be edited by double-clicking on them. They're written in a simple format called [Markdown](http://daringfireball.net/projects/markdown/syntax) to add formatting and section headings.  You don't need to learn Markdown, but you might want to.
# 
# After you edit a text cell, click the "run cell" button at the top that looks like ▶| to confirm any changes. (Try not to delete the instructions of the lab.)

# **Question 1. (1 pt)** This paragraph is in its own text cell.  Try editing it so that this sentence is the last sentence in the paragraph, and then click the "run cell" ▶| button.  This sentence, for example, should be deleted. So should this one. 

# **Question 1. (1 pt)** This paragraph is in its own text cell.  Try editing it so that this sentence is the last sentence in the paragraph, and then click the "run cell" ▶| button.

# ## 1.2. Code cells
# Other cells contain code in the Python 3 language. Running a code cell will execute all of the code it contains.
# 
# To run the code in a code cell, first click on that cell to activate it.  It'll be highlighted with a little green or blue rectangle.  Next, either press the symbol on the left that looks like the picture on the "run cell" button or hold down the `shift` key and press `return` or `enter`.
# 
# Try running this cell:

# In[3]:


print("Hello, World!")


# Notice that you need to put a pair of double quotes around text that you want to print. 
# 
# The fundamental building block of Python code is an expression. Cells can contain multiple lines with multiple expressions. When you run a cell, the lines of code are executed in the order in which they appear. Every `print` expression prints a line. Run the next cell and notice the order of the output.

# In[4]:


print("First this line is printed,")
print("and then this one.")


# **Question 2. (1 pt)** Change the cell above so that it prints out:
# 
#     First this line is printed,
#     then the whole shebang,
#     and then this one.
# 
# *Hint:* If you're stuck on this problem for more than a few minutes, try talking to a neighbor or the instructor.  That's a good idea for any lab problem.

# In[5]:


print("First this line is printed,")
print("then the whole shebang,")
print("and then this one.")


# ## 1.3. Writing Jupyter notebooks
# You can use Jupyter notebooks for your own projects or documents.  When you make your own notebook, you'll need to create your own cells for text and code.
# 
# To add a cell, click the + button in the menu bar.  It'll start out as a code cell.  You can change it to a text cell by clicking inside it so it's highlighted, clicking the drop-down box next to the restart (⟳) button in the menu bar, and choosing "Markdown".
# 
# **Question 3. (1 pt)** Add a code cell below this one.  Write code in it that prints out:
#    
#     A whole new cell! Wow!
# 
# Run your cell to verify that it works.

# In[ ]:


# get output from next cell and check that it equals 'A whole new cell! Wow!'
global credit
credit = 0
if my_notebook.cells[cell_num+1]['outputs'][0]['text'].strip() == 'A whole new cell! Wow!':
    credit = 1


# In[7]:


print("A whole new cell! Wow!")


# ## 1.4. Errors
# Python is a language, and like natural human languages, it has rules.  It differs from natural language in two important ways:
# 1. The rules are *simple*.  You can learn most of them in a few weeks and gain reasonable proficiency with the language in a semester.
# 2. The rules are *rigid*.  If you're proficient in a natural language, you can understand a non-proficient speaker, glossing over small mistakes.  A computer running Python code is not smart enough to do that.
# 
# Whenever you write code, you'll make mistakes.  When you run a code cell that has errors, Python will sometimes produce error messages to tell you what you did wrong.
# 
# Errors are okay; even experienced programmers make many errors.  When you make an error, you just have to find the source of the problem, fix it, and move on.
# 
# We have made an error in the next cell.  Run it and see what happens.

# In[8]:


print("This line is missing something."


# You should see something like this (minus our annotations):
# 
# ![error.jpg](attachment:error.jpg)
# 
# The last line of the error output attempts to tell you what went wrong.  The *syntax* of a language is its structure, and this `SyntaxError` tells you that you have created an illegal structure.  "`EOF`" means "end of file," so the message is saying Python expected you to write something more (in this case, a right parenthesis) before finishing the cell. Sometimes the error is not where Python thinks it is. If you can't find the error on the line that Python indicates, try looking at the line immediately prior to the line indicated by Python.
# 
# There's a lot of terminology in programming languages, but you don't need to know it all in order to make the computer do what you want. If you see a cryptic message like this, you can often get by without deciphering it.  (Of course, if you're frustrated, ask a neighbor or the instructor for help.)
# 
# Try to fix the code above so that you can run the cell and see the intended message instead of an error.

# ## 1.5. The Kernel
# The kernel is a program that executes the code inside your notebook and outputs the results. In the top right of your window, you can see a circle that indicates the status of your kernel. If the circle is empty (⚪), the kernel is idle and ready to execute code. If the circle is filled in (⚫), the kernel is busy running some code. 
# 
# You may run into problems where your kernel is stuck for an excessive amount of time, your notebook is very slow and unresponsive, or your kernel loses its connection. If this happens, try the following steps:
# 1. At the top of your screen, click **Kernel**, then **Interrupt**.
# 2. If that doesn't help, click **Kernel**, then **Restart**. If you do this, you will have to run your code cells from the start of your notebook up until where you paused your work.
# 3. If that doesn't help, restart your server. First, save your work by clicking **File** at the top left of your screen, then **Save and Checkpoint**. Next, click on the browser tab containing your directory structure, click on the **Running** tab, and then click on the orange **Shutdown** box next to your file. Click back on the **Files** tab and open the notebook your were working on again. You can now click on the x in the tab containing this file to close the tab. 

# ## 1.6. Submitting your work
# All assignments in the course will be distributed as notebooks like this one. You will submit your work by saving your file and then uploading it to Blackboard. All files will have a LASTNAME or LASTNAMES as part of their name. You should immediately change that to your last name, in CAPITALS. If you are working with a partner, add both your last names, in CAPITALS, separated by a hyphen (-). Do that now by clicking on **File** and selecting **Rename**. For instance, a group with MIDN Smith and MIDN Raven would call the file `lab 00-SMITH-RAVEN`. Also, fill in the cell below with your alpha codes replacing the ... Depending on how many people are in your group, your cell should look like: `alphas = [220000] or alphas = [220000,220006] or alphas = [220000,220006,220012]`.

# In[ ]:


global alphas # don't bother changing this line, just leave it alone; change the line below:
alphas = [...,....,...]


# ## 1.7. Comments
# You may have noticed the symbol `#` in the first line of the cell above. That is called a *comment*.  It doesn't make anything happen in Python; Python ignores anything on a line after a #.  Instead, it's there to communicate something about the code to you, the human reader.  Comments are extremely useful.

# # 2. Numbers
# 
# Quantitative information arises everywhere in data science and statistics. In addition to representing commands to print out lines, expressions can represent numbers and methods of combining numbers. The expression `3.2500` evaluates to the number 3.25. (Run the cell and see.)

# In[9]:


3.2500


# Notice that we didn't have to `print`. When you run a notebook cell, if the **last line** has a value, then Jupyter helpfully prints out that value for you. However, it won't print out prior lines automatically.

# In[10]:


print(2)
3
4


# Above, you should see that 4 is the value of the last expression, 2 is printed, but 3 is lost forever because it was neither printed nor last.
# 
# You don't want to print everything all the time anyway.  But if you feel sorry for 3, change the cell above to print it.

# ## 2.1. Arithmetic
# The line in the next cell subtracts.  Its value is what you'd expect.  Run it.

# In[11]:


3.25 - 1.5


# Many basic arithmetic operations are built in to Python.  The textbook section on [Expressions](http://www.inferentialthinking.com/chapters/03/1/expressions.html) describes all the arithmetic operators used in the course.  The common operator that differs from typical math notation is `**`, which raises one number to the power of the other. So, `2**3` stands for $2^3$ and evaluates to 8. 
# 
# The order of operations is what you learned in elementary school, and Python also has parentheses.  For example, compare the outputs of the cells below. Use parentheses to get a cool year for commissioning!

# In[12]:


8+6*5-6*3**2*2**3/4*7


# In[13]:


8+(6*5-(6*3))**2*((2**3)/4*7)


# In standard math notation, the first expression is
# 
# $$8 + 6 \times 5 - 6 \times 3^2 \times \frac{2^3}{4} \times 7,$$
# 
# while the second expression is
# 
# $$8 + (6 \times 5 - (6 \times 3))^2 \times (\frac{(2^3)}{4} \times 7).$$
# 
# **Question 4. (2 pts)** Write a Python expression in this next cell that's equal to $5 \times 3 - 51 + 2^{.5 \times 22} + 4 \times 2$.  
# 
# Replace the ellipses (`...`) with your expression.  Try to use parentheses only when necessary.
# 
# *Hint:* The correct output should start with a familiar number. Check your answer: the digits should sum to 4. 

# In[2]:


...


# In[ ]:


global credit
credit = 0
if eval(my_notebook['cells'][cell_num]['source'])== 5*3-51+2**(0.5*22)+4*2:
    credit = 2


# In[14]:


5*3-51+2**(0.5*22)+4*2


# # 3. Names
# In natural language, we have terminology that lets us quickly reference very complicated concepts.  We don't say, "That's a large mammal with brown fur and sharp teeth!"  Instead, we just say, "Bear!"
# 
# Similarly, an effective strategy for writing code is to define names for data as we compute it, like a lawyer would define terms for complex ideas at the start of a legal document to simplify the rest of the writing.
# 
# In Python, we do this with *assignment statements*. An assignment statement has a name on the left side of an `=` sign and an expression to be evaluated on the right.

# In[15]:


ten = 3 * 2 + 4


# When you run that cell, Python first evaluates the first line.  It computes the value of the expression `3 * 2 + 4`, which is the number 10.  Then it gives that value the name `ten`.  At that point, the code in the cell is done running.
# 
# After you run that cell, the value 10 is bound to the name `ten`:

# In[16]:


ten


# The statement `ten = 3 * 2 + 4` is not asserting that `ten` is already equal to `3 * 2 + 4`, as we might expect by analogy with math notation.  Rather, that line of code changes what `ten` means; it now refers to the value 10, whereas before it meant nothing at all.
# 
# If the designers of Python had been ruthlessly pedantic, they might have made us write
# 
#     define the name ten to hereafter have the value of 3 * 2 + 4 
# 
# instead.  You will probably appreciate the brevity of "`=`"!  But keep in mind that this is the real meaning.
# 
# **Question 5. (1 pt)** Try writing code that computes the sum of 2 and `eleven`. You should get an error because we haven't assigned a value to the name `eleven`. 

# In[ ]:


...


# In[ ]:


global credit
credit = 0
try:
    exec(my_notebook['cells'][cell_num]['source'])
except: 
    credit = 1 # give a point for any name error


# In[18]:


2+eleven


# A common pattern in Jupyter notebooks is to assign a value to a name and then immediately evaluate the name in the last line in the cell so that the value is displayed as output. 

# In[19]:


close_to_pi = 355/113
close_to_pi


# Another common pattern is that a series of lines in a single cell will build up a complex computation in stages, naming the intermediate results. In the cell below we'll compute the yearly salary of someone who earns 840 dollars every two weeks. 

# In[20]:


biweekly_salary = 840   
number_of_paychecks_in_a_year = 26           # 52 weeks divided by 2 weeks per paycheck 
yearly_salary = number_of_paychecks_in_a_year * biweekly_salary 
yearly_salary 


# **Aside**: confused about the meaning of `biweekly`? You have every right to be confused! Check out [Merriam Webster's dictionary blog](https://www.merriam-webster.com/words-at-play/on-biweekly-and-bimonthly) for more details if you are curious.

# Names in Python can have letters (upper- and lower-case letters are both okay and count as different letters), underscores, and numbers.  The first character can't be a number (otherwise a name might look like a number).  And names can't contain spaces, since spaces are used to separate pieces of code from each other.
# 
# Other than those rules, what you name something doesn't matter *to Python*.  For example, this cell does the same thing as the above cell, except everything has a different name:

# In[21]:


a = 840
b = 26
c = a*b
c


# **However**, names are very important for making your code *readable* to yourself and others.  The cell above is shorter, but it's totally useless without an explanation of what it does.

# # 4. Calling functions
# 
# The most common way to combine or manipulate values in Python is by calling functions. Python comes with many built-in functions that perform common operations.
# 
# For example, the `abs` function takes a single number as its argument and returns the absolute value of that number.  The absolute value of a number is its distance from 0 on the number line, so `abs(5)` is 5 and `abs(-5)` is also 5.

# In[22]:


abs(5)


# In[23]:


abs(-5)


# **Question 6. (1pt)** Set the variable `diff` equal to the absolute value of the difference between 15 and 128. Check your answer: it should be a positive number and your answer should use the `abs` function. 

# In[ ]:


diff = ... # make sure that your answer uses the abs function
diff


# In[24]:


diff = abs(15-128)
diff


# ## 4.1 Multiple arguments
# Some functions take multiple arguments, separated by commas. As an example, let's look at the `percentile` function. The function call 
# 
# `percentile(50,[4,2,3,5])`
# 
# computes the smallest number in the collection of numbers inside the brackets that is larger than or equal to  50% of all these numbers. Note that 50% of 4 numbers is 2 numbers, so we are looking for the smallest number among 4, 3, 2, and 5 that is larger than or equal to 2 of the numbers. Ordering the numbers in increasing order, it is easy to see that the number 3 is larger than or equal to 2 of the numbers (2 and 3) and it is the smallest such number. We say that 3 is the 50th percentile of the list of numbers 4, 2, 3 and 5.   
# 
# The `percentile` function is part of the `datascience` package of functions. Before we can call the `percentile` function, we need to import the `datascience` package. And before we can import the `datascience` package, we need to install it on our computer since it doesn't come preloaded in Anaconda Python. Fortunately, we only need to install the `datascience` package once (ever) on our computer. You may have already done this on Day 01, but if not, run the code in the following cell. You'll need an active internet connection. The command may take a minute or two to complete and it may print a fair bit of text to the screen, which you can ignore. If you mistakenly run the following code a second time, it will print a lot of text to the screen but it won't do any harm to your computer. 

# In[ ]:


# We only run the code in the following cell once. 
# You'll never have to pip install the datascience package again! 
# WARNING: This may take a minute or two and may print some odd text to the screen.
# If you get a pink WARNING box with a message about upgrading, you can ignore it.
get_ipython().system(' pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org datascience')


# In contrast to the code we just ran, we'll run the following `import` command once in every Python notebook before we use any of the functions in the `datascience` package. Since we'll be using the `datascience` package in almost all of our notebooks, this will become routine. It may take a few seconds to run the code in the following cell. 

# In[25]:


# We run the code in this cell in each notebook to allow us to use all the functions 
# in the datascience package.
from datascience import *


# Now we are ready to run the `percentile` command! 

# In[26]:


percentile(50,[4,3,2,5])


# The percentile command gave us the answer that we expected! Let's find the 51st percentile:

# In[27]:


percentile(51,[4,3,2,5])


# It is worth thinking carefully about the reason that `percentile(51,[4,3,2,5])` is 4. 
# 
# * The number 2 is larger than or equal to 1 of the four numbers, so it is larger than or equal to 25% of the numbers.   
# * The number 3 is larger than or equal to 2 of the four numbers, so it is larger than or equal to 50% of the numbers.  
# * The number 4 is larger than or equal to 3 of the four numbers, so it is larger than or equal to 75% of the numbers.  
# * The number 5 is larger than or equal to 4 of the four numbers, so it is larger than or equal to 100% of the numbers. 
# 
# We wanted the smallest number that is larger than 51 percent of the numbers. That number isn't 2 because 2 is only larger than 25% of the numbers. That number isn't 3 because 3 is only larger than 50% of the numbers. The number 4 is larger than 75% of the numbers (and hence larger than 51% of the numbers) and it is the smallest of the four numbers that has this property (5 is also larger than 51% of the numbers but it is not the smallest such number), so the 51st percentile of the four numbers is 4. 
# 
# In the next 3 cells we find the 70th, 75th and 76th percentiles of the collection of four numbers. Before running the code in each cell, try to predict what the `percentile` command will produce. 

# In[28]:


percentile(70,[4,3,2,5])


# In[29]:


percentile(75,[4,3,2,5])


# In[30]:


percentile(76,[4,3,2,5])


# **Question 7. (1 pt)** Set the variable named `perc` equal to the 80th percentile of the numbers 1, 2, 4, 6, and 9. 

# In[ ]:


perc = percentile(..., ...) # fill in the ... spots with the appropriate code (Hint: mimic the cell above)
perc


# In[56]:


perc = percentile(80, [1,2,4,6,9])
perc


# ## 4.2. Application: Inequality in the USA. 
# 
# One of the central issues in American society is the widening gap between the richest people and the average person. This rising level of inequality prompted the [Occupy Wall Street movement](https://en.wikipedia.org/wiki/Occupy_Wall_Street), starting in 2011. The following code loads income data from a random sample of over 68,000 households in the USA in 2019. 
#  The data has been obtained from the IPUMS-CPS organization (Citation: Sarah Flood, Miriam King, Renae Rodgers, Steven Ruggles and J. Robert Warren. Integrated Public Use Microdata Series, Current Population Survey: Version 6.0 [dataset]. Minneapolis, MN: IPUMS, 2018. https://doi.org/10.18128/D030.V6.0). Don't worry about the code in the next cell, just run it.

# In[67]:


income_table = Table.read_table("HHINCOME_2019.csv")
income_table


# We extract the numbers from the Income column and store the collection of numbers as `incomes`. Don't worry about the code in the next cell, just run it.

# In[68]:


incomes = income_table.column("Income")
incomes


# We can now compute the 20th percentile of the incomes of our sample:

# In[69]:


percentile(20,incomes)


# **Question 8. (2 pts)** Set `perc50` equal to the 50th percentile of the incomes and `perc99` equal to the 99th percentile of the incomes.  Check your answer: the 50th percentile ends in 21 and the 99th percentile ends in 14. 

# In[38]:


perc50 = percentile(..., ...)
perc99 = percentile(..., ...)
print(f"The 50th percentile is {perc50} and the 99th percentile is {perc99}.") 
# leave the following line alone, we are using for grading purposes
percs = [perc50,perc99]


# In[72]:


perc50 = percentile(50, incomes)
perc99 = percentile(99, incomes)
print(f"The 50th percentile is {perc50} and the 99th percentile is {perc99}.")
# leave the following line alone, we use it for grading purposes
percs = [perc50,perc99]


# The 50th percentile of the incomes is important since it can be interpreted as the income of the average person in our sample. You may want to think about which is higher: the income of the average person or the average income of all people in the US. We'll come back to this question when we examine skewed distributions later in the course.
# 
# Look back at line 3 in the cell above. By putting the `f` in front of the quotes, we tell Python to replace the expression inside the curly braces (e.g. `{perc50}`) with the value of that expression when printing to the screen. This **formatted print statement** can be very convenient.   

# **Question 9. (1 point)** Numbers on their own are not informative. You need to dig into the analysis to get a better understanding of the numbers **in context**. We'll learn how to ask penetrating questions to uncover hidden information in the data. Suppose you are interested in learning how inequality has changed over the last decade. Set the variable `helpful` equal to 1, 2, 3 or 4 to indicate which additional data is most helpful. 
# 
# 1. Data about the race of the individuals in our sample.  
# 2. Similar income data from a large sample of people in the US in 2009.  
# 3. Tax rates for various income ranges in 2019.  
# 4. Education levels for the people in our sample.   

# In[ ]:


helpful = ... # replace ... by 1, 2, 3 or 4
helpful


# In[38]:


helpful = 2 # replace ... by 1, 2, 3 or 4
helpful


# We should always think critically about the data that we're analyzing. For instance, we might ask about how the income data were collected: 
# 
# * How were the households in the survey selected? 
# * Were the households required to participate or did they volunteer?  
# * Are the response rates for households linked to some other feature of the household? For example, do single parent households respond less frequently than multi-parent households? This would be an example of **response bias**. 
# * Was there financial compensation offered to participate?  
# * What efforts were made to ensure that the households were reflective of American society? One way to address this is through **stratified sampling.**
#     * Were there efforts to ensure that racial groups were included at levels that reflect their prevalence in the USA?  
#     * Were there efforts to ensure geographic disparity? 
#     * Are certain professions over or under-represented in the survey? 
#     
# Let's look at our income data again: 

# In[37]:


income_table


# We have to be aware of **measurement error** in any data analysis. If the data isn't exact, then the error in the measurements will lead to an error in our analysis. For example, our 50th percentile calculation may not be correct. We'll learn ways to deal with this kind of uncertainty in our course. 
# 
# **Question 10. (1 pt)** Set the variable `estimated_income` equal to 1 if you think that some of the income figures in the table are not exact values but rather an estimate of the household income. Set `estimated_income` equal to 2 if you think that all of the income figures in the table are exact values. 

# In[38]:


estimated_income = ... #  replace ... with 1 or 2
estimated_income


# In[ ]:


estimated_income = 1 #  replace ... with 1 or 2
estimated_income


# You're done with Lab 00!  Choose **Save and Checkpoint** from the **File** menu, then choose **Close and Halt** from the **File** menu. Then upload your file to Blackboard. **Upload only one file per group. Also ensure that you are uploading the LASTNAMES file from your usual directory and not the one from the checkpoints subdirectory (you don't want to upload the backup file).**
