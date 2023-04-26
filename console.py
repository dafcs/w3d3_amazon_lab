import repositories.author_repository as author_repo
import repositories.book_repository as book_repo
from models.author import Author
from models.book import Book


author_repo.delete_all()

author_1 = Author('Aaw')
author_repo.save(author_1)
print(author_1.__dict__)
printme0 = author_repo.select(author_1.id)
print(printme0.__dict__)

printme = author_repo.select_all()
for prints in printme:
    print(prints.__dict__)

book_repo.delete_all()

author_1 = Author('Aaw')
author_repo.save(author_1)
print(author_1.__dict__)
printme0 = author_repo.select(author_1.id)
print(printme0.__dict__)

printme = author_repo.select_all()
for prints in printme:
    print(prints.__dict__)

