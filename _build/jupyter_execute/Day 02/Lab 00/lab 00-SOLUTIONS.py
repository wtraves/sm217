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
# **Today's lab**
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


# # Anaconda and Jupyter
# 
# In this class we'll use Anaconda's distribution of Python to do computations. Those computations take place inside your laptop. We use a Jupyter notebook to interface with the computer: to give the computer instructions and see the results of its computation. This webpage is a Jupyter notebook. 

# ## Cells
# 
# A notebook is made up of cells, each a rectangular block of text or code. Text cells display both words and pictures. We can use `markdown` format to tell the computer to display text in special ways. For instance, we can write words in **bold** or in *italics*. A popular [cheat sheet](https://www.markdownguide.org/cheat-sheet/) contains information about some of the things that markdown can do, though we won't require you to do anything fancy in this class.   
# 
# **Question 1.** (1 pt) Left-click on the cell below to edit the text in the cell. Change the message so that it mentions markdown rather than markup format. Then hit <kbd>Shift</kbd>+<kbd>Enter</kbd> to **render** the cell: to make it display the text. 

# This cell is written in markup format. 

# This cell is written in markdown format.

# Code cells contain instructions for the computer. Those instructions can be in several languages; we'll always write our instructions in Python, a popular language for data science. The cell below is a code cell and contains instructions that tell the computer to print **Hello World!** to the screen. Note that the text that we intend to print is enclosed in double quotes. Left click on the cell and hit <kbd>Shift</kbd>+<kbd>Enter</kbd> to **execute** the commands in the cell. 

# In[ ]:


print("Hello World!")


# We've made a few changes to the Jupyter notebook. Let's save our notebook to record the changes. The easiest way to do this is to click on the floppy disk button immediately below the `jupyter` symbol on the top left of this page. Hit this SAVE button now.
# 
# There are other buttons there as well: they add a cell, delete a cell, copy a cell, and paste a cell. The arrow buttons allow you to move cells too. We don't recommend using these buttons at all. The notebooks we work with have cells with hidden information used by our autograder and using these buttons can mess up that process. However, it is a good idea to hit the SAVE button every few minutes so that you don't lose much of your work if your computer crashes. 
# 
# You should also see an empty circle next to Python 3 at the top right of this notebook. When the computer is working to execute code that circle will be filled in. If the computer is working on code for an excessive amount of time, there may be a problem with your code or your computer. In this case, we recommend the following procedure: 
# 
# 1. Click on the **File** menu and select **Save and Checkpoint**.   
# 2. Click on the x in the browser tab for this notebook to close it.  
# 3. In the browser tab containing your directory structure, click on the **Running** tab, and then click on the orange **Shutdown** box next to your file.  
# 4. Click back on the **Files** tab and open the notebook your were working on again. 

# ## Arithmetic
# 
# You can use Python like a fancy calculator.  Run the following cell. 

# In[ ]:


1+2+3


# Cells can contain multiple lines of code. Each line is executed in the order in which they appear. Python displays the output of the expression on the last line of the cell. For instance, after running the following cell, we'll just see the number 4, even though Python executes three lines of code; the evaluation of two of the lines of code are not displayed.

# In[ ]:


1+1
1+2
1+3


# We can see all three numbers using print statements. The f in front of the double quotes indicates a formated string, in which expressions between curly braces are not printed but rather their value is printed. Run the code in the following cell. 

# In[ ]:


print(f"The value of 1+1 is {1+1}.")
print(f"The value of 1+2 is {1+2}.")
print(f"The value of 1+3 is {1+3}.")


# **Question 2. (1 pt)** Python knows your Dear Aunt Sally! Well, perhaps you don't have an Aunt Sally, but Python does know the order of arithmetic operations, PEMDAS -- parentheses first, then exponents, multiplication, division, addition and subtraction -- an ordering which is easy to remember as **P**lease **E**xcuse **M**y **D**ear **A**unt **S**ally. Use this information to have Python compute and print the value of the expression 
# $$ 1+2+3*4-(1-2^3)+2*10^3.$$
# Do this by replacing the ellipses (...) in the code below with an appropriate arithmetic expression. You should use a single asterisk for multiplication -- e.g. 2\*3 is 6 -- and double asterisks for exponents: $3^2$ is coded as 3\*\*2 in Python. 

# In[ ]:


print(f"The value of the expression is {...}.")


# In[13]:


print(f"The value of the expression is {1+2+3*4-(1-2**3)+2*10**3}.")


# **WARNING**: Sometimes computations give rise to round-off error: error that is due to the way that the computer stores and adds numbers in its internal memory. For instance: we know that 0.1 + 0.2 = 0.3 but Python's computation comes up with a tiny error in the final computation; run the next cell and see!

