books = {
     1:{"title": "Алхимик", "author": "Пауло Коэльо", "year": "1988"},
     2:{"title": "Дежавю. Богемский рэп, сода и я", "author": "Олег Нечипоренко ", "year": "2022"},
     3:{"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": "1866"},
     4:{"title": "Евгений Онегин", "author": "Александр Пушкин", "year": "1833"},
     5:{"title": "Сто лет одиночества", "author": "Габриэль Гарсиа Маркес", "year": "1967"}
}
count = 1

for key,book in books.items():
    print("-"*25,"Книга",count,"-"*25)
    print("Название:",book['title'],end=", ")
    print("Автор:",book['author'])
    print("-"*25,book['year'],"-"*25)
    count+=1