# Python_Notes

Some notes on python with examples.

## Data Structures and Algorithms (look in dsAlgo folder for examples)

### Unpacking a Sequence into Separate Variables
* You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.
* Any sequence or iterable can be unpacked into variables using a simple operator.
* Unpacking actually works with any object that happens to be iterable, not just tuples or lists. This includes strings,
files, iterators, and generators.
* When unpacking, you may sometimes want to discard certain values. Python has no special syntax for this, but you can often
just pick a throwaway variable name `_` or `ign` for it. ex:
```python
data = ['ACME', 50, 81.1, (2012, 12, 21)]
_, shares, price, _ = data
```

### Unpacking elements from iterables of arbitrary length
* You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too many values to unpack"
exception.
* Use Python "star expressions" ===> look at python_notes1.py
* ex:`>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')`
* `>>> name, email, *phone_numbers = record`
* `>>> print(name)`
* `>>> Dave`
* Note: `phone_numbers` variable will always be a list
* It is worth noting that the star syntax can be especially useful when iterating over a sequence of tuples of varying length.
* Star unpacking can also be useful when combined with certain kinds of string processing operations, such as splitting.
* There is a certain similarity between star unpacking and list-processing features of various functional languages. For
example, if you have a list, you can easily split it into head and tail components like this:
```python
items = [1, 4, 2, 4]
head, *tail = items
```
* One could imagine writing functions that perform such splitting in order to carry out some kind of clever recursive algorithm.
```python
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
```
* However, be aware that recursion isn't a strong Python feature due to the inherent recursion limit.

### keeping the last N items
* You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
* keeping a limited history is a perfect use for a `collections.deque` -> look ay python_notes2.py
* When writing code to search for items, it is common to use a generator function involving `yield`. This decouples the
process of searching from the code that uses the results.
* Using `deque(maxlen=N)` creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is
automatically removed.
* although you could manually perform such operations on a list, the queue solution is far more elegant and runs a lot faster.
* More generally, a `deque` can be used whenever you need a simple queue structure. If you don't give it a max size, you
get an unbounded queue that lets you append and pop items on either end.
* adding or popping items from either end of a queue has O(1) complexity. This is unlike
a list where inserting or removing items from the front of the list is O(N).

