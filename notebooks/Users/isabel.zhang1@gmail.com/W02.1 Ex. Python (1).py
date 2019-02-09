-- Databricks notebook source
-- MAGIC %md # Week 2 - Exercises - Python Essentials

-- COMMAND ----------

-- MAGIC %md ## Contents
-- MAGIC 1. Data lab notebooks
-- MAGIC 1. Lists
-- MAGIC 1. Dictionaries
-- MAGIC 1. Comprehensions
-- MAGIC 1. Map & filter 
-- MAGIC 1. Methods
-- MAGIC 1. JSON

-- COMMAND ----------

Hello_test_2

-- COMMAND ----------

-- MAGIC %md ## Data lab notebooks

-- COMMAND ----------

-- MAGIC %md In the [/Data Lab notebooks/Python/Essentials/Contents](https://bentley.cloud.databricks.com/#notebook/189051)
-- MAGIC notebook you will find links to the remaining notebooks in the _Python Essentials_ folder.
-- MAGIC 
-- MAGIC Please work through and understand __all of the notebooks__ linked to from the above Contents notebook.
-- MAGIC We will work through some of these notebooks during class.
-- MAGIC 
-- MAGIC Complete the exercises in this notebook. 
-- MAGIC All of the code in this notebook and in the notebooks linked to from the above Contents notebook may be asked about in the interviews. 

-- COMMAND ----------

-- MAGIC %md ## Lists

-- COMMAND ----------

-- MAGIC %md __Exercise:__ 
-- MAGIC 1. Create a list that contains all integers greater than or equal to `1` and (strictly) less than `1000000`. Store this list in a varable. Do not display this list.
-- MAGIC 1. Display the last ten elements of this list 

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Store a list in variable `b` below so that the cell returns `True`.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC b = []
-- MAGIC ['a',1] + b == ['a',1,2,'b']

-- COMMAND ----------

Hello_test

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Store a list in variable `c` below so that the cell returns `True`.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC c = []
-- MAGIC 3 * c == [[1,2],[1,2],[1,2]]

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Store a list in variable `d` below so that the cell returns `True`.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC d = []
-- MAGIC d[1:4] == [4,'x',True]

-- COMMAND ----------

-- MAGIC %md ## Dictionaries

-- COMMAND ----------

-- MAGIC %md __Exercise:__ create a dictionary with three keys, `a`, `b`, and `c`. The values should be `11`, `22`, and `33` (respectively).

-- COMMAND ----------

-- MAGIC %md The following code cell creates a dictionary and stores it in variable `europe_cities`.

-- COMMAND ----------

europe_cities = {'spain'  :['madrid', 'barcelona', 'seville', 'valencia'], 
                 'france' :['paris', 'marseille', 'bordeaux'], 
                 'germany':['berlin', 'munich'], 
                 'norway' :['oslo'] }

-- COMMAND ----------

-- MAGIC %md __Exercise:__ retrieve the third city in the list of cities in Spain. Do so with a single command. Do not store temporary results in a variable.

-- COMMAND ----------

-- MAGIC %md ## Comprehensions

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use a list comprehension to display a list of the square of every integer greater than or equal to `0` and (strictly) less than `10`.

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use a list comprehension to display a list of the square of every odd integer greater than or equal to `0` and (strictly) less than `10`.

-- COMMAND ----------

-- MAGIC %md The following code cell creates a dictionary and stores it in variable `europe_cities`.

-- COMMAND ----------

europe_cities = {'spain'  :['madrid', 'barcelona', 'seville', 'valencia'], 
                 'france' :['paris', 'marseille', 'bordeaux'], 
                 'germany':['berlin', 'munich'], 
                 'norway' :['oslo'] }

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use a dictionary comprehension to create and display a dictionary with the same keys as `europe_cities` but with values that are the length of the list for that key in the `europe_cities` dictionary. For instance the value corresponding to the key `spain` will be `4`.

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Write a list comprehension, in or following the next cell, that returns a list containing the four countries from the dictionary `europe_cap_pop`.

-- COMMAND ----------

-- MAGIC %python 
-- MAGIC europe_cap_pop = {'spain'  : { 'capital':'madrid' , 'population':46.77 },
-- MAGIC                   'france' : { 'capital':'paris'  , 'population':66.03 },
-- MAGIC                   'germany': { 'capital':'berlin' , 'population':80.62 },
-- MAGIC                   'norway' : { 'capital':'oslo'   , 'population': 5.84 }}

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Write a list comprehension, in or following the next cell, that returns a list containing the four capitals from the dictionary `europe_cap_pop`.

-- COMMAND ----------

-- MAGIC %python 
-- MAGIC europe_cap_pop = {'spain'  : { 'capital':'madrid' , 'population':46.77 },
-- MAGIC                   'france' : { 'capital':'paris'  , 'population':66.03 },
-- MAGIC                   'germany': { 'capital':'berlin' , 'population':80.62 },
-- MAGIC                   'norway' : { 'capital':'oslo'   , 'population': 5.84 }}

-- COMMAND ----------

-- MAGIC %md ## Map & filter 

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use the `map` function to display a list of the square of every integer greater than or equal to `0` and (strictly) less than `10`. 

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use the `map` and `filter` functions to display a list of the square of every odd integer greater than `0` and (strictly) less than `10`.

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Use the `map` function, in or following the next cell, that returns a list containing the four countries from the dictionary `europe_cap_pop`.

-- COMMAND ----------

-- MAGIC %python 
-- MAGIC europe_cap_pop = {'spain'  : { 'capital':'madrid' , 'population':46.77 },
-- MAGIC                   'france' : { 'capital':'paris'  , 'population':66.03 },
-- MAGIC                   'germany': { 'capital':'berlin' , 'population':80.62 },
-- MAGIC                   'norway' : { 'capital':'oslo'   , 'population': 5.84 }}

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Use either a list comprehension or the `map` and `filter` functions, in or following the next cell, 
-- MAGIC that returns a list containing the capitals of countries with populations over `50` (from the dictionary `europe_cap_pop`).

-- COMMAND ----------

-- MAGIC %python 
-- MAGIC europe_cap_pop = {'spain'  : { 'capital':'madrid' , 'population':46.77 },
-- MAGIC                   'france' : { 'capital':'paris'  , 'population':66.03 },
-- MAGIC                   'germany': { 'capital':'berlin' , 'population':80.62 },
-- MAGIC                   'norway' : { 'capital':'oslo'   , 'population': 5.84 }}

-- COMMAND ----------

-- MAGIC %md ## Methods

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use three methods on the string defined below and describe your results. 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC my_string = "It's a lovely day in the neighborhood."

-- COMMAND ----------

-- MAGIC %md __Exercise:__ use three methods on the list defined below and describe your results.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC my_list = [2, 3, 4, 5, 7, 8, 11, 16]

-- COMMAND ----------

-- MAGIC %md ## JSON 
-- MAGIC 
-- MAGIC See the [/Data Lab notebooks/Python/Essentials/JSON](https://bentley.cloud.databricks.com/#notebook/858024) notebook for JSON examples. 

-- COMMAND ----------

-- MAGIC %md __Exercise:__ create JSON data that stores contact info for the members of your group. (It doesn't need to be real data.)
-- MAGIC This contact data should be a list and each element of the list should be a dictionary. 
-- MAGIC Each dictionary should record the contact info for one person and should include a key called `"name"`.
-- MAGIC - Store this data as a Python string in a variable named `group_json_string` (in the following code cell).

-- COMMAND ----------

-- MAGIC %python
-- MAGIC group_json_string=''

-- COMMAND ----------

-- MAGIC %md __Exercise:__ create and display a list using the `loads` function (from the `json` module) with the JSON data stored in `group_json_string` from the previous exercise as input. 
-- MAGIC - Store the output (of the `loads` function) in a variable named `group_contact_list`.

-- COMMAND ----------

-- MAGIC %md __Exercise:__ create and display a Pandas dataframe using the JSON data, stored in `group_contact_list`. 

-- COMMAND ----------

-- MAGIC %md __Exercise__: Using this file: `/dbfs/mnt/datalab-datasets/file-samples/one_list.json`
-- MAGIC 1. Create, using a `with`-`open` context manager, a list of dictionaries in variable `one_list` (from the above file)
-- MAGIC 1. Display, using a list comprehension, a list of quantities (from `one_list`)
-- MAGIC 1. Display, using a list comprehension, a list of quantities with `100` added to each quantity (from `one_list`)
-- MAGIC 1. Display, using a list comprehension, a list of quantities greater than `250` (from `one_list`)

-- COMMAND ----------

-- MAGIC %md __Exercise__: Using this file: `/dbfs/mnt/datalab-datasets/file-samples/one_list.json`
-- MAGIC 1. Create, using a `with`-`open` context manager, a list of dictionaries in variable `one_list` (from the above file)
-- MAGIC 1. Display, using the `map` function, a list of quantities (from `one_list`)
-- MAGIC 1. Display, using the `map` function, a list of quantities with `100` added to each quantity (from `one_list`)
-- MAGIC 1. Display, using the `map` and `filter` functions, a list of quantities greater than `250` (from `one_list`)

-- COMMAND ----------

-- MAGIC %md __Exercise:__ Some datafiles, such as the file partially displayed below, are stored as a single JSON object. This is acceptable for small files.
-- MAGIC 
-- MAGIC 
-- MAGIC Read in the entire contents of the file using the `load` function of the `json` package. 
-- MAGIC - Display the result of the `load` function. 
-- MAGIC - What type of Python object is the result? Why? 
-- MAGIC %sh head -n 54 /dbfs/mnt/datalab-datasets/file-samples/one_list_with_metadata.json

-- COMMAND ----------

-- MAGIC %md __Exercise (continued):__ Create (and display) a dataframe from (part of) the result of the `load` function in the previous part of this exercise.

-- COMMAND ----------

-- MAGIC %md __The End__