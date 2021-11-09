#!/usr/bin/env python
# coding: utf-8

# # Data Science for Decision Makers
# 
# Much of this course will focus on **data analysis and the communication of insights obtained from data**, key skills for military officers. The Navy's Education for Seapower report makes a strong case for developing these skills at USNA: 
# 
# >In the Cognitive Age, where leaders have to deal not only with incomplete data but also with analysis and decision making in a world that involves overwhelming data, the ability to evaluate information, reason strategically and ethically, and act decisively, will be essential elements of future success. These are skills that can be taught. These are talents that can be developed. The challenges and multi-disciplinary issues of our contemporary world can and should be specifically examined through our naval education programs. [Education for Seapower Final Report, page 11](https://media.defense.gov/2020/May/18/2002302021/-1/-1/1/E4SFINALREPORT.PDF)
# 
# This course is a direct response to remarks by Vice Admiral Sean Buck, who encouraged USNA to develop a data science curriculum to make midshipmen more effective officers. 
# 
# The National Academies of Sciences, Engineering and Medicine introduce data science in the following way: 
# 
# > Today, the term “data scientist” typically describes a knowledge worker who is principally
# occupied with analyzing complex and massive data resources. However, data science spans a broader
# array of activities that involve applying principles for data collection, storage, integration, analysis,
# inference, communication, and ethics. In future decades, all undergraduates will profit from a
# fundamental awareness of and competence in data science. [NASEM report, page S1](https://www.nationalacademies.org/our-work/envisioning-the-data-science-discipline-the-undergraduate-perspective)
# 
# We'll use a slightly modified list of data science tasks: **data collection, storage, management, analysis, communication, and deployment** span the **data science life cycle**. 
# 
# To illustrate the meaning of each task, consider one of the Navy's current data science projects aimed at reducing maintenance costs on our F-18 fighter jets. Currently we perform maintenance on manufacturer-suggested schedules, but we might be able to align maintenance efforts to aircraft performance, saving money on unnecessary service and identifying needed repairs before our air crew is put at risk. The project **collects** performance data on the airplanes as well as data from the maintenance crews and parts supply chain.  Data from these various sources may be combined in a single database. The database is too massive to save on a single computer and must be **stored** in a data warehouse. Access to the data is strictly **managed**, so that only authorized users can see it. Data scientist **analysis** identifies patterns in the data: performance readings that signal a plane needs maintenance. The analysts **communicate** the results of the analysis to many different stakeholders, including senior Navy leadership, air bosses, and maintenance crews. Eventually, we will develop and **deploy** a computer application that tracks aircraft performance and suggests maintenance actions for planes in real-time. The data science project doesn't end there; we would want to continue to collect and analyze data to ensure that the deployed system evolves as the performance of the jets changes. 
# 
# <img src="f18_pic.jpg" alt="f18 jet" align="center" width="400px">
# 
# <center> An F/A-18E Super Hornet from the Tophatters of Strike Fighter Squadron (VFA) 14 flies past aircraft carrier USS John C. Stennis in April 2013. (US Navy/MC3 Ignacio D. Perez; picture appeared on the cover of the [2015 June-July issue of Air and Space magazine](https://www.airspacemag.com/military-aviation/about-f-18-photo-180955971/)) </center>
# 
# ## Why is data science so popular today?
# 
# Intense interest among commercial and government entities has led to massive investments in data science.  Many data science projects make significant use of probability and statistics, mathematical tools that help us understand and quantify uncertainty. These tools have been around for a long time but several recent developments are making data science more important and more effective than ever before.  Essentially there are three factors driving data science development: more available data, more powerful computers, and more sophisticated algorithms. 
# 
# * **More data**: Internet browsing requires the transmission of data about you and your past browsing history, giving rise to a lot of information about online behavior. Similarly, the internet of things (IoT) -- internet enabled devices like smart doorbells and fitness trackers -- produce massive amounts of data about our physical world. Economic data is carefully tracked and published; see the [FRED website](https://fred.stlouisfed.org/) for data compiled by the St. Louis Federal Reserve bank. Demographic data is collected by the U.S. Census Bureau every ten years, but they also collect data about housing and jobs more frequently in the [American Community Survey](https://www.census.gov/programs-surveys/acs).  Many cities publish data about their operations, including information about crime and policing, taxes, and business activity. For example, check out Washington's D.C.'s data on [Open Data DC](https://opendata.dc.gov/). The availability of large accessible datasets gave rise to the **big data** revolution, a precursor to the current data science craze.
# 
# * **More powerful computers**: In the mid-1980's statisticians developed simple statistical methods, replacing theoretically intensive statistical tests with large-scale computer simulations. These simulation methods have an additional advantage: they don't require us to make hard-to-test assumptions about the way the data were generated. However, simulation requires a lot of computation. Too much computation for the personal computers of the Reagan era. But computer processing speeds have grown according to Moore's law: doubling every two years. This exponential growth in processing power led to today's laptop computers, machines with enough processing power to manipulate large datasets in the blink of an eye. More powerful computers helped make data science possible.  
# 
# * **More sophisticated algorithms**: Many of the most important recent developments in data science depend on advances in machine learning. You may have heard about deep neural networks, which are behind many of these new applications. For instance, a special kind of neural network called a convolutional neural net allows computers to classify objects in images after being trained on many pictures of such objects.  These algorithms help drive autonomous cars like Tesla's model X. The hype around the computer chess program AlphaZero hasn't reached Elon Musk's level yet, but it is revolutionizing many fields where humans used to outperform computers. Of course, computers could reliably beat the world's best chess players by the mid-2000's, but in 2018, the company DeepMind used a technique called reinforcement learning to teach a computer to play chess from scratch. Just 24 hours after learning the rules of the game, AlphaZero dominated the best computer chess programs like those programs beat up on human players! This suggests that there may be many areas where computers can quickly achieve superhuman performance. We can expect to see more of such technology in the future, perhaps one day we'll even have an AlphaNavy! 
# 
# That last comment was a bit of a joke but the pace at which technology is advancing isn't a laughing matter. Data science (more specifically, machine learning and artificial intelligence) has all sorts of applications, some of which which might be unethical or unwise. Though we won't get into the details of these technical learning algorithms, we will discuss some of the ethical issues arising in data science later in this class.  
# 
# 
# ## More details about this class
# 
# The preceding discussion already points towards some of the special characteristics of this course that distinguish it from a traditional statistics course. First, we'll make heavy use of the computer. We'll learn to code basic instructions in **Python**, a free general-purpose computer language that is particularly popular for data science. You've probably already downloaded the Anaconda distribution of Python and installed it on your laptop. However, this is not a computer programming course so we've carefully picked an instructional path that teaches you how to do both data manipulation and statistical simulation without getting bogged down in computer jargon. 
# 
# We'll work with complex real-world datasets, many of which involve thousands of rows of data. The range of applications of data science is astonishing. We've made a special effort to include data and applications that relate to the majors of the midshipmen taking this course, as well as datasets with military applications. There are several places where our methods differ from the traditional statistics course. Some majors, most notably Chemistry and Political Science, continue to make good use of these statistical methods so, when appropriate, we'll point out how our methods relate to techniques in those disciplines. 
# 
# Finally, we've avoided most of the mathematical prerequisites for a traditional probability or statistics class. There are a few optional sections (labeled as **PRO TIPS**) where we use Calculus, but this class is essentially independent of your past advanced mathematics courses. If you've struggled with mathematics in the past, think of this course as a fresh start. And if you've done well in your previous mathematics courses, then you'll be able to read some of those optional sections!  
# 
# Our approach is very much in line with recommendations laid out in the 2016 GAISE College Report, endorsed by the American Statistical Association. The material in this course is based off pioneering work in the U.C. Berkeley's [data8 course](https://data8.org/) but we've modified their curriculum to adapt to the needs of the Naval Academy, the Navy and the Marine Corps. 
# 
# ## Overview of course topics
# 
# The course breaks up into roughly three parts: data manipulation and visualization, statistical methods for data analysis, and ethical and methodological problems in machine learning. We've listed some of the questions that we'll be studying below.
# 
# **Data manipulation and visualization**: 
# * **Data management**: How do we organize, collate, and clean datasets? 
# * **Summary statistics**: What measurements give an appropriate summary of our data? 
# * **Visualization**: How do we choose an appropriate visualization to display our data?
# * **Communication**: What factors should be considered when briefing senior leadership on the results of our analysis? 
# 
# **Statistical methods for data analysis**: 
# * **Data collection**: What can we learn from data collected outside ideally controlled laboratory settings? 
# * **Probability**: How can we quantify and think about uncertainty and risk? 
# * **Conditional Probability**: How do we reassess the likelihood of an event given new information? 
# * **Hypothesis testing**: How strong is the evidence in a dataset for a particular claim? What level of evidence is necessary to support a decision or policy? 
# * **Confidence intervals**: How can we use data and simulation to estimate unknown quantities?
# * **Central limit theorem**: Why do large datasets allow more precise results and what can we conclude when we just have a little data?
# * **Regression and correlation**: How can we use trends in our data to make good numerical predictions? 
# 
# **Advanced Topics**: 
# * **Classification** How can machine learning algorithms predict which military community a midshipman will join when they commission as an officer? 
# * **Ethics**: Machine learning and data science allow predictions, which drive decisions, which affect individuals, communities, and our environment. How can we understand the ethical implications of machine learning applications? 
# * **Human-data interaction**: Data science is not done in a vacuum; it takes place in societies, with all their complex issues. How do social factors interact with machine learning applications? 
# * **Decision making**: What are the key questions to ask about any data analysis? 
# 
# ## Work flow in this course
# 
# We'll settle into a very structured work flow in this course. You'll do a small amount of reading prior to each class. In-class interactive lectures and labs will require that you've done this background reading, so we'll have daily reading quizzes to reward your efforts. We will have approximately ten in-class labs done in groups of two to three midshipmen and ten individual homework assignments. We will also have five in-class quizzes, two tests, and a final exam to <del>test</del> celebrate 😃 your progress.  
# 
# Your instructor will have office hours for you to set up extra instruction (EI). As well, we have a very talented group of Midshipman Group Study (MGSP) Leaders that excelled in this course and are keen to work with you to ensure your success. We realize that working with the computer and dealing with data are not intuitive concepts and we are committed to providing strong support for you in this course. It is not a sign of weakness to ask for help; rather it shows initiative and commitment. 