# In[2]:


0.1+0.2


# Round-off error is a common problem in all numerical computation, but it won't really bother us in this class.

# ## Syntax Errors and Carry-over Lines
# 
# When we run the following cell, we get an informative error. Try it! 

# In[15]:


print(f"The value of the expression is {2*1010}.)


# We see unusual output saying that there is a `SyntaxError`. This means that the computer got an instruction that doesn't conform to its input requirements. Computers are like extremely strict teachers: they **only** accept input in very specific ways! Here additional details are provided: we hit an `EOL while scanning string literal`. This isn't too helpful unless you know that `EOL` stands for end of line. The computer was trying to assess the input instruction on line 1 but hit the end of the line before encountering something that it needed. In this case we're missing the second set of double quotes to close out the text we want to print to the screen. The caret (^) in the brown line is pointing to where the computer understood that it hit an error, but sometimes the error comes earlier than that location. Here we are missing a double quote before the parenthesis rather than after it. Try editing the cell above and re-running it so that it does not display an error. When you try to add the second set of double quotes you may get a pair of double quotes (""). Just click between them and hit DELETE to get rid of one of them. 
# 
# The errors you'll encounter often involve missed parentheses or quotes. If you or your team can't find the error, don't be shy about asking your instructor for assistance. We aren't really focused on coding in this class and we'll be happy to get you back on track! 
# 
# Python will often stop reading your code at the end of a line, but you can force Python to continue reading your code on the following line if you've opened a parenthesis but not yet closed it. For instance, the following code works fine. 

# In[12]:


(
1+2
+3+4
)


# Python keeps reading from line 1 to line 2 since a parenthesis remains open, continues on to line 3 and then sees the closing parenthesis on line 4, only then stopping to evaluate the sum. We'll make good use of this behavior later in the course. You can also explicitly tell Python to keep reading on the next line by ending your line with the \ symbol. 

# ## Variables 
# 
# Computation with numbers isn't so hard we'll also make good use of variables, which can be confusing at first, as noted in the comic [Rhymes with Orange](https://nebusresearch.wordpress.com/2019/07/09/reading-the-comics-july-2-2019-back-on-schedule-edition/) by Hilary Price from 30 JUN 2019, where one student says says to the other, "Math isn't fair; it's numbers, numbers, numbers, then BAM! It's letters." as the teacher writes an equation using variables on the blackboard.
# 
# We use variables to assign names to particular values. This allows us to access the value without re-doing the computation in the future. Even if we are not going to use a value later, it can be helpful to give it a descriptive name. This can make our code readable. For instance, suppose I pay my son \$30 to mow the lawn each week over a 12-week summer; how much money does he earn? The next cell does the computation using descriptive variable names.

# In[3]:


weekly_payment = 30    # this line defines the variable weekly_payment and gives it the value 30
weeks_in_summer = 12
total_earnings = weekly_payment * weeks_in_summer
print(f'He earns ${total_earnings} for mowing the lawn all summer.')


# Note how the computation on line 3 is almost self-explanatory: if we had just written 
# 
# `total_earnings = 30 * 12`
# 
# you wouldn't know where the numbers 30 and 12 came from. Also note that Python remembered the value of `weekly_payment` from line 1 when using it on line 3. 
# 
# In general, we give a quantity a name (also known as defining a variable) using the syntax
# 
# `variable_name = value`
# 
# That is, the variable name goes on the left of the `=` sign and the value (or a computation that gives rise to a value) goes on the right. The equals sign here doesn't really mean equality: in this context it should be read as "the name on the left refers to the value on the right".
# 
# Did you notice the `#` sign on line 1? It tells Python that the remainder of the line is just a comment to the reader and so Python ignores it. 
# 
# The values of the variables can be accessed in all subsequent cells too. For instance, suppose that I decided to pay my son \$35 to mow the lawn; how much does he earn over the summer now? 

# In[5]:


new_weekly_payment = 35
new_total_earnings = new_weekly_payment * weeks_in_summer
new_total_earnings


# Note that on line 2 we used the variable `weeks_in_summer` that was defined in a previous cell. 
# 
# **Choose your variables names carefully!** Variable names should be short **and** descriptive.The following code uses variables but isn't very readable since the variables are not descriptive. 

# In[6]:


a = 35
b = 12 
c = a * b 
print(f'He earns ${c} for mowing the lawn all summer.')


# There are rules for variable names in Python. Variable names can't start with a number (e.g. 20thCompany) is not allowed and no spaces are allowed (we use underscores instead). We tend to prefer variable names that are in lowercase letters with words separated by underscores, though we aren't terribly consistent. Sometimes you'll see variables in camel case (e.g. `WeeklyPayment`), so-called because of the up and down variation in the heights of the letters. 

# **Question 3. (2 pt)** My son gets entrepreneurial and offers to do all sorts of chores around the house for \$40 per week. Set the variable `yearly_earnings` equal to the amount (in dollars) that he could earn over a whole year. Use other suitable variable names for full credit.  

# In[ ]:


... = 40 # define a suitably named variable
= 52 # define a suitably named variable
yearly_earnings = ... # compute yearly_earnings equal
yearly_earnings # this line just displays the yearly earnings, leave it alone :)


# In[7]:


weekly_payment = 40 # define a suitably named variable
weeks_in_a_year = 52 # define a suitably named variable
yearly_earnings = weekly_payment * weeks_in_a_year # compute yearly_earnings equal
yearly_earnings # this line just displays the yearly earnings, leave it alone :)


# ## Functions 
# 
# You are used to trigonometric functions like sine, cosine, and tangent, and other functions like the absolute value function that takes an input number and returns the positive number of the same magnitude. Python knows about the absolute value function: to compute |-2| you write `abs(-2)`. Note that the computation requires a function name followed by some input arguments in parenthesis. Here there is just one input argument, -2.  When we apply a function to some input we say that we are "calling the function".

# In[11]:


abs(-2)


# In[12]:


abs(2) # note that the absolute value of 2 is what you'd expect


# **Question 4. (2pts)** Set the variable `diff` equal to the absolute value of the difference between 15 and 128. Check your answer: it should be a positive number and your answer should use the `abs` function. 

# In[ ]:


diff = ... # make sure that your answer uses the abs function
diff


# In[ ]:


global credit
credit = 0
if diff == 113:
    credit += 1.5 
if "abs(" in my_notebook['cells'][cell_num]['source']:
    credit += 0.5


# In[24]:


diff = abs(15-128)
diff


# ## Multiple arguments
# Some functions take multiple arguments, separated by commas. As an example, let's look at the `percentile` function. The function call 
# 
# `percentile(50,[4,2,3,5])`
# 
# computes the smallest number in the collection of numbers inside the brackets that is larger than or equal to  50% of all these numbers. Note that 50% of 4 numbers is 2 numbers, so we are looking for the smallest number among 4, 3, 2, and 5 that is larger than or equal to 2 of the numbers. Ordering the numbers in increasing order, it is easy to see that the number 3 is larger than or equal to 2 of the numbers (2 and 3) and it is the smallest such number. We say that 3 is the 50th percentile of the list of numbers 4, 2, 3 and 5.   
# 
# The `percentile` function is part of the `datascience` package of functions. Before we can call the `percentile` function, we need to import the `datascience` package. And before we can import the `datascience` package, we need to install it on our computer since it doesn't come preloaded in Anaconda's distribution of Python. Fortunately, we only need to install the `datascience` package once (ever) on our computer. You may have already done this on Day 01, but if not, run the code in the following cell. You'll need an active internet connection. The command may take a minute or two to complete and it may print a fair bit of text to the screen, which you can ignore. If you mistakenly run the following code a second time, it will print a lot of text to the screen but it won't do any harm to your computer. 

# In[ ]:


# We only run the code in the following cell once. 
# You'll never have to pip install the datascience package again! 
# WARNING: This may take a minute or two and may print some odd text to the screen.
# If you get a pink WARNING box with a message about upgrading, you can ignore it.
get_ipython().system(' pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org datascience')


# In contrast to the code we just ran, we'll run the following `import` command once in every Python notebook before we use any of the functions in the `datascience` package. Since we'll be using the `datascience` package in almost all of our notebooks, this will become routine. It may take a few seconds to run the code in the following cell. 

# In[14]:


# We run the code in this cell in each notebook to allow us to use all the functions 
# in the datascience package.
from datascience import *


# Now we are ready to run the `percentile` command! 

# In[15]:


percentile(50,[4,3,2,5])


# The percentile command gave us the answer that we expected! Let's find the 51st percentile:

# In[16]:


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

# In[17]:


percentile(70,[4,3,2,5])


# In[18]:


percentile(75,[4,3,2,5])


# In[19]:


percentile(76,[4,3,2,5])


# **Question 5. (1 pt)** Set the variable named `perc` equal to the 80th percentile of the numbers 1, 2, 4, 7, and 9. 

# In[ ]:


perc = percentile(..., ...) # fill in the ... spots with the appropriate code (Hint: mimic the cell above)
perc


# In[21]:


perc = percentile(80, [1,2,4,7,9])
perc


# ## Application: Inequality in the USA. 
# 
# One of the central issues in American society is the widening gap between the richest people and the average person. This rising level of inequality prompted the [Occupy Wall Street movement](https://en.wikipedia.org/wiki/Occupy_Wall_Street), starting in 2011. The following code loads income data from a random sample of over 68,000 households in the USA in 2019. 
#  The data has been obtained from the IPUMS-CPS organization (Citation: Sarah Flood, Miriam King, Renae Rodgers, Steven Ruggles and J. Robert Warren. Integrated Public Use Microdata Series, Current Population Survey: Version 6.0 [dataset]. Minneapolis, MN: IPUMS, 2018. https://doi.org/10.18128/D030.V6.0). Don't worry about the code in the next cell, just run it.

# In[22]:


income_table = Table.read_table("HHINCOME_2019.csv")
income_table


# We extract the numbers from the Income column and store the collection of numbers as `incomes`. Don't worry about the code in the next cell, just run it.

# In[23]:


incomes = income_table.column("Income")
incomes


# We can now compute the 20th percentile of the incomes of our sample:

# In[24]:


percentile(20,incomes)


# **Question 6. (2 pts)** Set `perc50` equal to the 50th percentile of the incomes and `perc99` equal to the 99th percentile of the incomes.  Check your answer: the 50th percentile ends in 21 and the 99th percentile ends in 14. 

# In[38]:


perc50 = percentile(..., ...)
perc99 = percentile(..., ...)
print(f"The 50th percentile is {perc50} and the 99th percentile is {perc99}.") 
# leave the following line alone, we are using for grading purposes
percs = [perc50,perc99]


# In[25]:


perc50 = percentile(50, incomes)
perc99 = percentile(99, incomes)
print(f"The 50th percentile is {perc50} and the 99th percentile is {perc99}.")
# leave the following line alone, we use it for grading purposes
percs = [perc50,perc99]


# The 50th percentile of the incomes is important since it can be interpreted as the income of the average person in our sample. You may want to think about which is higher: the income of the average person or the average income of all people in the US. We'll come back to this question when we examine skewed distributions later in the course.

# **Question 7. (1 point)** Numbers on their own are not informative. You need to dig into the analysis to get a better understanding of the numbers **in context**. We'll learn how to ask penetrating questions to uncover hidden information in the data. Suppose you are interested in learning how inequality has changed over the last decade. Set the variable `helpful` equal to 1, 2, 3 or 4 to indicate which additional data is most helpful. 
# 
# 1. Education levels for the people in our sample.
# 2. Tax rates for various income ranges in 2019.
# 3. Data about the race of the individuals in our sample.  
# 4. Similar income data from a large sample of people in the US in 2009.  

# In[ ]:


helpful = ... # replace ... by 1, 2, 3 or 4
helpful


# In[26]:


helpful = 4 # replace ... by 1, 2, 3 or 4
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

# In[27]:


income_table


# We have to be aware of **measurement error** in any data analysis. If the data isn't exact, then the error in the measurements will lead to an error in our analysis. For example, our 50th percentile calculation may not be correct. We'll learn ways to deal with this kind of uncertainty in our course. 
# 
# **Question 8. (1 pt)** Set `exact_income` equal to 0 if you think that some of the income figures in the table are not exact values but rather an estimate of the household income. Set the variable `exact_income` equal to 1 if you think that all of the income figures in the table are exact values.  

# In[38]:


exact_income = ... #  replace ... with 0 or 1
exact_income


# In[28]:


exact_income = 0 #  replace ... with 0 or 1
exact_income


# ## Submitting your work
# All assignments in the course will be distributed as notebooks like this one. You will submit your work by saving your file and then uploading it to Blackboard. All files will have a LASTNAME or LASTNAMES as part of their name. You should immediately change that to your last name, in CAPITALS. If you are working with a partner, add both your last names, in CAPITALS, separated by a hyphen (-). Do that now by clicking on **File** and selecting **Rename**. For instance, a group with MIDN Smith and MIDN Raven would call the file `lab 00-SMITH-RAVEN`. Also, fill in the cell below with your alpha codes replacing the ... Depending on how many people are in your group, your cell should look like: `alphas = [220000] or alphas = [220000,220006] or alphas = [220000,220006,220012]`.

# In[ ]:


global alphas # don't bother changing this line, just leave it alone; change the line below:
alphas = [...,....,...]


# You're done with Lab 00!  Choose **Save and Checkpoint** from the **File** menu, then choose **Close and Halt** from the **File** menu. Then upload your file to Blackboard. **Upload only one file per group. Also ensure that you are uploading the LASTNAMES file from your usual directory and not the one from the checkpoints subdirectory (you don't want to upload the backup file).**
