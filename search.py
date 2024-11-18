try:
    from googlesearch import search
except ImportError:
    print("Module not found.\n")

query=input("Search your query here!..\n")

for i in search(query,tld="com",num=10,stop=10,pause=2):
    print(i)
