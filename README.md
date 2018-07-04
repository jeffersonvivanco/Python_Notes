# Python_Notes

Some notes on python with examples.

## Data Structures and Algorithms (look in dsAlgo folder for examples)

### unpacking elements from iterables of arbitrary length
* unpack arrays, objects, tuples -> look at python_notes1.py
* ex:`>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')`
* `>>> name, email, *phone_numbers = record`
* `>>> print(name)`
* `>>> Dave`

### keeping the last N items
* keeping a limited history is a perfect use for a collections.deque -> look ay python_notes2.py
* although you could manually perform such operations on a list, the queue solution
  is far more elegant and runs a lot faster.
* adding or popping items from either end of a queue has O(1) complexity. This is unlike
  a list where inserting or removing items from the front of the list is O(N).

### finding the largest or smallest N items
* to make a list of the largest or smallest N items in a collection, use heapq -> look at python_notes3.py
* the heapq module has 2 functions nlargest() and nsmallest()
* Further info
  * If you are looking for the N smallest or largest items and N is small compared to the overall
    size of the collection, these functions (nlargest, nsmallest) provide superior performance.
  * the most important feature of a heap is that heap[0] is always the smallest item.
  * Moreover, subsequent items can be easily found using the heapq.heappop() method, which pops off the first
    item and replaces it with the next smallest item (an operation that requires O(logN) operations where N is
    the size of the heap). 
  * IMPORTANT: nlargest() and nsmallest() are most appropriate if you are trying to find a relatively small number of
    items. 
  * If you are simply trying to find the single smallest and largest item (N=1), it is faster to use min(), max()
  * IMPORTANT: similarly if N is about the same size as the collection itself, it's usually faster to sort it first
    and take a slice (i.e., use sorted(items)[:N] or sorted(items)[-N:]).

### mapping keys to multiple values in a dictionary
* a dictionary is a mapping where each key is mapped to a single value. If you want to map keys to multiple values,
  you need to store the multiple values in another container such as a list or set. -> look at multidict.py
* list: to store order
* set: to eliminate duplicates

### keeping dictionaries in order
* to control the order of items in a dictionary, you can use an OrderedDict from the collections module. It exactly
  preserves the original insertion order of data when iterating.  ==> look at dict_notes.py
* An OrderedDic internally maintains a doubly linked list that orders the keys according to insertion order. When a
  new item is first inserted, it is placed at the end of this list.
* be aware that the size of an OrderedDict is more than twice as large as a normal dictionary due to the extra linked
  list that's created.

### calculating with dictionaries
* to perform various calculations (eg. min, max, sorting) on a dictionary data. ==> look at dict_notes.py
* in order to perform useful calculations on the dictionary contents, it is often useful to invert the keys and values
  of the dictionary using zip()
*** be aware that zip() creates an iterator that can only be consumed once.
*** If you try to perform data reductions on a dictionary, you'll find that they only process the keys, not the values.
    You can fix this by using the values method of a dictionary, but then you don't get the keys, using zip solves this
    problem

### finding commonalities in two dictionaries
* to find out what two dictionaries have in common, simply perform common set operations using the keys() or items() methods
  ===> look in dict_notes.py

### removing duplicates while preserving order
* ===> look at removing_duplicates.py
* if order does not matter to you, you can convert the list into a set

### naming a slice
* If you have a lot of hardcoded slices in your code, you can name a slice by using the slice function and assigning it to a
  variable. ===> look at python_notes4.py

### determining the most frequently occuring items in a sequence
* The collections.Counter class is designed for just such a problem. It even comes with a handy most_common() method that will
  give you the answer. ===> look at mostFrequentOccur.py
* As input, Counter objects can be fed any sequence of hashable input items.
* to update the list of words and do a count you can use the update function
* You can combine counter objects using + and -
 
### sorting a list of dictionaries by a common key
* sorting this type of structure is easy using the operator module's itemgetter function. ===> look at sortingListOfDicts.py
* the itemgetter function can also accept multiple keys
* the operator.itemgetter() function takes as arguments the lookup indices used to extract the desired values from the records
  in rows (look at sample code). It can be a dictionary key name, a numeric list element, or any value that can be fed to an
  object's __get_item__() method. If you give multiple indices to itemgetter(), the callable it produces will return a tuple
  with all of the elements in it, and sorted() will order the output according to the sorted order of the tuples.
* The functionality of itemgetter() is sometimes replaced by lambda expressions, ex: 
  rows_by_fname = sorted(rows, key=lambda r: r['fname'])
* The solution above works fine, but the solution with itemgetter tends to run a bit faster
* this technique can applied also to min and max

### sorting objects without native comparison support
* When you want to sort objects of the same class and they don't natively support comparison operations you can use the built
  in sorted function.
* The built in sorted() function takes a key argument that can be passed a callable that will return some value in the object
  that sorted will use to compare the objects. ===> look at comparing_users.py
