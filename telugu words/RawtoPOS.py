with open("telugu.output.txt", encoding='utf-8') as handle:
    with open("adjectives.txt",'wb') as output:
        with open("adverb.txt",'wb') as output1:
            with open("verb.txt",'wb') as output2:
                for line in handle:
                    if line.startswith('<')==False and line.endswith('>')==False :
                        words=line.split()
                        if words[1]=='JJ':
                            output.write(words[0].encode('utf-8')+'\n'.encode('utf-8'))
                        if words[1]=='RB':
                            output1.write(words[0].encode('utf-8')+'\n'.encode('utf-8'))
                        if words[1]=='VM':
                            output2.write(words[0].encode('utf-8')+'\n'.encode('utf-8'))
