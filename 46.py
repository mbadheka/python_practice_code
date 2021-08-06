with open('Linkpractice.html','r') as webpage:
    with open('linkpractice.txt','a') as wf:
        for lines in webpage:
            if '<a href' in lines:
                pos = lines.find('a href= ')
                first_quotes = lines.find('\"',pos)
                second_quotes = lines.find('\"',first_quotes+1)
                URL = lines[first_quotes+1:second_quotes]
                wf.write(URL+'\n')