* you can use operator.attrgetter to get the key
* same technique for min and max

### Grouping records together based on a field
* the itertools.groupby() function is particularly useful for grouping data
* [INFO]: sort() will sort the original list unlike sorted that returns a new list, fyi
* The groupby() function works by scanning a sequence and finding sequential 'runs' of identical values. On each iteration it
   returns the value along with an iterator that produces all of the items in a group with the same value
* An important preliminary step is sorting the data according to the field of interest. Since groupby() only examines
  consecutive items, failing to sort first won't group the records as you want

### filtering sequence elements
* the easiest way to filter sequence data is often to use a list comprehension, ===> look at filtering_sequence.py
* you can also use generator expressions to produce the filtered values iteratively 
* sometimes, the filtering criteria cannot be easily expressed in a list comprehension or generator expression. For
  example, suppose that the filtering process involves exception handling or some other complicated detail. For this
  put the filtering code into its own function and use the built-in filter() function 
* filter() creates an iterator, so if you want to create a list of results, make sure you also use list()
* List comprehensions and generator expressions also have the power to transform the data at the same time
  ex: [math.sqrt(n) for n in mylist if n > 0]
* One variation on filtering involves replacing the values that don't meet the criteria with a new value instead of discarding
  them. ex: clip_neg = [n if n > 0 else 0 for n in mylist]
* Another notable filtering tool is itertools.compress(), which takes an iterable and an accompanying Boolean selector sequence
  as input. As output, it gives you all of the items in the iterable where the corresponding element in the selector is True.
  This can be useful if you're trying to apply the results of filtering one sequence to another related sequence.
* like filter, compress normally returns an iterator. Thus, you need to use list() to turn the results into a list if desired.

### extracting a subset of a dictionary
* this is easily accomplished using dictionary comprehension ===> look at filtering_sequence.py

### mapping names to sequence elements
* Problem: You have code that accesses list or tuple elements by position, but this makes the code somewhat difficut to read
  at times. You'd also like to be less dependent on position in the structure, by accessing the elements by name.
* Solution: collections.namedtuple() provides these benefits while adding minimal overhead over using a normal tuple object.
  collections.namedtuple() is actually a factory method that returns a subclass of the standard python tuple type. You feed it a type name, and the fields it should have, and it returns a class that you can instantiate, passing in values for the 
  fields you have defined. ====> look at namedTuple.py
* Although an instance of a namedtuple looks like a normal class instance, it is a interchangeable with a tuple and supports
  all of the usual tuple operations such as indexing and unpacking.
* A major use case for named tuples is decoupling your code from the position of the elements it manipulates. So, if you get
  back a large list of tuples from a database call, then manipulate them by accessing the positional elements, your code could
  break if, say, you added a new column to your table. Not so if you first cast the returned tuples to namedtuples.
* One possible use of a namedtuple is as a replacement for a dictionary, which requires more space to store. Thus, if you are 
  building large data structures involving dictionaries, use of a namedtuple will be more efficient. However, be aware that
  unlike a dictionary, a namedtuple is immutable.
* If you need to change any of the attributes, it can be done using the _replace() method of a namedtuple instance, which
  makes an entirely new namedtuple with specified values replaced. 
* A subtle use of the _replace() method is that it can be a convinient way to populate named tuples that have optional or
  missing fields. To do this, you make a prototype tuple containing the default values and then use _replace() to create
  new instances with values replaced.
* Last, but not least, it should be noted that if your goal is to define an efficient data structure where you will be
  changing various instance attributes, using namedtuple is not your best choice, instead consider defining a class using
  _slots_ 

### Transforming and Reducing Data at the same time
* A very elegant way to combine a data reduction and a transformation is to use a generator-expression argument.
  ====> look at generator_expression.py
* Using a generator argument is often a more efficient and elegant approach than first creating a temporary list.
  For a small list, it might not matter, but if nums was huge, you would end up creating a large temporary data structure
  to only be used once and discarded. The generator solution transforms the data iteratively and is therefore much more
  memory efficient.
* Certain reduction functions such as min and max accept a key argument that might be useful in situations where you might
  be inclined to use a generator.

### Combining multuple mappings into a single mapping
* Suppose you want to perform lookups where you have to check 2 dictionaries. An easy way to do this is to use the ChainMap
  class from the collections module. ==> look at dict_notes.py
* A ChainMap takes multiple mappings and makes them logically as one. However, the mappings are not literally merged together,
  instead a ChainMap simply keeps a list of the underlying mappings and redefines common dictionary operations to scan the
  list.
* If there are multuple keys, the values from the first mapping are used.
* Operations that mutate the mapping always affect the first mapping.
* As an alternative to ChainMap, you might consider merging dictionaries together using the update() method
* This works, but it requires you to make a new dictionary. If the original dict changes, the new one does not
  get affected unlike ChainMap