### finding the largest or smallest N items
* You want to make a list of the largest or smallest N items in a collection.
* the `heapq` module has 2 functions `nlargest()` and `nsmallest()` that do exactly what you want. ===> look at python_notes3.py
* If you are looking for the N smallest or largest items and N is small compared to the overall size of the collection, these 
functions (nlargest, nsmallest) provide superior performance. Underneath the cover, they work by first converting the data
into a list where items are ordered as a heap.
```python
nums = [1, 8, -1, 0, 5]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
# >>>> [-1, 0, 1, 5]
``` 
* the most important feature of a heap is that heap[0] is always the smallest item. Moreover, subsequent items can be easily found 
using the heapq.heappop() method, which pops off the first item and replaces it with the next smallest item (an operation that 
requires O(logN) operations where N is the size of the heap). 
* **`nlargest()` and `nsmallest()` are most appropriate if you are trying to find a relatively small number of items.** 
* **If you are simply trying to find the single smallest and largest item (N=1), it is faster to use min(), max()**
* **similarly if N is about the same size as the collection itself, it's usually faster to sort it first
and take a slice (i.e., use `sorted(items)[:N]` or `sorted(items)[-N:])`.**
* It should be noted that the actual implementation of `nlargest()` and `nsmallest()` is adaptive to how it operates and will
carry out some of the optimizations on your behalf.

### Implementing a Priority Queue
* You want to implement a queue that sorts items by a given priority and always returns the item with the highest priority
on each pop operation. ==> Look at data_structures_and_algorithms/priority_queue.py
* The core of this recipe concerns the use of the `heapq` module. The functions `heapq.heappush()` and `heapq.heappop()`
insert and remove items from a list `_queue` in a way such that the first item in the list has the smallest priority. The
`heappop()` method always returns the "smallest" item, so that is the key to making the queue pop the correct items. Moreover,
since the push and pop operations have O(logN) complexity where N is the number of items in the heap, they are fairly efficient
even for fairly large values of N.
* In this recipe, the queue consists of tuples of the form `(-priority, index, item)`. The `priority` value is negated to get
the queue to sort items from highest priority to lowest priority. This is opposite of the normal heap ordering, which sorts
from lowest to highest value.
* The role of the `index` variable is to properly order items with the same priority level. By keeping a constantly increasing
index, the items will be sorted according to the order in which they were inserted. However, the index also serves as an important
role in making the comparison operations work for items that have the same priority level.
* If you want to use this queue for communication between threads, you need to add appropriate locking and signaling.

### mapping keys to multiple values in a dictionary
* You want to make a dictionary that maps keys to more than one value (a so-called "multidict").
* a dictionary is a mapping where each key is mapped to a single value. If you want to map keys to multiple values,
you need to store the multiple values in another container such as a list or set. -> look at multidict.py
```python
d = {
  'a': [1, 2, 3],
  'b': [4, 5]
}
e = {
  'a': {1, 2, 3},
  'b': {4, 5}
}
```
* Use a list if you want to preserve the insertion order of the items.
* Use a set if you want to eliminate duplicates (and don't care about the order).
* to easily construct such dictionaries, you can use `defaultdict` in the `collections` module. A feature of `defaultdict`
is that it automatically initializes the first value so you can simply focus on adding items. One caution with `defaultdict` is that
it will automatically create dictionary entries for keys accessed later on (even if they aren't currently found in the dictionary).
If you don't want this behavior, you might use `setdefault()` on an ordinary dictionary instead. For example
```python
d = {} # a regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('c', []).append(1)
```
* However, many programmers find `setdefault()` to be a little unnatural--not to mention the fact that it always creates
a new instance of the initial value on each invocation (the empty list `[]` in the example above).

### keeping dictionaries in order
* You want to create a dictionary, and you also want to control the order of items when iterating or serializing.
* to control the order of items in a dictionary, you can use an `OrderedDict` from the collections module. It exactly
  preserves the original insertion order of data when iterating.  ==> look at dict_notes.py
```python
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
```
* An `OrderedDict` can be particularly useful when you want to build a mapping that you may want to later serialize or encode
into a different format. For example, if you want to precisely control the order of fields appearing in a JSON encoding, first
building the data in an `OrderedDict` will do the trick.
```python
import json
json.dump(d)
```
* An `OrderedDict` internally maintains a doubly linked list that orders the keys according to insertion order. When a
  new item is first inserted, it is placed at the end of this list. Subsequent reassignment of an existing key doesn't change
  the order.
* be aware that the size of an OrderedDict is more than twice as large as a normal dictionary due to the extra linked
  list that's created. Thus, if you are going to build a data structure involving a large number of `OrderedDict` instances
  (e.g., reading 100,000 lines of a CSV file into a list of `OrderedDict` instances), you would need to study the requirements
  of your application to determine if the benefits of using an `OrderedDict` outweighed the extra memory overhead.

### calculating with dictionaries
* You want to perform various calculations (e.g., minimum value, maximum value, sorting, etc.) on a dictionary of data.
* in order to perform useful calculations on the dictionary contents, it is often useful to invert the keys and values
of the dictionary using `zip()` For example ==> look at dict_notes.py 
```python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# In order to perform useful calculations on the dictionary contents, it is often useful to invert the keys and values of
# the dictionary using zip(). For example, find the min and max price and stock name
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
# Similarly to rank the data, use zip() with sorted()
prices_sorted = sorted(zip(prices.values(), prices.keys()))
 
```
* **be aware that zip() creates an iterator that can only be consumed once.**
* If you try to perform data reductions on a dictionary, you'll find that they only process the keys, not the values.
You can fix this by using the `values()` method of a dictionary, but then you don't get the keys.
* You can get the key corresponding to the min or max value if you supply a key function to `min()` and `max()`. However,
to get the minimum value, you'll need to perform an extra lookup step.
```python
prices = {}
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])
min_value = prices[min(prices, key=lambda k: prices[k])]
```
* Using zip solves this problem by "inverting" the dictionary into a sequence of `(value, key)` pairs. When performing 
comparisons on such tuples, the `value` element is compared first, followed by the `key`. This gives you exactly the behavior 
that you want and allows reductions and sorting to be easily performed on the dictionary contents using a single statement.
* It should be noted that in calculations involving `(value, key)` pairs, the key will be used to determine the result in
instances where multiple entries happen to have the same value. For instance, in calculations such as `min()` and `max()`,
the entry with the smallest or largest key will be returned if there happen to be duplicate values. 

### finding commonalities in two dictionaries
* You have two dictionaries and want to find out what they might have in common (same keys, values, etc.).
* to find out what two dictionaries have in common, simply perform common set operations using the `keys()` or `items()` methods**
For example, ===> look in dict_notes.py
```python
a = {'x':1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
# Find keys in common
common_keys = a.keys() & b.keys() # {'x', 'y'}
# Find keys in a that are not in b
a_not_in_b = a.keys() - b.keys() # {'z'}
# Find (key, value) pairs in common
common_items = a.items() & b.items() # {('y', 2)}
```
* These kinds of operations can also be used to alter or filter dictionary contents. For example, suppose you want to make a
new dictionary with selected key words removed. For example using dictionary comprehension
```python
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
```
* a dictionary is a mapping between a set of keys and values. The `keys()` method of a dictionary returns a keys-view object
that exposes the keys. A little-known feature of keys views is that they also support common set operations such as unions,
intersections and differences.
* the `items()` method of a dictionary returns an items-view object consisting of (`key`, `value`) pairs. This object supports
similar set operations and can be used to perform operations such as finding out which key-value pairs two dictionaries have
in common.
* although similar, the `values()` method of a dictionary does not support the set operations described in this recipe. In part,
this is due to the fact that unlike keys, the items contained in the values view aren't guaranteed to be unique. However, if you
must perform such calculations, they can be accomplished by simply converting the values to a set first.

### removing duplicates from a sequence while maintaining order
* You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items
* If the values in a sequence are hashable, the problem can be easily solved using a set and a generator. For example:
```python
def dedupe(items):
  seen = set()
  for item in items:
    if item not in seen:
      yield item
      seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
a_d = list(dedupe(a))
```
* This only works if the items in the sequence are hashable. If you are trying to eliminate duplicates in a sequence of unhashable
types (such as dicts), you can make a slight change to the recipe
```python
def dedupe(items, key=None):
  seen = set()
  for item in items:
    val = item if key is None else key(item)
    if val not in seen:
      yield item
      seen.add(val)
# Here the purpose of the key argument is to specify a function that converts a sequence of items into a hashable type for the
# purposes of duplicate detection
a = [{'x':1,'y':2}, {'x':1,'y':3}, {'x':1,'y':2}, {'x':2,'y':4},]
a_d = list(dedupe(a, key=lambda d: (d['x', d['y']])))
a_d2 = list(dedupe(a, key=lambda d: d['x']))
```
* If all you want to do is eliminate duplicates, it is often easy enough to make a set. For example
```python
a = [1, 2, 1, 3, 1, 2, 1, 4]
a_d = set(a)
```
* However, this approach doesn't preserve any kind of ordering. So, the resulting data will be scrambled afterward. The solution
above avoids this.
* The use of a generator function in this recipe reflects the fact that you might want the function to be extremely general
purpose--not necessarily tied directly to list processing. For example, if you want to read a file, eliminating duplicate lines,
you could simply do this:
```python
with open(somefile, 'r') as f:
  for line in dedupe(f):
    # ...
```
* The specification of a `key` function mimics similar functionality in built-in functions such as `sorted()`, `min()`, and `max()`.

### naming a slice
* Your program has become an unreadable mess of hardcoded slice indices and you want to clean it up.
* Suppose you have some code that is pulling specific data fields out of a record string with fixed fields (e.g., from a flat file or similar format):
```python
# 01234567891011121314151617181920
record = '..........100       ....513.25    .......'
SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = int(record[SHARES]) * float(record[PRICE])
```
* This way you avoid having a lot of mysterious hardcoded indices, and what you're doing becomes much clearer
* If you have a `slice` instance `s`, you can get more information about it by looking at its `s.start`, `s.stop`, and `s.step`
attributes respectively.
* In addition, you can map a slice onto a sequence of a specific size by using its `indices(size)` method. This returns a
tuple `(start, stop, step)` where all values have been suitably limited to fit within bounds (as to avoid `IndexError` exceptions
when indexing). For example
```python
s = 'Hello World'
a = slice(10, 50, 2)
a_2 = a.indices(len(s))
for i in range(*a_2):
  print(i)
```

### determining the most frequently occurring items in a sequence
* You have a sequence of items, and you'd like to determine the most frequently occurring items in the sequence.
* The `collections.Counter` class is designed for just such a problem. It even comes with a handy `most_common()` method that will
  give you the answer.
* To illustrate, let's say you have a list of words and you want to find out which words occur most often.
```python
words = [
     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
```
* As input, `Counter` objects can be fed any sequence of hashable input items. Under the covers, a `Counter` is a dictionary
that maps the items to the number of occurrences. For example: `print(word_counts['not']) # 1`. If you want to increment the
count manually, simply use addition: `word_counts[word] += 1`. Or alternatively you could use the `update()` method:
`word_counts.update(morewords)`
* A little known feature of `Counter` instances is that they can easily combined using various mathematical operations. For example:
```python
a = Counter(words)
b = Counter(morewords)
# Combine counts
c = a + b
# Subtract counts
d = a - b
```
* Needless to say, `Counter` objects are a tremendously useful tool for almost any kind of problem where you need to tabulate
and count data. You should prefer this over manually written solutions involving dictionaries.

### sorting a list of dictionaries by a common key
* You have a list of dictionaries and you would like to sort the entries according to one or more of the dictionary values.
* sorting this type of structure is easy using the `operator` module's `itemgetter()` function. ===> look at sortingListOfDicts.py
* the `itemgetter()` function can also accept multiple keys
* If you give multiple indices to `itemgetter()`, the callable it produces will return a tuple with all the elements in it, and
`sorted()` will order the output according to the sorted order of the tuples.
* The functionality of `itemgetter()` is sometimes replaced by `lambda` expressions. For example
```python
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
```
* this technique can applied also to `min()` and `max()`

### sorting objects without native comparison support
* You want to sort objects of the same class, but they don't natively support comparison operations.
* The built in `sorted()` function takes a key argument that can be passed a callable that will return some value in the object
  that `sorted` will use to compare the objects. For example, if you have a sequence of User instances in your application, and
  you want to sort them by their `user_id` attribute, you would supply a callable that takes a User instance as input and
  returns the `user_id`. ex:
```python
class User:
  def __init__(self, user_id):
    self.user_id = user_id
  def __repr__(self):
    return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(9)]
sorted(users, key=lambda u: u.user_id)
```
* instead of using `lambda`, an alternative approach is to use `operator.attrgetter()`
* the choice of whether or not to use `lambda` or `attrgetter()` may be one of personal preference. However, `attrgetter()`
is often a tad bit faster and also has the added feature of allowing multiple fields to be extracted simultaneously. This
is analogous to the use of `operator.itemgetter()` for dictionaries. For example, if `User` instances also had a `first_name`
and `last_name` attribute, you could perform a sort like this: `by_name = sorted(users, key=attrgetter('last_name', 'first_name'))`
* It is also worth noting that the technique used in this recipe can be applied to functions such as `min()` and `max()`
* note: `sorted()` returns a new list, unlike `list_name.sort()` sorts items in place

### Grouping records together based on a field
* You have a sequence of dictionaries or instances and you want to iterate over the data in groups based on the value of
a particular field, such as date.
* the `itertools.groupby()`function is particularly useful for grouping data together like this. To illustrate, suppose you
have the following list of dictionaries:
```python
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# Now suppose you want to iterate over the data in chunks grouped by date. To do it, first sort by the desired field (in this case date)
# and then use itertools.groupby()
from operator import itemgetter
from itertools import groupby

# sort by the desired field first
rows.sort(key=itemgetter('date'))

# iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
  print(date)
  for i in items:
    print(' ', i)
```
* The `groupby()` function works by scanning a sequence and finding sequential "runs" of identical values (or values returned
by the given key function). On each iteration it returns the value along with an iterator that produces all of the items in a 
group with the same value.
* An important preliminary step is sorting the data according to the field of interest. Since `groupby()` only examines
consecutive items, failing to sort first won't group the records as you want.
* If your goal is to simply group the data together by dates into a large data structure that allows random access, you may
have better luck using `defaultdict()` to build a multidict, as described in earlier. It's not necessary to sort the records
first. Thus, if memory is no concern, it may be faster to do this than to first sort the records and iterate using `groupby()`

### filtering sequence elements
* You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.
* the easiest way to filter sequence data is often to use a list comprehension, ===> look at filtering_sequence.py
```python
my_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
my_list2 = [n for n in my_list if n > 0]

```
* one potential downside of using a list comprehension is that it might produce a large result if the original input is large.
If this is concern, you can use generator expressions to produce the filtered values iteratively. ex: `pos = (n for n in mylist if n > 0)`
* sometimes, the filtering criteria cannot be easily expressed in a list comprehension or generator expression. For
  example, suppose that the filtering process involves exception handling or some other complicated detail. For this
  put the filtering code into its own function and use the built-in `filter()` function 
```python
values = ['1', '2', '3', '-', '4', 'N/A', 'S']
def is_int(val):
  try:
    x = int(val)
    return True
  except ValueError:
    return False
ivals = list(filter(is_int, values))
print(ivals)
```
* `filter()` creates an iterator, so if you want to create a list of results, make sure you also use `list()`
* List comprehensions and generator expressions are often the easiest and most straightforward ways to filter simple data. They
also have the added power to transform the data at the same time. ex: `[math.sqrt(n) for n in my_list if n > 0]`
* One variation on filtering involves replacing the values that don't meet the criteria with a new value instead of discarding
  them. For example, perhaps instead of just finding positive values, you want to also clip bad values to fit within a specified
  range. This is often easily accomplished by moving the filter criterion into a conditional expression like this:
`clip_pos = [n if n < 0 else 0 for n in my_list]`
* Another notable filtering tool is `itertools.compress()`, which takes an iterable and an accompanying Boolean selector sequence
  as input. As output, it gives you all of the items in the iterable where the corresponding element in the selector is `True`.
  This can be useful if you're trying to apply the results of filtering one sequence to another related sequence. For example,
  suppose you have the following two columns of data.
```python
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

# list of all addresses where the corresponding count value was greater than 5
from itertools import compress
more5 = [n > 5 for n in counts] # [False, False, True, False, False, True, True, False]
x = list(compress(addresses, more5)) # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
```
* the key here is to first create a sequence of Booleans that indicates which elements satisfy the desired condition. The
`compress()` function then picks out the items corresponding to `True` values.
* like `filter()`, `compress()` normally returns an iterator. Thus, you need to use `list()` to turn the results into a list if desired.

### extracting a subset of a dictionary
* You want to make a dictionary that is a subset of another dictionary.
* this is easily accomplished using dictionary comprehension ===> look at filtering_sequence.py
```python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}

# make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
```

### mapping names to sequence elements
* Problem: You have code that accesses list or tuple elements by position, but this makes the code somewhat difficult to read
  at times. You'd also like to be less dependent on position in the structure, by accessing the elements by name.
* `collections.namedtuple()` provides these benefits while adding minimal overhead over using a normal tuple object.
  `collections.namedtuple()` is actually a factory method that returns a subclass of the standard python tuple type. You feed it a type name, 
  and the fields it should have, and it returns a class that you can instantiate, passing in values for the 
  fields you have defined, and so on.
* Although an instance of a namedtuple looks like a normal class instance, it is interchangeable with a tuple and supports
  all of the usual tuple operations such as indexing and unpacking.
```python
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('email@email.com', '2012-10-19')
print(len(sub)) # 2
addr, joined = sub
print(addr, joined) # email@email.com 2012-10-19
```
* A major use case for named tuples is decoupling your code from the position of the elements it manipulates. So, if you get
  back a large list of tuples from a database call, then manipulate them by accessing the positional elements, your code could
  break if, say, you added a new column to your table. Not so if you first cast the returned tuples to namedtuples. References
  to positional elements often make the code a bit less expressive and more dependent on the structure of the records. Naturally,
  you can avoid the explicit conversion of the Stock namedtuple if the records sequence in the example already contained such
  instances. For ex:
```python
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
  total = 0.0
  for rec in records:
    s = Stock(*rec)
    total += s.shares * s.price
  return total
```
* One possible use of a namedtuple is as a replacement for a dictionary, which requires more space to store. Thus, if you are 
  building large data structures involving dictionaries, use of a namedtuple will be more efficient. However, be aware that
  unlike a dictionary, a namedtuple is immutable.
* If you need to change any of the attributes, it can be done using the `_replace()` method of a namedtuple instance, which
  makes an entirely new namedtuple with specified values replaced. 
* A subtle use of the `_replace()` method is that it can be a convenient way to populate named tuples that have optional or
  missing fields. To do this, you make a prototype tuple containing the default values and then use `_replace()` to create
  new instances with values replaced.
* Last, but not least, it should be noted that if your goal is to define an efficient data structure where you will be
  changing various instance attributes, using namedtuple is not your best choice, instead consider defining a class using
  `_slots_` 

### Transforming and Reducing Data at the same time
* You need to execute a reduction function (e.g., `sum()`, `min()`, `max()`), but first need to transform or filter the data.
* A very elegant way to combine a data reduction and a transformation is to use a generator-expression argument.
  ====> look at generator_expression.py
* For example, if you want to calculate the sum of squares, do the following:
```python
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be Python!')
else:
    print('Sorry, no Python :(')
    
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
{'name': 'GOOG', 'shares': 50},
{'name': 'YHOO', 'shares': 75},
{'name': 'AOL', 'shares': 20},
{'name': 'SCOX', 'shares': 65},
]
min_shares = min(s['shares'] for s in portfolio)
```
* Using a generator argument is often a more efficient and elegant approach than first creating a temporary list.
  For a small list, it might not matter, but if nums was huge, you would end up creating a large temporary data structure
  to only be used once and discarded. The generator solution transforms the data iteratively and is therefore much more
  memory efficient.
* Certain reduction functions such as min and max accept a key argument that might be useful in situations where you might
  be inclined to use a generator. For example
```python
# Original: Returns 28
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
```

### Combining multiple mappings into a single mapping
* You have multiple dictionaries or mappings that you want to logically combine into a single mapping to perform certain operations,
such as looking up values or checking for the existence of keys.
* Suppose you want to perform lookups where you have to check 2 dictionaries. An easy way to do this is to use the `ChainMap`
class from the `collections` module. ==> look at dict_notes.py
```python
a = {'x': 1}
b = {'y': 2}
from collections import ChainMap
c = ChainMap(a, b)
print(c['x']) # 1
```
* A `ChainMap` takes multiple mappings and makes them logically as one. However, the mappings are not literally merged together.
Instead a `ChainMap` simply keeps a list of the underlying mappings and redefines common dictionary operations to scan the list.
Most operations will work, for example: `len(c)`, `list(c.keys())`, `list(c.values())`
* **If there are multiple keys, the values from the first mapping get used.**
* **Operations that mutate the mapping always affect the first mapping listed.**
* A `ChainMap` is particularly useful when working with scoped values such as variables in a programming language (i.e., globals, locals, etc).
In fact, there are methods that make this easy:
```python
from collections import ChainMap
values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['y'] = 2

# values: ChainMap({'x': 1}, {'y': 2})

# Discard last mapping
values = values.parents

# values: ChainMap({'x': 1})
```
* An alternative to `ChainMap`, you might consider merging dictionaries together using the `update()` method. For example
```python
a = {'x': 1}
b = {'y': 2}
merged = dict(b)
merged.update(a)
```
* This works, but requires you to make a completely separate dictionary object (or destructively alter one of the existing
dictionaries). Also, if any of the original dictionaries mutate, the changes don't get reflected in the merged dictionary.
A `ChainMap` uses the original dictionaries, so it doesn't have this behavior.

### Python slicing
* If you want to reverse an array using slicing ex: a[::-1]
* beg:end:increment

## Strings and Text (look in the stringText folder for examples)

### Splitting strings on any of multiple of delimeters (so common omg)
* Suppose you want to split a string into fields, but the delimeters and spacing around them aren't consistent throughout the
string.
* the split() method of string objects is really meant for very simple cases, and does not allow for multiple delimeters or account for 
possible whitespace around the delimeters. In cases when you need a bit more flexibility, use the re.split() method. (look in split.py)
* the result is a list of fields

### Matching text at the start or end of the string
* A simple solution is to use the str.startswith() or str.endswith() methods
* If you need to check against multiple choices, simply provide a tuple of possibilities to startswith() or endswith()

### Matching strings using shell wildcard patterns
* You want to match text using the same wildcard patterns as are commonly used when working in unix shells (e.g, *.py, Dat[0-9]*.csv, etc)
* the fnmatch module provides two functions-- fnmatch() and fnmatchcase()--that can be used to perform such matching.
* the matching performed by fnmatch sits somewhere between the functionality of simple string methods and the full power of regular expressions. If you are just trying to provide a simple mechanism for allowing wildcards in data processing applications, it's often a reasonable solution. If you're actually trying to write code that matches filenames, use the glob module instead.

### Matching and searching for text patterns
* If the text you're trying to match is a simple literal, you can often just use the basic string methods, such as str.find(), str.endswith(), str.startswith()
* For more complicated matching, use regular expressions and the re module. ==> look at matchingSearchin.py
* if you are going to perform a lot of matches using the same pattern, it usually pays to precompile the regular expression pattern into a pattern object first
* match() always tries to find the match at the start of the string. If you want to search text for all occurrences of a pattern, use the findall() method instead
* when defining regular expressions, it is common to introduce capture groups by enclosing parts of the pattern in parentheses.
Capture groups often simplify subsequent processing of the matched text because the contents of each group can be extracted individually.
* the findall() method searches the text and finds all matches, returning them as a list. If you want to find matches iteratively, use the finditer() method instead.
* **Note** Be aware that the match method only checks the begining of a string. If you want an exact match, make sure the pattern includes the end-marker ($).
* If you're just doing a simple text matching/searching operation, you can often skip the compilation step and use module-level functions in the re module instead. Be aware though, 
that if you are going to perform a lot of matching or searching, it usually pays to compile the pattern first and use it over and over again. The module-level functions keep a cache 
of recently compiled patterns, so there isn't a huge performance hit, but you'll save a few lookups and extra processing by using your own compiled pattern. 

### Searching and replacing text
* For simple literal patterns, use the str.replace() method.
* For more compilcated patterns, use the sub() functions in the re module.  ==> look at matchingSearchin.py
* For more complicated substitutions, it's possible to specify a substitution callback function instead. The function should return the replacement text. 
* If you want to know how many substitutions were made in addition to getting the replacement text, use re.subn() instead.

### Searching and replacing case-insensitive text.
* To perform case-insensitive text operations, you need to use the re module and supply the re.IGNORECASE flag to various operations. ==> look at matchingSearch.py 

### Specifying a regular expression for the shortest match
==> look at matchingSearch.py

### Writing a regular expression for multiline patterns
* this problem arises in patterns that use the dot to match any character but forget to account for the fact that it doesn't match newlines. 
* to fix this problem you can add support for newlines ex: re.compile(r'/\*((?:.|\n)*?)\*/')
* In this pattern, (?:.|\n) specifies a noncapture group (i.e it defines a group for the purposes of matching, but that group is not captured seperately or numbered).

### Normalizing unicode text to a standard representation
* In unicode, certain characters can be represented by more than one valid sequence of code points. Having multiple representations is a problem for programs that compare strings. In order to fix this, you should first normalize the text into a standard representation using the unicodedata module.
* The first argument to normalize() specifies how you want the string normalized. NFC means that characters should be fully composed (i.e, use a single code point if possible). NFD means that characters should be fully decomposed with the use of combining characters. Python also supports the normalization forms NFKC and NFKD, which add extra compatibility features for dealing with certain kinds of characters.

### Working with unicode characters in regular expressions
* By default, the re module is already programmed with rudimentary knowledge of certain Unicode character classes. For example, \d already matches any unicode digit character.
* If you need to include specific unicode character patterns, you can use the usual escape sequence for unicode characters.
* **Important** When performing matching and searching operations, its a good idea to normalize and possibly sanitize all text to a standard form first. 
* you should consider installing the 3rd party regex library

### Stripping unwanted characters from strings
* the strip() method can be used to strip characters from the beginning or end of a string.lstrip() and rstrip() perform stripping from the left or right side. By default, these methods strip whitespace, but other characters can be given.
* be aware that stripping does not apply to any text in the middle of a string.
* if you needed to do something to the inner space, you would need to use another technique, such as using the replace() method or a regular expression substitution.
* **Important** It is often the case that you want to combine string stripping operations with some other kind of iterative processing, such as reading lines of data from a file. If so, this is one area where a generator expression can be useful. ex: 
``` python
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
      
```
* here, the expression lines = (line.strip() for line in f) acts as a kind of data transform. It's efficient because it doesn't actually read the data into any kind of temporary list first. It just creates an iterator where all of the lines produced have the stripping operation applied to them.

### Sanitizing and cleaning up text
* The problem of sanitizing and cleaning up text applies to a wide variety of problems involving text parsing and data handling. At a very simple level, you might use basic string functions (str.upper() and str.lower()) to convert text to a standard case. Simple replacements using str.replace() or re.sub() can focus on removing or changing very specific character sequences. You can also normalize text using unicodedata.normalize().
* However, you might want to take the sanitation process a step further. Perhaps, for example, you want to eliminate whole ranges of characters or strip diacritical marks. To do so, you can use the str.translate() method. ===> Look at sanitize.py
* A major issue with sanitizing text can be runtime performance. As a general rule, the simpler it is, the faster it will run. Only use it if you need to perform any kind of nontrivial character-to-character remapping or deletion.
* Although the focus has been text, similar techniques can be applied to bytes, including simple replacements, translation, and regular expressions.

### Aligning text strings
* You need to format text with some sort of alignment applied. ==> look at stringText/alignment.py
* For basic alignment of strings, the `ljust()`, `rjust()`, and `center()` methods of strings can be used.
* Above methods also accept an optional fill character ex: `text.rjust(20, '=')` produces `****Hello World****`
* the format() function can also be used to easily align things. All you need to do is use the `<`, `>`, or `^` characters along with a desired width.
```python
text = 'Hello World'
text = format(text, '>20')
# >>> '      Hello World'

text = format(text, '<20')
# >>>> 'Hello World     '

text = format(text, '^20')
# >>>> '     Hello World     '
```
* You can also specify a fill character. ex: `format(text, '=>20s')`
* These format codes can also be used in the `format()` method when formatting multiple values
```python
t = '{:>10s} {:>10s}'.format('Hello', 'World')
# >>> '    Hello     World'
```
* One benefit of `format()` is that it is not specific to strings. It works with any value, making it more general purpose.
For instance, you can use it with numbers:
```python
x = 1.2345
y = format(x, '>10')
# >>> '    1.2345'
z = format(x, '^10.2f')
# >>>> '   1.23   '
```
* In older code, you will also see the % operator be used however in newer code you should use the format() method since it is more powerful

### Combining and concatenating strings
* You want to combine many small strings together into a larger string. ===> Look at stringText/combiningConcatenating.py
* If the strings you wish to combine are found in a sequence or iterable , the fastest way to combine them is to use the `join()` method. 
```python
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s = ' '.join(parts)
```
* At first glance the syntax might look really odd, but the `join()` operation is specified as a method on strings. Partly this is
because the objects you want to join could come from any number of different data sequences (e.g., lists, tuples, dicts, files,
sets, or generators), and it would be redundant to have `join()` implemented as a method on all those objects separately. So you
just specify the separator string that you want to use and use the `join()` method on it to glue text fragments together.
* If you are combining a few strings, usually `+` usually works well enough
* **If you are trying to combine string literals together in source code, you can simply place them adjacent to each other
with no `+` operator.**
* Joining strings together is often an area where programmers make programming choices that severely impact the performance of their
code. *The most important thing to know is that using the `+` operator to join a lot of strings together is grossly inefficient
due to the memory copies and garbage collection that occurs.* In particular, you never want to write code that joins strings
together like this:
```python
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s = ''
for p in parts:
    s += p
```
* This runs quite a bit slower than using `join()` method, mainly because each `+=` operation creates a new string object. You're
better off just collecting all of the parts first then joining them together at the end.
* One related (and pretty bad) trick is the conversion of data to strings and concatenation at the same time using a generator
expression, for example
```python
data = ['ACME', 50, 91.1]
s = ','.join(str(d) for d in data)
```
* Also be on the lookout for unnecessary string concatenations. Sometimes programmers get carried away with concatenation when
it's really not technically necessary. For example, when printing
```python
a = '1'
b = '2'
c = '3'
print(a + ':' + b + ':' + c) # ugly
print(':'.join([a, b, c])) # still ugly
print(a, b, c, sep=':') # better
```
* Mixing I/O operations and string concatenation is something that might require study in your application. For example, consider
the following two code fragments
```python
# version 1 (string concatenation)
f.write(chunk1 + chunk2)

# version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)
```
* If the two strings are small, the first version might offer much better performance due to the inherent expense of carrying
out an I/O system call. On the other hand, if the two strings are large, the second version may be more efficient, since it
avoids making a large temporary result and copying blocks of memory around.
* Last but not least, if you're writing code that is building output from lots of small strings, you might consider writing
that code as a generator function, using `yield` to emit fragments. For example
```python
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Not Chicago'
```
* The interesting things about this approach is that it makes no assumption about how the fragments are to be assembled together.
For example, you can simply join the fragments using `join()` ==> `text = ''.join(sample())`
* Or you can direct the fragments to I/O
```python
for part in sample():
    f.write(part)
```
* Or you could come up with some kind of hybrid scheme that's smart about combining I/O operations:
```python
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            
for part in combine(sample(), 32768):
    f.write(part)
```
* The key point is that the original generator function doesn't have to know the precise details. It just yields the parts.

### Interpolating variables in strings
* Python has no direct support for simply substituting variable values in strings. However, this feature can be approximated using the format() method of strings.
  =====> see string/Text/combininhConcatenating.py
  
  
  
  
### Performing Text operations on Byte strings
You want to perform common text operations (e.g., stripping, searching, and replacement) on byte strings
* Byte strings already support most the same built-in operations as text strings. For example:
```python
data = b'Hello World'
s = data[0:5] # b'Hello'
s2 = data.startswith(b'Hello') # True
s3 = data.split() # [b'Hello', b'World']
s4 = data.replace(b'Hello', b'Hello cruel') # b'Hello cruel World'
```
* Such operations also work with byte arrays. For example:
```python
data = bytearray(b'Hello World')
d = data[0:5] # bytearray(b'Hello')
d2 = data.startswith(b'Hello') # True
d3 = data.split() # [bytearray(b'Hello'), bytearray(b'World')]
d4 = data.replace(b'Hello', b'Hello cruel') # bytearray(b'Hello cruel World')
```
* You can apply regular expression pattern matching to byte strings, but the patterns themselves need to be specified as
bytes. For example
```python
import re
data = b'FOO:BAR,SPAM'
ds = re.split(b'[:,]', data) # [b'FOO', b'BAR', b'SPAM']
```
* Almost all of the operations available on text strings will work on byte strings. However, there are a few notable differences
to be aware of.
  * First, indexing of byte strings produces integers, not individual characters
  * Second, byte strings don't provide a nice string representation and don't print cleanly unless first decoded into a text string.
  ```python
  s = b'Hello World'
  print(s) # b'Hello World'
  print(s.decode('ascii')) # Hello World
  ```
    * Similarly, there are no string formatting operations available to byte strings.
  * Finally, you need to be aware that using a byte string can change the semantics of certain operations--especially those
  related to the filesystem. For example, if you supply a filename encoded as bytes instead of a text string, it usually
  disables filename encoding/decoding.
 
* Some programmers might be inclined to use byte strings as an alternative to text strings due to a possible performance improvement.
Although it's true that manipulating bytes tends to be slightly more efficient than text (due to the inherent overhead related to
Unicode), doing so usually leads to very messy and non idiomatic code. You'll often find that byte strings don't play well
with a lot of other parts of Python, and that you end up having to perform all sorts of manual encoding/decoding operations
yourself to get things to work right. Frankly, if you're working with text, use normal text strings in your program, not byte strings.

## Numbers, Dates and Times
### Rounding numerical values
* You want to round a floating-point number to a fixed number of decimal places.
* For simple rounding, use the built-in `round(value, ndigits)` function
* When a value is exactly halfway between two choices, the behaviour of round is to round to the nearest even digit. That is, values such as
  1.5 or 2.5 both get rounded to 2.
* The number of digits given to round() can be negative, in which case rounding takes place for tens, hundreds, thousands, and so on.
* Don't confuse rounding with formatting a value for output. You can just specify the desired precision when formatting.
```python
x = 1.23456
print(format(x, '0.2f'))
print('value is {:0.3f}'.format(x))
```
* Also, resist the urge to round floating-point numbers to "fix" perceived accuracy problems. For example, you might be
inclined to do this.
```python
a = 2.1
b = 4.2
c = a + b # 6.30000001
c = round(c, 2) # "fix" result?
print(c) # 6.3
```
* For most applications involving floating point, it's simply not necessary (or recommended) to do this. Although there
are small errors introduced into calculations, the behaviors of these errors are understood and tolerated. If avoiding
such errors is important (e.g, in financial applications, perhaps), consider the use of the `decimal` module.

### Performing accurate decimal calculations
You need to perform accurate calculations with decimal numbers, and don't want the small errors that naturally occur with
floats.
* A well-known issue with floating-point numbers is that they can't accurately represent all base-10 decimals. Moreover,
even simple mathematical calculations introduce small errors. For example:
```python
a = 4.2
b = 2.1
c = a + b # 6.300000000000001
```
* These errors are a "feature" of the underlying CPU and the IEEE 754 arithmetic performed by its floating-point unit.
Since Python's float data type stores data using the native representation, there's nothing you can do to avoid such errors
if you write your code using `float` instances.
* If you want more accuracy (and are willing to give up some performance), you can use the `decimal` module:
```python
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
c = a + b # Decimal('6.3')
print(c) # 6.3
```
* A major feature of `decimal` is that it allows you to control different aspects of calculations, including number of
digits and rounding. To do this, you create a local context and change its settings. ex:
```python
from decimal import localcontext, Decimal
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b) # 0.7647058823529411764705882353
with localcontext() as ctx:
  ctx.prec = 3
  print(a/b) # 0.765
``` 
* The `decimal` module implements IBM's "General Decimal Arithmetic Specification." 
* Newcomers to Python might be inclined to use the `decimal` module to work around perceived accuracy problems with the
`float` data type. However, it's really important to understand your application domain. If you're working with science
or engineering problems, computer graphics, or most things of a scientific nature, it's simply more common to use the
normal floating-point type. For one, very few things in the real world are measured to the 17 digits of accuracy that
floats provide. Thus, tiny errors introduced in calculations just don't matter. Second, performance of native floats is
significantly faster--something that's important if you're performing a large number of calculations.
* That said, you can't ignore the errors completely. Mathematicians have spent a lot of time studying various algorithms,
and some handle errors better than others. You also have to a little careful with effects due to things such as subtractive
cancellation and adding large and small numbers together. ex:
```python
nums = [1.23e+18, 1, -1.23e+18]
s = sum(nums) # notice how 1 disappears
print(s) # 0
```
* This latter example can be addressed by using a more accurate implementation in `math.fsum()`.
* However, for other algorithms, you really need to study the algorithm and understand its error propagation properties.
* All of this said, the main use of the `decimal` module is in programs involving things such as finance. In such programs,
it's extremely annoying to have small errors creep into calculation. It is also common to encounter `Decimal` objects when
Python interfaces with databases--again, especially when accessing financial data. 

### Picking things at random
* the random module has various functions for random numbers and picking random items.
* For example, to pick a random out of a sequence, use random.choice()
* To take a sampling of N items where selected items are removed from further consideration, use random.simple() instead.
* If you simply want to shuffle items in a sequence in place, use random.shuffle()
* To produce random integers use random.randint(0, 10)
* To produce uniform floating-point values in the range 0 to 1, use random.random()
* To get N random-bits expressed as an integer, use random.getrandbits()
* The random module computes random numbers using the Mersenne Twister Algorithm. This is a deterministic algorithm, but you can alter the
initial seed by using the random.seed() function.
* In addition to the functionality above, random() includes functions for uniform, Gausian, and other probability distributions. Functions in
random() **SHOULD NOT** be used in programs related to cryptography. If you need such functionality, consider using functions in the ssl module instead.

### Converting Strings into Datetimes
* Your application receives temporal data in string format, but you want to convert those strings into `datetime` objects in
order to perform nonstring operations on them.
* Python's standard `datetime` module is typically the easy solution for this. ===> Look at numbers_dates_time/date_timez.py
* The `datetime.strptime()` method supports a host of formatting codes, like `%Y` for the four-digit year and `%m` for the
two-digit month. It's also worth noting that these formatting placeholders also work in reverse, in case you need to represent
a `datetime` object in string output and make it look nice. For example, let's say you have some code that generates a datetime
object, but you need to format a nice, human-readable date to put in the header of an auto-generated letter or report:
```python
z = datetime.datetime(2012, 9, 23, 21, 37, 4, 177393)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
```
* The above would print `Sunday September 23, 2012`
* **It's worth noting that the performance of `strptime()` is often much worse than you might expect, due to the fact that
it's written in pure Python and it has to deal with all sorts of system locale settings.** If you are parsing a lot of dates
in your code and you know the precise format, you will probably get much better performance by cooking up a custom solution
instead. For example, if you knew that the dates were of the form "YYYY-MM-DD", you could write a function like this:
```python
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
```
* When tested, this function runs over seven times faster than `datetime.strptime()`. This is probably something to consider
if you are processing large amounts of data involving dates. 

## Iterators and Generators
### Manually consuming an Iterator
* You need to process items in an iterable, but for whatever reason, you can't or don't want to use a for loop.
====> look at iteratorsGenerators/iterator1.py
* To manually consume an iterable, use the next() function and write your code to catch the StopIteration exception.

### Delegating Iteration to a container object
* Typically, all you need to do is define an `__iter__()` method that delegates iteration to the internally held container.
  ex: In this code, the `__iter__()` method simply forwards the iteration request to the internally held _children attribute.
  <pre>
  def __iter__(self):
    return iter(self._children)
  </pre>

### Creating new iterations patterns with generators
* If you want to implement a new kind of iteration pattern, define it using a generator function.

## Files and I/O

### Reading and writing text data
* Use the open() function with mode rt to read a text file. ==> look at fileAndIo/file_example1.py
* Use the open() function with mode wt to write to a file, clearing and overwriting the previous contents (if any).
* Use the open() function with mode at to append to a file
* By default, files are read/written using the system default text encoding, as can be found in sys.getdefaultencoding().
On most machines, this is set to utf-8. If you know that the text you are reading or writing is in a different encoding,
supply the optional encoding paramete to open(). ex: encoding='latin-1'
* Some things to keep in mind from the example
    * First, the use of the 'with' statement in the examples establishes a context in which the file will be used. When control
    leaves the 'with' block, the file will be closed automatically. You don't need to use the 'with' statement, but if you don't
    use it, make sure you remember to close the file.
* Another minor complication concerns the recognition of newlines, which are different on Unix and Windows(i.e., \n versus \r\n).
By default Python operates in what's known as "universal newline" mode. In this mode, all common newline conventions are recognized,
and newline characters are converted to a single \n character while reading. Similarly, the newline character \n is converted
to the system default newline character on output. If you don't want this translation, supply the newline='' argument to
open() like newline=''
* If you are experiencing encoding errors, you can supply an optional errors argument to open() to deal with the errors.
ex: errors='replace', errors='ignore'

### Printing with a different separator or line ending
* You want to output data using `print()`, but you also want to change the separator character or line ending.
* Use the `sep` and `end` keyword arguments to `print()` to change the output as you wish.
* Use of the `end` argument is also how you suppress the output of newlines in output, ==> `print(i, end=' ')`
* ex: `print(*row, sep=',')`

### Build your own Command Line with ANSI escape codes
* The way that most programs interact with the Unix terminal is through ANSI escape codes. These are special codes that your
program can print in order to give the terminal instructions.
* Rich Text
  * Colors - The most basic thing you can do to your text is to color it. The Ansi colors all look like
    * Red - `\u001b[31m`
    * Reset - `\u001b[0m` note: Resets all colors and text effects.
    * The `\u001b` character is the special character that starts off most Ansi escapes; most languages allow this syntax
    for representing special characters, e.g. Java, Python, and JS all allow the `\u001b` syntax
    * The color will persist when you print other strings. To avoid this, we need to make sure we end our colored-string with
    the Reset code.
    * The most basic terminals have a set of **8** different colors:
    
    | Color | Ansi Code |
    | --- | --- |
    | Black | `\u001b[30m` |
    | Red   | `\u001b[31m` |
    | Green | `\u001b[32m` |
    | Yellow| `\u001b[33m` |
    | Blue  | `\u001b[34m` |
    | Magenta| `\u001b[35m`|
    | Cyan  | `\u001b[36m` |
    | White | `\u001b[37m` |
    | Reset | `\u001b[0m`  |
    
    * Most terminals, apart from the basic set of 8 colors, also support the "bright" or "bold" colors, **16** colors. These have their own
    set of codes, mirroring the normal colors, but with an additional ;1 in their codes. ex: 
    
    | Color | Ansi code |
    | ---   | ---       |
    | Bright Black | `\u001b[30;1m` |
    
    * Lastly, after the 16 colors, some terminals support a 256-color extended color set. These are of the form `\u001b[38;5;${ID}m`.
    ====> look at escape_codes_examples.py
  * Background Colors - the ansi escape codes let you set the color of the text-background the same way it lets you set the color
  of the foreground.
  
    | Background Color | Code |
    | ---              | ---  |
    | Black | `\u001b[40m` |
    | Red   | `\u001b[41m` |
    | Green | `\u001b[42m` |
    | Yellow| `\u001b[43m` |
    | Blue  | `\u001b[44m` |
    | Magenta | `\u001b[45m` |
    | Cyan  | `\u001b[46m` |
    | White | `\u001b[47m` |
  
    * Bright versions being: ex: bright black `\u001b[40;1m`
  * Decorations - Apart from colors, and background colors, Ansi escape codes also allow decorations on the text:
    * Bold: `\u001b[1m`
    * Underline: `\u001b[4m`
    * Reversed: `\u001b[7m`
* Cursor Navigation - the next set of Ansi escape codes allow you to move the cursor around the terminal window, or erase
parts of it. These are the Ansi escape codes that programs like Bash use to let you move your cursor left and right across
your input command in response to arrow-keys
  * Basic cursor moves up, down, left and right (n = number of characters to move by)
    * Up - `\u001b[{n}A`
    * Down - `\u001b[{n}B`
    * Right - `\u001b[{n}C`
    * Left - `\u001b[{n}D`
  * Progress Indicator - ====> Look at filesAndIo/progress_indicator.py
  * ASCII Progress bar - ====> Look at filesAndIo/progress_indicator.py
  * Multiple ASCII Progress bar - ====> Look at filesAnIo/progress_indicator.py
    * Perhaps next time you are writing a command line application that's downloading lots of files in parallel, or doing
    some kind of parallel task, you could write a similar Ansi-escape-code-based progress bar so the user can see how their
    command is progressing.
    
### Writing a command line
One of the more fancy things you might do with Ansi escape codes is to implement a command-line. Bash, Python, Ruby, all have
their own in-built command line that lets you type out a command and edit its text before submitting it for execution. While
it may seem special, in reality this command line is just another program that interacts with the terminal via Ansi escape
codes! 
  
  
    


### Reading and Writing Binary Data
* Use the open() function with mode rb or wb to read or write binary data. When reading binary data, it is important to stress
that all data returned will be in the form of byte strings, not text strings. Similarly, when writing you must supply data
in the form of objects that expose data as bytes (e.g., byte strings, bytearray objects).
* When reading binary data, the subtle semantic differences between byte strings and text strings pose a potential gotcha. In
particular be aware that indexing and iteration return integer byte values instead of byte strings.
* If you ever need to read or write text from a binary-mode file, make sure you remember to decode and encode it. For example
<pre>
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    
with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
</pre>
* A lesser known aspect of binary I/O is that objects such as *arrays* and C structures can be used for writing without any kind
of intermediate conversion to a bytes objects.

## Data Encoding and Processing
### Parsing Simple XML Data
* You would like to extract data from a simple XML document.
* The `xml.etree.ElementTree` module can be used to extract data from simple XML documents. ===> data_encoding_and_processing/xml_parsing.py
* The `xml.etree.ElementTree.parse()` function parses the entire XML document into a document object. From there you use methods
such as `find()`, `iterfind()`, and `findtext()` to search for specific XML elements. The arguments to these functions are
the names of a specific tag.
* Each find operation takes place relative to a starting element. Likewise, the tagname that you supply to each operation is
also relative to the start.
* Each element represented by the `ElementTree` module has a few essential attributes and methods that are useful when parsing.
The `tag` attribute contains the name of the tag, the `text` attribute contains enclosed text, and the `get()` method can be
used to extract attributes if any.
* It should be noted `xml.tree.ElementTree` is not the only option for XML parsing. For more advanced applications, you might
consider `lxml`. Its the same as `xml` except that it is extremely fast, and provides support for features such as validation,
XSLT, and XPath.

## Functions
### Writing functions that accept any number of arguments
* To write a function that accepts any number of positional arguments, use a * argument. A * argument can only appear as the last positional argument in a function definition.
  * example use: avg(1, 2, 3)
* To accept any number of keyword arguments, use an argument that starts with **. A ** argument can only appear as the last argument. A subtle aspect of function definition is that arguments can still appear after a * argument.
  * example use: find_person(name='Bob', age=100)
### Writing functions that only accept keyword arguments.
* This feature is easy to implement if you place the keyword arguments after a * argument or a single unnamed *. Keyword-only arguments are often a good way to enforce greater code clarity when specifying optional function arguments.
### Attaching informational metadata to function arguments
* Function argument annotations can be a useful way to give programmers hints about how a function is supposed to be used. ==> look at functions/functions.py
### Returning multiple values from a function
* To return multiple values from a function, simply return a tuple
### Defining functions with default arguments
* On the surface, defining a function with optional arguments is easy--simply assign values in the definition and make sure
that default arguments appear last.
* If the default value is supposed to be a mutable container, such as a list, set, or dictionary, use `None` as the default
* If instead of providing a default value, you want to write code that merely tests whether an optional argument was given
an interesting value or not, use this idiom: `_no_value = object()`
### Defining anonymous or Inline functions
* Simple functions that do nothing more than evaluate an expression can be replaced by a lambda expression. ===> look at
functions/functions.py
* Although lambda allows you to define a simple function, its use is highly restricted. In particular, only a single expression
can be specified, the result of which is the return value. This means that no other language features, including multiple
statements, conditionals, iteration, and exception handling, can be included.
### Capturing Variables in Anonymous Functions
* If you want an anonymous function to compare a value at the point of definition and keep it, include the value as a default
value, like this: `a = lambda y, x=x: x + y`

### Replacing Single Method Classes with Functions
* In many cases, single-method classes can be turned into functions using closures.
* Whenever you're writing code and you encounter the problem of attaching additional state to a function, think closures.
They are often a more minimal and elegant solution than the alternative of turning your function into a full-fledged class.

### Carrying Extra State with Callback Functions
* Look at functions/functions.py
* Software based on callback functions often runs the risk of turning into a huge tangled mess. Part of the issue is that
the callback function is often disconnected from the code that made the initial request leading to callback execution. Thus,
the execution environment between making the request and handling the result is effectively lost. If you want the callback
function to continue with a procedure involving multiple steps, you have to figure out how to save and restore the associated
state.
* There are really two main approaches that are useful for capturing and carrying state. You can carry it around on an instance
(attached to a bound method perhaps) or you can carry it around in a closure (an inner function). Of the two techniques,
closures are perhaps a bit more lightweight and natural in that they are simply built from functions. They also automatically
capture all of the variables being used. Thus, it frees you from having to worry about the exact state that needs to be stored
(it's determined automatically from your code).
* If using closures, you need to pay attention to mutable variables. The `nonlocal` declaration is used to indicate that a 
variable is being modified from within the callback. Without this declaration, you'll get an error. ex: `nonlocal sequence`
* The use of coroutine as a callback handler is interesting in that it is is closely related to the closure approach. In 
some sense, it's even cleaner, since there is just a single function. Moreover, variables can be freely modified without
worrying about nonlocal declarations. The potental downside is that coroutines don't tend to be as well understood as other
parts of Python. There are also a few tricky bits such as the need to call `next()` on a coroutine prior to using it. That's
something that could be easy to forget in practice.
* The last technique involving `partial()` is useful if all you need to do is pass extra values into a callback. Instead
of using `partial()`, you'll sometimes see the same thing accomplished with the use of lambda

### Inlining Callback Functions
* Callback functions can be inlined into a function using generators and coroutines.

## Classes and Objects
### Changing the string representation of instances
* You want to change the output produced by printing or viewing instances to produce something more sensible
* To change the string representation of an instance, define the `__str__()` and `__repr__()` methods ==> look at classesAndObjects/classes1.py
* The `__repr__()` method returns the code representation of an instance, and is usually the text you would type to re-create the
the instance. The built-in `repr()` function returns this text, as does the interactive interpreter when inspecting values.
* The `__str__()` method converts the instance to a string, and is the output produced by the `str()` and `print()` functions.
* Defining `__repr__()` and `__str__()` is often good practice, as it can simplify debugging and instance output. For example,
by merely printing or logging an instance, a programmer will be shown more useful information about the instance contents.
* It is standard practice for the output of `__repr__()` to produce text like `Student('JEFFERSON', 'Vivanco')`. If this is
not possible or desired, then it is common to create a useful textual representation enclosed in `<` and `>` instead, for
example `<Student first_name='JEFFERSON' last_name='Vivanco'>`


### Saving Memory When Creating a Large Number of Instances
* Your program creates a large number (e.g., millions) of instances and uses a large amount of memory.
* For classes that primarily serve as simple data structures, you can often greatly reduce the memory footprint of instances
by adding the `__slots__` attribute to the class definition.
```python
class Date:
  __slots__ = ['year', 'month', 'day']
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day
```
* When you define `__slots__`, Python uses a much more compact internal representation for instances. Instead of each instance
consisting of a dictionary, instances are built around a small fixed-sized array, much like a tuple or list. Attribute names
listed in the `__slots__` specifier are internally mapped to specific indices within this array.
* A side effect of using slots is that it is no longer possible to add new attributes to instances--you are restricted to
only those attribute names listed in the `__slots__` specifier.
* The memory saved by using slots varies according to the number and type of attributes stored. However, in general, the resulting
memory use is comparable to that of storing data in a tuple. To give you an idea, storing a single `Date` instance without slots
requires 428 bytes of memory on a 64-bit version of Python. If slots is defined, it drops to 156 bytes. In a program that
manipulated a large number of dates all at once, this would make a significant reduction in overall memory use.
* Although slots may seem like a feature that could be generally useful, you should resist the urge to use it in most code.
There are many parts of Python that rely on the normal dictionary-based implementation. In addition, classes that define slots
don't support certain features such as multiple inheritance. For the most part, you should only use slots on classes that
are going to serve as frequently used data structures in your program.

### Encapsulating names in a class
* Rather than relying on language features to encapsulate data, Python programmers are expected to observe certain naming conventions
concerning the intended usage of data and methods.
* The first convention is that any name that starts with a **single leading underscore (_) should always be assumed to be internal
implementation.** ==> look at classesAndObjects/classes1.py
* Python doesn't actually prevent someone from accessing internal names. However, doing so is considered impolite, and may result
in fragile code.
* You may also encounter the use of two leading underscores (__) on names within class definitions. The use of double leading
underscores causes the name to be mangled to something else. Specifically, for example a private method in a class B get renamed to
_B__private_method respectively. The purpose of such name mangling is *inheritance*. Such attributes cannot be overriden via inheritance.
* Also note, sometimes you may want to define a variable that clashes with the name of a reserved word. For this you should use a single
trailing underscore ex: lambda_

### Creating managed attributes
* You want to add extra processing (e.g, type checking or validation) to the getting or setting of an instance attribute.
* A simple way to customize access to an attribute is to define it as a "property". Look at ==> classesAndObjects/classes1.py
* When implementing a property, the underlying data (if any) still needs to be stored somewhere. Thus, in the get and set methods,
you see direct manipulation of a _first_name attribute, which is where the actual data lives.
* Properties should only be used in cases where you actually need to perform extra processing on attribute access. Sometimes
programmers coming from languages such as Java feel that all access should be handled by getters and setters. Don't write
properties that don't actually add anything extra like this. For one, it makes your code more verbose and confusing to others.
Second, it will make your program run **a lot slower**. Lastly, it offers no real design benefit. Specifically, if you later
decide that extra processing needs to be added to the handling of an ordinary attribute, you could promote it to a property
without changing existing code. This is because the syntax of code that accessed the attribute would remain unchanged.
* Properties can also be a way to define computed attributes. These are attributes that are not actually stored, but computed
on demand.
* Although properties give you an elegant programming interface, sometimes you actually may want to directly use getter and
setter functions. This often arises in situations where Python code is being integrated into a larger infrastructure of systems
or programs. For example, perhaps a Python class is going to be plugged into a large distributed system based on remote procedure
calls or distributed objects. In such a setting, it may be much easier to work with an explicit get/set method (as a normal method call)
rather than a property that implicitly makes such calls. 
* **Last but not least, don't write Python code that features a lot of repetitive property definitions. Code repetitions leads to
bloated, error prone, and ugly code. As it turns out, there are much better ways to achieve the same thing using descriptors or
closures.

### Calling a method on a Parent Class
* You want to invoke a method in a parent class in place of a method that has been overriden in a subclass.
* To call a method in a parent (or superclass), use the super() function. 

### Extending a Property in a Subclass
* Within a subclass, you want to extend the functionality of a property defined in a parent class. 
====> Look at classesAndObjects/classes1.py
* Extending a property in a subclass introduces a number of very subtle problems related to the fact that a property is
defined as a collection of getter, setter, and deleter methods, as opposed to just a single method. Thus, when extending
a property, you need to figure out if you will redefine all of the methods together or just one of the methods.
* In this particular solution, there is no way to replace the hardcoded class name `Person` with something more generic.
If you don't know which base class defined a property, you should use the solution where all of the property methods are
redefined and `super()` is used to pass control to the previous implementation.

### Defining an Interface or Abstract Base Class
* You want to define a class that serves as an interface or abstract base class from which you can perform type checking
and ensure that certain methods are implemented in subclasses. ===> Look at classesAndObjects/classes2.py
* A central feature of an abstract class is that it cannot be instantiated directly.
* A major use of abstract base classes is in code that wants to enforce an expected programming interface
* For example, one way to view the `IStream` base class is as a high level specification for an interface that allows reading
and writing of data. Code that explicitly checks for this interface could be written as follows:
```python
def serialize(obj, stream):
  if not isinstance(stream, IStream):
    raise TypeError('Expected an IStream')
```
* You might think that this type of type checking only works by subclassing the abstract base class (`ABC`), but `ABC` allows
other classes to be registered as implementing the required interface. For example, you can do this:
```python
import io
# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)
# Open a normal file and type check
f = open('foo.txt')
isinstance(f, IStream) # Returns True
```
* It should be noted that `@abstractmethod` can also be applied to static methods, class methods, and properties.
* Predefined abstract base classes are found in various places in the standard library. The `collections` module defines a
variety of ABCs related to containers and iterators (sequences, mappings, sets, etc.), the `numbers` library defines ABCs related
to numeric objects (integers, floats, rationals, etc.), and the `io` library defines ABCs related to I/O handling.
* If you use the ABC functionality, it is wise to carefully write tests that verify that the behavior is as you intended.
* Although ABCs facilitate type checking, it's not something that you should overuse in a program. At its heart, Python is a
dynamic language that gives you great flexibility. Trying to enforce type constraints everywhere tends to result in code that
is more complicated than it needs to be. You should embrace Python's flexibility.

## Modules and Packages

### Making a Hierarchical Package of Modules
* You want to organize your code into a package consisting of a hierarchical collection of modules.
* Making a package structure is simple. Just organize your code as you wish on the file system and make sure that every
directory defines an `__init__.py` file. Once you have done this, you should be able to perform various import statements,
such as the following:
```python
import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg
```
* Defining a hierarchy of modules is as easy as making a directory structure on the file system. The purpose of the `__init__.py`
files is to include optional initialization code that runs at different levels of a package are encountered. More often than
not, it's fine to leave the `__init__.py` files empty. However, there are certain situations where they might include code. For
example, an `__init__.py` file can be used to automatically load submodules like this:
```python
# graphics/formats/__init__.py
from . import jpg
from . import png
```
For such a file, a user merely has to use a single `import graphics.formats.png`.
* Other common uses of `__init__.py` include consolidating definitions from multiple files into a single logical namespace, as is
sometimes done when splitting modules.
* Astute programmers will notice that Python 3.3 still seems to perform package imports even if no `__init__.py` files are present.
If you don't define `__init__.py`, you actually create what is known as a "namespace package". All things being equal, include
`__init__.py`.

### Reading Datafiles Within a Package
Your package includes a datafile that your code needs to read. **You need to do this in the most portable way possible.**
* Suppose the file *spam.py* wants to read the contents of the file *somedata.dat*. To do it, use the following code:
```python
import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
```
The resulting variable `data` will be a byte string containing the raw contents of the file.
* To read a datafile, you might be inclined to write code that uses built-in I/O functions, such as `open()`. However, there
are several problems with this approach. 
  * First, a package has very little control over the current working directory of the interpreter. Thus, any I/O operations would
  have to be programmed to use absolute file-names. Since each module includes a `__file__` variable with the full path, it's
  not impossible to figure out the location, but it's messy.
  * Second, packages are often installed as *zip* or *.egg* files, which don't preserve the files in the same way as a normal
  directory on the file system. Thus, if you tried to use `open()` on a datafile contained in an archive, it wouldn't work
  at all.
* The first argument to `get_data()` is a string containing the package name. You can either supply it directly or use a
special variable, such as `__package__`. The second argument is the relative name of the file within the package. If necessary,
you can navigate into different directories using standard Unix filename conventions as long as the final directory is still
located within the package.

### Creating a New Python Environment
* You want to create a new Python environment in which you can install modules and packages. However, you want to do this without
installing a new copy of Python or making changes that might affect the system Python installation.
* You can make a new "virtual" environment using the `venv` command. This command is installed in the same directory as the
Python interpreter or possibly in the *Scripts* directory on Windows. Here is an example:
```bash
bash % python3 -m venv Spam
bash %
```
The name supplied to `venv` is the name of a directory that will be created. Upon creation, the *Spam* directory will look
something like this:
```bash
bash % cd Spam
bash % ls
bin include lib pyvenv.cfg
```
* To activate the virtual environment so it uses your newly created interpreter and packages do `source Span/bin/activate`
* To deactivate do `deactivate`
* In the *bin* directory, you'll find a Python interpreter that you can use.
* A key feature of this interpreter is that its *site-packages* directory has been set to the newly created environment. Should
you decide to install third-party packages, they will be installed here, not in the normal system *site-packages* directory.
* The creation of a virtual environment mostly pertains to the installation and management of third-party packages. With a
new virtual environment, the next step is often to install a package manager, such as `distribute` or `pip`. When installing
such tools and subsequent packages, you just need to make sure you use the interpreter that's part of the virtual environment. This
should install the packages into the newly created *site-packages* directory.
* By default, virtual environments are completely clean and contain no third-party add-ons. If you would like to include
already installed packages as part of a virtual environment, create the environment using the `--system-site-packages` option.

### Using PIP (the package installer for python)
You can use pip to install packages from the Python Package Index and other indexes.
* `pip install SomePackage` - install a package from PyPI
* `pip install SomePackage-1.0-py2.py3-none-any.wh1` - install a package that's already been downloaded from PYPI or obtained
from elsewhere. This is useful if the target machine does not have a network connection.
* `pip show --files SomePackage` - show what files were installed, show details about an installed package
* `pip list --outdated` - show what packages are outdated
* `pip install --upgrade SomePackage` - upgrade a package
* `pip uninstall SomePackage` - uninstall a package
* `pip install -U pip` - to upgrade pip

* Requirement Files - are files containing a list of items to be installed using pip install like so
`pip install -r requirements.txt`. In practice, there are 4 common uses of Requirements files
  1. Requirement files are used to hold the result from `pip freeze` for the purpose of achieving repeatable installations.
  ```bash
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```
  2. Requirement files are used to force pip to properly resolve dependencies.
  3. Requirement files are used to force pip to install an alternate version of a sub-dependency.
  4. Requirement files are used to override a dependency with a local patch that lives in version control.

## Network and Web Programming
### Interacting with http services as a client
* to send a simple http get request to a remote service you can use the urllib.request module 
===> Look at network_and_web_programming/web_example1.py

## Concurrency

### Starting and Stopping Threads
* You want to create and destroy threads for concurrent execution of code.
* The `threading` library can be used to execute any Python callable in its own thread. ===> Look at concurrency/threadz.py
* Threads are executed in their own system-level thread(e.g., a POSIX thread or Windows threads) that is fully managed by
the host operating system. Once started, threads run independently until the target function returns. You can query a thread
instance to see if it's still running:
```python
if t.is_alive():
    print('still running')
else:
    print('completed')
```
* You can also request to join with a thread, which waits for it to terminate: `t.join()`
* The interpreter remains running until all threads terminate. For long-running threads or background tasks that run forever,
you should consider making the thread daemonic. For example
```python
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
```
* Daemonic threads can't be joined. However, they are destroyed automatically when the main thread terminates.
* Beyond the two operations shown, there aren't many other things you can do with threads. For example, there are no operations
to terminate a thread, signal a thread, adjust its scheduling, or perform any other high-level operations. If you want these
features, you need to build them yourself.
* If you want to be able to terminate threads, the thread must be programmed to poll for exit at selected points.
===> concurrency/terminate_ex.py
* Polling for thread termination can be tricky to coordinate if threads perform blocking operations such as I/O. For example,
a thread blocked indefinitely on an I/O operation may never return to check if it's been killed. To correctly deal with this
case, you'll need to carefully program thread to utilize timeout loops.
* Due to a global interpreter lock (GIL), Python threads are restricted to an execution model that only allows one thread
to execute in the interpreter at any given time. For this reason, Python threads should generally not be used for computationally
intensive tasks where you are trying to achieve parallelism on multiple CPUs. They are much better suited for I/O handling
concurrent execution in code that performs blocking operations (e.g., waiting for I/O, waiting for results from a database, etc.).
* You can also execute your code in a separate process using the `multiprocessing` module ==> Look at concurrency/multiprocessingz.py
* Don't tie your class to either Thread or Process class so your class is free to be used either way

### Communicating between threads
* You have multiple threads in your program and you want to safely communicate or exchange data between them.
* Perhaps the safest way to send data from one thread to another is to use a `Queue` from the `queue` library. To do this,
create a `Queue` instance that is shared by the threads. Threads then use `put()` or `get()` operations to add or remove
items from the queue. ===> look at concurrency/communication.py
* **Queue instances already have all of the required locking, so they can be safely shared by as many threads as you wish.**
* When using queues, it can be somewhat tricky to coordinate the shutdown of the producer and consumer. A common solution to
this problem is to rely on a special sentinel value, which when placed in the queue, causes consumers to terminate.
===> look at concurrency/communicationz.py
  * A subtle feature of the above example is that the consumer, upon receiving the special sentinel value, immediately places
  it back onto the queue. This propagates the sentinel to other consumers threads that might be listening on the same queue--thus
  shutting them all down one after the other.
* **Although queues are the most common thread communication mechanism, you can build your own data structures as long as
you add the required locking and synchronization.** The most common way to do this is to wrap your data structures with a
condition variable. ====> communication/PriorityQueue.py
* **Thread communication with a queue is a one-way and nondeterministic process.** In general, there is no way to know
when the receiving thread has actually received a message and worked on it. However, `Queue` objects do provide some basic
completion features, as illustrated by the `task_done()` and `join()` methods in this example. ===> look at concurrency/communicationz.py
* If a thread needs to know immediately when a consumer thread has processed a particular item of data, you should pair the sent
data with an `Event` object that allows the producer to monitor its progress. ===> look at concurrency/communicationz.py
* Writing threaded programs based on simple queuing is often a good way to maintain sanity. If you can break everything down
to simple thread-safe queueing, you'll find that you don't need to litter your program with locks and other low-level synchronization.
Also, communicating with queues often leads to designs that can be scaled up to other kinds of message-based communication
patterns later on. For instance, you might be able to split your program into multiple processes, or even a distributed system,
without changing much of its underlying queuing architecture.
* One caution with thread queues is that putting an item in a queue doesn't make a copy of the item. Thus, communication actually
involves passing an object reference between threads. If you are concerned about shared state, it may make sense to only pass
immutable data structures (e.g., integers, strings, or tuples) or to make deep copies of the queued items.
* Making a queue block when it's full can have an unintended cascading effect throughout your program, possibly causing it
to deadlock or run poorly. In general, the problem of "flow of control" between communicating threads is a much harder problem
than it seems. If you ever find yourself trying to fix a problem by fiddling with queue sizes, it could be an indicator of
a fragile design or some other inherent scaling problem.
* Both the `get()` and `put()` methods support nonblocking and timeouts. ex: `q.get(block=False)`. Both of these options can
be used to avoid the problem of just blocking indefinitely on a particular queuing operation. For example, a nonblocking `put()`
could be used with a fixed-sized queue to implement different kinds of handling code for when a queue is full. For ex:
```python
def producer(q):
    try:
        q.put(item, block=False)
    except queue.Full:
        log.warning('queued item %r discarded!', item)
```  
* A timeout is useful if you're trying to make consumer threads periodically give up on operations such as `q.get()` so that
they can check things such as a termination flag.
* There are utility methods `q.size()`, `q.full()`, `q.empty()` that can tell you the current size and status of the queue.
However, be aware that all of these are unreliable in a multithreaded environment. Frankly, it's best to write your code
not to rely on such functions.

## Utility Scripting and System Administration
A lot of people use Python as a replacement for shell scripts, using it to automate common
system tasks, such as manipulating files, configuring systems, and so forth. The main goal
for this chapter is to describe features related to common tasks encountered when writing
scripts. 

### Terminating a program with an error message
* You want your program to terminate by printing a message to standard error and returning a nonzero status code.
* To have a program terminate in this manner, raise a `SystemExit` exception, but supply the error message as an argument.
For ex: `raise SystemExit('It Failed')`
* This will cause the supplied message to be printed to `sys,stderr` and the program to exit with
a status code of 1.

### Prompting for a Password at Runtime
You've written a script that requires a password, but since the script is meant for 
interactive use, you'd like to prompt the user for a password rather than hardcode it
into the script.
* Python's `getpass` module is precisely what you need in this situation. It will allow
you to very easily prompt for a password withot having the keyed-in password displayed
on the user's terminal. Here's how it's done
```python
import getpass

def svc_login(user, passwd):
  pass

user = getpass.getuser()
passwd = getpass.getpass()
if svc_login(user, passwd):
  print('Yay')
else:
  print('Boo')
```
* In this code, the `svc_login()` function is code that you must write to further process
the password entry.
* Note in the preceding code that `getpass.getuser()` doesn't prompt the user for their
username. Instead, it uses the current user's login name, according to the user's shell
environment, or as last resort, according to the local system's password database (on
platforms that support the `pwd` module).
* It's also important to remember that some systems may not support the hiding of the
typed password input to the `getpass()` method. In this case, Python does all it can to
forewarn you of problems before moving on.

### Making a stopwatch timer
You want to be able to record the time it takes to perform various tasks.

* The `time` module contains various functions for performing time-related functions. However, it's
often useful to put a higher-level interface on them that mimics a stop watch. For ex:
```python
import time

class Timer:
  def __init__(self, func=time.perf_counter):
    self.elapsed = 0.0
    self._func = func
    self._start = None
  def start(self):
    if self._start is not None:
      raise RuntimeError('Already started')
    self._start = self._func()
  def stop(self):
    if self._start is None:
      raise RuntimeError('Not started')
    end = self._func()
    self.elapsed += end - self._start
    self._start = None
  def reset(self):
    self.elapsed = 0.0

  @property
  def running(self):
    return self._start is not None
  def __enter__(self):
    self.start()
    return self
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.stop()
```
* This class defines a timer that can be started, stopped, and reset as needed by the user. It keeps
track of the total elapsed time in the `elapsed` attribute. Here is an example that shows
how it can be used:
```python
# Implementation above
class Timer:
  pass
def countdown(n):
  while n > 0:
    n -= 1

# Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(1000000)
t.stop()
print(t.elapsed)

# Use 2: As a context manager
with t:
  countdown(1000000)
print(t.elapsed)

with Timer() as t2:
  countdown(1000000)
print(t2.elapsed)
```
* This recipe provides a simple yet very useful class for making timing measurements and tracking 
elapsed time. It's also a nice illustration of how to support the context management protocol and
the `with` statement.
* One issue in making timing measurements concerns the underlying time function used to do it. As
a general rule, the accuracy of timing measurements made with functions such as `time.time()` or
`time.clock()` varies according to the operating system. In contrast, the `time.perf_counter()`
function always uses the highest-resolution timer available on the system.
* As shown , the time recorded by the `Timer` class is made according to wall-clock time, and
includes all time spent sleeping. If you only want the amount of CPU time used by the process, use
`time.process_time()` instead. For example:
```python
import time
def countdown():
  pass
class Timer:
  pass
t = Timer(time.process_time)
with t:
  countdown(1000000)
print(t.elapsed)
```
* Both the `time.perf_counter()` and the `time.process_time()` return a "time" in fractional
seconds. However, the actual value of the time doesn't have any particular meaning. To make
sense of the results, you have to call the functions twice and compute a time difference.

### Putting limits on memory and cpu usage
You want to place some limits on the memory or CPU use of a program running on Unix system.

* The `resource` module can be used to perform both tasks. For example, to restrict CPU time,
do the following:
```python
import signal, resource, os
def time_exceeded(signo, frame):
  print("Time's up")
  raise SystemExit(1)

def set_max_runtime(seconds):
  # install the signal handler and set a resource limit
  soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
  resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
  signal.signal(signal.SIGXCPU, time_exceeded)


```

### Launching a web browser
You want to launch a browser from a script and have it point to some URL that you specify.

* The `webbrowser` module can be used to launch a browser in a platform-independent manner. For ex:
```python
import webbrowser
webbrowser.open('http://www.python.org')
```
* This opens the requested page using the default browser. If you want a bit more control over how the page
gets opened, you can use one of the following functions:
  * `webbrowser.open_new('http://www.python.org')`
  * `webbrowser.open_new_tab('http://www.python.org')`

* If you want to open a page in a specific browser, you can use the `webbrowser.get()` function to
specify a particular browser. For ex:
```python
import webbrowser
c = webbrowser.get('firefox')
c.open('http://www.google.com')
```

## Testing, Debugging and Exceptions
### Unit Tests and Test Cases
* the module unittest from the Python standard library provides tools for testing your code. 
* A *unit test* verifies that one specific aspect of a function's behavior is correct.
* A *test case* is a collection of unit tests that together prove that a function behaves as it's supposed to, 
within the full range of situations you expect it to handle.
* A good test case considers all the possible kinds of input a function could receive and includes tests to represent
each of these situations.
* A test case with *full coverage* includes a full range of unit tests covering all the possible ways you can use a function.
* Assert methods available from the unittest module
*  
  | Method | Use  |
  | ---    | ---- |
  |assertEqual(a, b) |Verify that a == b |
  |assertNotEqual(a, b) |Verify that a != b |
  |assertTrue(x) |Verify that x is True |
  |assertFalse(x) |Verify that x is False |
  |assertIn(item, list) |Verify that item is in list |
  |assertNotIn(item, list) |Verify that item is not in list |
* Testing a class is similar to testing a function--much of your work involves testing the behavior of the methods in the class.
* the setUp() method
  * The unittest.TestCase class has a setUp() method that allows you to create these objects once and use them in each of your test methods.
    When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with test_. Any
    objects created in the setUp() method are then available in each test method you write.
    
### Creating Custom Exceptions
* look at beginner_notes/exceptions
  

## Web Application Util
### Logging
* use `logging` module, ===> look at web_application_util/logging.py
* Logging is a means of tracking events that happen when some software runs. The software's developer adds logging calls
to their code to indicate that certain events have occurred. An event is described by a descriptive message which can optionally
contain variable data. Events can also have an importance which the developer ascribes to the event; the importance can also
be called the level or severity.
* When to use logging?

| Task you want to perform | The best tool for the task |
| ---                      | ---                        |
| Display console output for ordinary usage of a command line script or program | `print()` |
| Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation) | `logging.info()` (or `logging.debug()` for very detailed output for diagnostic purposes) |
| Issue a warning regarding a particular runtime event | `warnings.warn()` in library code if the issue is avoidable and the client application should be modified to eliminate the warning. `logging.warning()` if there's nothing the client application can do about the situation, but the event should still be noted |
| Report an error regarding a particular runtime event | Raise an exception |
| Report suppression of an error without raising an exception (e.g. error handler in a long-running server process | `logging.error()`, `logging.exception()` or `logging.critical()` as appropriate for the specific error and application domain |

* The logging functions are named after the level or severity of the events they are used to track. The standard levels and their
applicability are described below (in increasing order of severity):

| Level | When it's used |
| ---   | ---            |
| `DEBUG` | Detailed information, typically of interest only when diagnosing problems. |
| `INFO`  | Confirmation that things are working as expected |
| `WARNING` | An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected. |
| `ERROR` | Due to a more serious problem, the software has not been able to perform some function |
| `CRITICAL` | A serious error, indicating that the program itself may be unable to continue running |

* The default level is `WARNING`, which means that only events of this level and above will be tracked, unless the logging package
is configured to do otherwise. 

