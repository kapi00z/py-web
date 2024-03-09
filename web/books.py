import requests, os, re, json

bookDir = os.path.join(os.getcwd(), 'books')

def addBook(book):
    bPath = os.path.join(bookDir, 'books.json')
    if os.path.isfile(bPath):
        with open(bPath, 'r') as file:
            books = json.loads(file.read())
    else:
        books = {}
    
    books.update({book['id']: book})
    with open(bPath, 'w') as file:
        file.write(json.dumps(books))

def getIdx():
    with open("books/.index/nums.txt", "r") as file:
        data = file.read().split()

    idx = [int(x) for x in list(dict.fromkeys(data))]
    idx.sort()
    
    return idx

def getWords(data):
    ret = {}
    clean = re.sub(r'\W+', ' ', data.lower()).split()
    for word in clean:
        if word in ret:
            ret[word] += 1
        else:
            ret[word] = 1
    return ret

def getBook(id=None):
    if id is None:
        return "No value provided!"
    if id not in getIdx():
        return "Incorrect id provided!"
    bookUrl = f"https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"
    response = requests.get(bookUrl)
    text = response.text
    with open(f'{bookDir}/{id}.txt', 'w') as file:
        file.write(text)
    book = {'id': id, 'url': bookUrl, 'words': getWords(text)}
    addBook(book)
    return(book)

for i in [110, 111, 112, 113, 115, 117, 118, 119]:
    getBook(i)