import repositories.author_repository as author_repo
import repositories.book_repository as book_repo
from models.author import Author
from models.book import Book

book_repo.delete_all()
author_repo.delete_all()


author_1 = Author('Aaw')
author_2 = Author('Aawe')
author_3 = Author('Aa')
author_list = [author_1,author_2,author_3]
for author in author_list:
    author_repo.save(author)


printmeauthor = author_repo.select_all()
for prints in printmeauthor:
    print(prints.__dict__)



book_1 = Book('MyTitle1',author_1)
book_2 = Book('MyTitle2',author_1)
book_3 = Book('MyTitle3',author_1)
book_4 = Book('MyTitle4',author_2)
book_5 = Book('MyTitle5',author_2)
book_6 = Book('MyTitle6',author_2)
book_7 = Book('MyTitle7',author_3)
book_list = [book_1,book_2,book_3,book_4,book_5,book_6,book_7]

for book in book_list:
    book_repo.save(book)


printmebook = book_repo.select_all()
for prints in printmebook:
    print(prints.__dict__)

