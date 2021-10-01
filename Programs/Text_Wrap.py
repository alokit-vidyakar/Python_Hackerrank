#https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap


# brute force method
"""def wrap(string, max_width):
    a =[]
    index =0
    while index < len(string):
    	substring = string[index:index+max_width]
    	a.append(substring)
    	index = index+max_width
    print(a)"""
#hackerrank solution
def wrap(string,max_width):
	return( textwrap.fill(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
"""    print(textwrap.wrap(string, max_width))
    print(textwrap.fill(string, max_width))
"""

"""now there is a module called textwrap which is used for working around texts only.
The methods which are availbale are:

1. textwrap.wrap(string, width) #breaks the string after given width length and return an array of 
2. textwrap.shorten(string, width) #for truncating the text
3. textwrap.dedent(string) # for removing indentation 
4. textwrap.indent(string,"\t") #for adding indentation
5. textwrap.fill(string,width) # same as wrap but returns a single string containing the wrapped paragraph 
"""
	