# ## Income in the USA
# 
# Let's look at an example of data analysis using U.S. household income data from 2010 to 2019. The data is from a random sample of over 800 thousand households over 11 years. Incomes are not adjusted for inflation, so take this into account when comparing values. The data has been obtained from the [IPUMS-CPS organization](https://doi.org/10.18128/D030.V6.0). Don't worry about the commands below; we are just trying to give you a feel for some of the kinds of analysis we'll be doing. 

# ### Install the Datascience Package
# 
# Before doing anything else, we need to **install** the `datascience` package. This contains specialized commands that make it easier to learn data science tasks in Python. 
# 
# This only needs to be done **once on each machine**. We run the following code cell in a Jupyter notebook to install the package.  

# In[1]:


# left click on this cell and hit SHIFT-ENTER
get_ipython().system(' pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org datascience')


# We'll also import the `datascience` package and other packages into our Python session, giving us access to special commands.  

# In[2]:


from datascience import *                 # datascience library has great data science commands
import numpy as np                        # numpy has great numerical commands

# These following lines do some fancy plotting magic; you can safely ignore them
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)


# We read in the data from the file `income_data.csv`. A csv file is a **comma-separated value** file. It contains a table of data, where the entries of each row appear on their own line in the file and the values in the columns are separated by commas. 