## Strings and Text (look in the stringText folder for examples)

### Splitting strings on any of multiple of delimeters (so common omg)
* Suppose you want to split a string into fields, but the delimeters and spacing around them aren't consistent throughout the
string.
* the split() method of string objects is really meant for very simple cases, and does not allow for multiple delimeters or account for possible whitespace around the delimeters. In cases when you need a bit more flexibility, use the re.split() method. (look in split.py)
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
* If you're just doing a simple text matching/searching operation, you can often skip the compilation step and use module-level functions in the re module instead. Be aware though, that if you are going to perform a lot of matching or searching, it usually pays to compile the pattern first and use it over and over again. The module-level functions keep a cache of recently compiled patterns, so there isn't a huge performance hit, but you'll save a few lookups and extra processing by using your own compiled pattern. 

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
* **Important** It is often the case that you want to combine string stripping operations with some other kind of iterative processing, such as reading lines of data from a file. If so, this is one area where a generator expression can be useful. ex: ```with open(filename) as f:
      lines = (line.strip() for line in f)
      for line in lines:
      ...```
* here, the expression lines = (line.strip() for line in f) acts as a kind of data transform. It's efficient because it doesn't actually read the data into any kind of temporary list first. It just creates an iterator where all of the lines produced have the stripping operation applied to them.

### Sanitizing and cleaning up text
* The problem of sanitizing and cleaning up text applies to a wide variety of problems involving text parsing and data handling. At a very simple level, you might use basic string functions (str.upper() and str.lower()) to convert text to a standard case. Simple replacements using str.replace() or re.sub() can focus on removing or changing very specific character sequences. You can also normalize text using unicodedata.normalize().
* However, you might want to take the sanitation process a step further. Perhaps, for example, you want to eliminate whole ranges of characters or strip diacritical marks. To do so, you can use the str.translate() method. ===> Look at sanitize.py
* A major issue with sanitizing text can be runtime performance. As a general rule, the simpler it is, the faster it will run. Only use it if you need to perform any kind of nontrivial character-to-character remapping or deletion.
* Although the focus has been text, similar techniques can be applied to bytes, including simple replacements, translation, and regular expressions.

### Aligning text strings
* You need to format text with some sort of alignment applied. ==> look at stringText/alignment.py
* For basic alignment of strings, the ljust(), rjust(), and center() methods of strings can be used.
* Above methods also accept an optional fill character
* the format() function can also be used to easily align things. All you need to do is use the <, >, or ^ characters along with a desired width. You can also specify a fill character. ex: format(text, '=>20s')
* multiple strings example: '{:>10s} {:>10s}'.format('Hello', 'World')
* You can also use it with numbers: format(x, '^10.2f')
* In older code, you will also see the % operator be used however in newer code you should use the format() method since it is more powerful

### Combining and concatenating strings
* If the strings you wish to combine are found in a sequence or iterable , the fastest way to combine them is to use the join method. You specify the seperator string that you want and use the join() method on it to glue text fragments together. ===> see stringText/combiningConcatenating.py
* If you're only combining a few strings, using + usually works well enough
* If you're trying to combine string literals together in source code, you can simply place them adjacent to each other with no + operator.
* The most important thing to know is that using the + operator to join a lot of strings together is grossly inefficient due to memory copies and garbage collection that occurs. *In particular you never want to write code that joins strings together like this:*
  <pre>s = ''
  for p in parts:
    s += p
  </pre>
* This runs quite a bit slower than using the join() method, mainly because each += operation creates a new string object. You're better off just collecting all the parts first and then joining them together at the end.
* One related trick is the conversion of data to strings and concatenation at the same time using a generator expression.
<pre>
data = ['ACME', 50, 91.1]
s = ','.join[str(d) for d in data]
</pre>
* Last but not least, if you are writing code that is building output from lots of small strings, you might consider writing code as a generator function, using yield to emit fragments. The original generator function doesn't have to know the precise details. It just yields the parts.

### Interpolating variables in strings
* Python has no direct support for simply substituting variable values in strings. However, this feature can be approximated using the format() method of strings.
  =====> see string/Text/combininhConcatenating.py
  
## Numbers, Dates and Times
### Rounding numerical values
* For simple rounding, use the built-in round(value, ndigits) function
* When a value is exactly halfway between two choices, the behaviour of round is to round to the nearest even digit. That is, values such as
  1.5 or 2.5 both get rounded to 2.
* The number of digits given to round() can be negative, in which case rounding takes place for tens, hundreds, thousands, and so on.
* Don't confuse rounding with formatting a value for output. You can just specify the desired precision when formatting.
    * example: `'value is {:0.3f}'.format(x)`

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

## Network and Web Programming
### Interacting with http services as a client
* to send a simple http get request to a remote service you can use the urllib.request module



