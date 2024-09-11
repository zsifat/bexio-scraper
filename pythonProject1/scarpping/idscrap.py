from bs4 import BeautifulSoup
from lxml.builder import unicode

soup = BeautifulSoup('<p class="body strikeout">HI</p>', 'xml',multi_valued_attributes={'*':'class'})
tag = soup.p
tag['id']='font'
tag.string.replace_with('Hello')
print(unicode(tag.string))

print(tag['class'])