# In[3]:


income_data = Table.read_table("income_data.csv")
income_data.show(10)


# ### Summary Data
# Now we look at the yearly mean, median, and high incomes. We put them all in a new table. 
# 
# The **mean** of a collection of data is the **average value** of the data: to compute the mean we sum up the values and divide by the number of values. The **median** of a collection of data is the **middle value** of the data. We line up the values in increasing order. If the number of values is odd, then the median is the middle value. If the number of values is even the median is the average of the two values that are in the middle of the collection. Don't worry about the hidden code below, but do look at its output! What happened to the mean income from 2009 to 2019? What happened to the median income over the same time period?

# In[4]:


summary_by_year = Table.read_table("summary_by_year.csv")
summary_by_year.set_format("Income mean",NumberFormatter(2))
summary_by_year.set_format("Income median",NumberFormatter(2))
summary_by_year.set_format("Income high",NumberFormatter(2))
summary_by_year.show(11)


# ### Percentiles
# The 80th percentile of a collection of values is the smallest value in the collection that is at least as large as 80% of all of the values. Roughly speaking, if you line up all the values from smallest to largest, the 80th percentile will be the value 80% along the list. This is only a rough idea though: if we only have 3 values then there is no value 80% along the list, which is why we phrase the definition of percentile in that awkward way. 
# 
# The 25th percentile is sometimes called the **first quartile**, the 50th percentile is sometimes called the second quartile, and the 75% percentile is sometimes called the third quartile. Answer this question for yourself: Is the 99th percentile a large value relative to the other values in the collection or a small value?
# 
# You can read more about percentiles in section 13.1 of the [data8 textbook](https://www.inferentialthinking.com/chapters/13/1/Percentiles.html). 

# ### We are the 99%
# 
# The slogan, "We are the 99%" originated in the Occupy movement, which grew out of protests in New York City in 2011. The movement was a push for social justice and the slogan references the increasing concentration of wealth and income among the top 1%. 

