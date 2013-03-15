def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    import re

    patternurls = r'(?<=<a href=\").+(?=\"\>)'
    patterntext = r'(?<=\"\>).+(?=\</a\>)'
    
    f = open(filename)
    site = f.read()
    
    values = re.findall(patternurls, site)
    keys = re.findall(patterntext, site)
    
    dct = dict(zip(keys, values))

    f.close()    

    return dct


def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    
    from lxml.html import iterlinks

    f = open(filename)
    site = f.read()

    html = iterlinks(site)
    values = []
    keys = []

    for a in html:
        keys.append(a[0].text)
        values.append(a[2])

    dct = dict(zip(keys, values))

    f.close()
    return dct