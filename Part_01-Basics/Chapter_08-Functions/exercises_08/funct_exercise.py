# Exercise 8-1 Message - write a funct called siplay_message() that prints one sentence telling everyone what you are learning about in this chapter.  call the function and make sure it displays correctly.
def display_message():
    print("Functions are a way to stor longer sections of code to re-use where you can pass different parameters.")

display_message()

# Exercise 8-2 Favorite Book - write a function favorite_book().  accepts a parameter "title" print a message with that parameter.
def favorite_book(title):
    print(f"my favorite book is {title.title()}.")

favorite_book('The Shining')