title_of_an_article = input()
content_of_that_article = input()
print(f"<h1>\n    {title_of_an_article}\n</h1>")
print(f"<article>\n    {content_of_that_article}\n</article>")
command = input()
while command != 'end of comments':
    comments = command
    print(f"<div>\n    {comments}\n</div>")
    command = input()