# <img src="99percent.jpg" alt="protest march" align="center" width="400px">
# 
# <center> Protesters march in downtown Portland, Oregon on Nov. 17, 2011. (AP Photo/Don Ryan) </center>

# Let's compute and plot the 25th, 50th, 75th and 99th percentiles for our household income data over the period 2011 to 2019. First we make a table with the percentiles. Notice how difficult it is to get insight from a glance at the table. We'd need to to do a lot of work to make sense of this data. 

# In[5]:


percentiles_data = Table.read_table('summary_by_year_with_percentiles.csv')
percentiles_data.show(11)


# In contrast, we can get an immediate sense of what is going on from a plot of the data. 

# In[6]:


# gather the percentile data in its own table and plot values with Year on the x-axis:
summary_with_just_percentile_data = percentiles_data.select([0,4,2,5,6])
summary_with_just_percentile_data.plot('Year')


# The data shows that the 99th percentile for household income took a huge hit in 2011 and then rebounded over the following 5 years. The income for the 99th percentile has been rising steeply since 2011, particularly compared with the income gains among the rest of the population. 
# 
# Caution is advised when comparing percentiles, averages or other summary statistics over time.   We aren't tracking individual households. Any individual household may suffer a serious loss, dropping it out of the 99th percentile. However, another household takes its place, propping up the 99th percentile's value. So the group's composition may change from year to year, masking changes. It becomes hard to tell whether a drop in income is due to a drop in income for the top 1% overall, or whether the drop is due to changes in who makes up the top 1%. 

# ### Skewed distributions
# Let's look at a **histogram** of the 2019 household incomes, as well as the median and mean incomes. Distributions of income, wealth, and housing prices tend to be heavily **right-skewed**: there is a long tail of rare high values that pulls the mean above the median. You can read more about skewed distributions in section 14.1 of the [data8 textbook](https://www.inferentialthinking.com/chapters/14/1/Properties_of_the_Mean.html). Again, ignore the hidden code below and just look at the picture that it outputs.

# In[7]:


# restrict to 2019 data
income_2019 = income_data.where('Year',are.equal_to(2019))

# compute some summary statistics
median_2019 = np.median(income_2019.column('Income'))
mean_2019 = np.mean(income_2019.column('Income'))
ninety_ninth_2019 = percentile(99,income_2019.column('Income'))
high_2019 = np.max(income_2019.column('Income'))

# make a plot
income_2019.where('Income',are.below(ninety_ninth_2019)).hist('Income',unit='Dollar',bins=100)
plots.plot([mean_2019,mean_2019], [0,0.00001], color='red',label='mean')
plots.plot([median_2019,median_2019],[0,0.00001], color='green',label='median')
plots.plot([ninety_ninth_2019,ninety_ninth_2019],[0,0.00001], color='gold',label='99th perc.')
plots.legend(loc='upper center')
plots.title('Some Incomes');


# You can clearly see the right tail in the plot above. It pulls the mean (the red line giving the average income) above the median income (represented by the green line). That is why economists often report median earnings: this is the earning of the "average person" rather than the average earnings of a person (which can be high just because there are a few **very** high income people). Things look pretty rosy for the top 1% in this picture, but they aren't even really on the picture at all! We only plotted the incomes of people in the bottom 99% on the graph above.  Below, we plot **all the incomes**. 

# In[8]:


income_2019.hist('Income',unit='Dollar',bins=100)
plots.plot([mean_2019,mean_2019], [0,0.00001], color='red',label='mean')
plots.plot([median_2019,median_2019],[0,0.00001], color='green',label='median')
plots.plot([ninety_ninth_2019,ninety_ninth_2019],[0,0.00001], color='gold',label='99th perc.')
plots.plot([high_2019,high_2019],[0,0.00001], color='black',label='high')
plots.legend(loc='upper center')
plots.title('All incomes');


# One of the central problems in American society right now is that many people only get their news from a single (often biased) source. Some people only get information from social media outlets, meaning that they only have visibility on what their friends are experiencing. If, like most of us, you have a limited range of friends, then you may be unaware of other people's experiences. This has led to social bubbles, where our experiences are amplified by the echo of social media. Looking at our first histogram of incomes, we might imagine that a person with the median income may see a person earning half a million dollars as incredibly wealthy. However, if that wealthy person only sees the experience of others in the top 1% then they would feel that there are lots of people doing better than them in this economy. Both perspectives are appropriate responses to the data available to each person; we can only get a full picture of the true situation when we look at a massive dataset that is representative of the entire U.S. population. 
