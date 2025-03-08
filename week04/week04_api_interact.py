import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    
    response = requests.post(url, json=book)
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), head
    
    return response.json()


def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()
    pass

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()




def main():
    books = getAllBooks()
    if not books:
        print("No books available.")
        return
    
    prices = [book.get('price', 0) for book in books]
    print(f"Average price: ${sum(prices) / len(prices):.2f}" if prices else "No price data.")


if __name__ == "__main__":
    book= {
        'author':"myone",
        'title':"tests",
        "price": 1200
    }
    bookdiff= {
        "price": 1234444
    }
    main()
    #print(getAllBooks())
    #print(getBook(1181))
    #print (deleteBook11816))
    #print (deleteBook(81))
    #print (createBook(book))
    #print (updateBook(22, bookdiff))