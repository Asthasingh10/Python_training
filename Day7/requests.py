import requests
from bs4 import  BeautifulSoup
with open("sample.html","r") as f:
    html_doc=f.read()
soup=BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
# print(soup.title.name ,type(soup.title.string))
# print(soup.findAll("div"))

# for link in soup.find_all("a"):
#     print(link.get("href"))
#       print(link.get_text())

# s=soup.find(id="specialLink")
# print(s)
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.span.get("class"))
# print(soup.find(class_="italic"))

# for parent in soup.find(class_="box").parents:
#     print(parent)

# count=soup.find(class_="container")
# count.name="span"
# print(count)


# TO INSERT NEW TAG
# ulTag=soup.new_tag("ul")
# liTag=soup.new_tag("li")
# liTag.string="Home"
# ulTag.append(liTag)

# liTag=soup.new_tag("li")
# liTag.string="About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)
# with open("modified.html","w") as f:
#     f.write(str(soup))

# TO FIND IN TAG THAT ATTRIBUTE IS AVAILABLE OR NOT
# cont=soup.find(class_="container")
# print(cont.has_attr("id"))

# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")
# result=soup.find_all(has_class_but_not_id)
# for result in result:
#     print(result,"\n\n")