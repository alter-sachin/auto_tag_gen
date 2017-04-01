#!/usr/bin/env python
def naivebayes(string_tags, global_var):
    import os
    import codecs
    pathname = "eattreat_nlp_taggenerator/"
    paths = ['Bakery&Sweets/', 'Snacks/', 'Meats/', 'Organics/', 'Other/',
             'Drinks/', 'Restaurants/']
    path1 = ['Bakery&Sweets', 'Snacks', 'Meats', 'Organics', 'Other', 'Drinks',
             'Restaurants']

    vocab = [{}, {}, {}, {}, {}, {}, {}]
    V = []
    alltags = set()
    classoccur = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for p, path in enumerate(paths):

        for filename in os.listdir(pathname + path):
            if not filename.startswith('.'):
                classoccur[p] += 1
                inputfile = codecs.open(pathname + path + filename, 'r')
                for line in inputfile:
                    content = line.split("\t")
                    post_id = content[0]  # not being used anywhere
                    post_title = content[1] # not being used anywhere
                    post_tags = content[2]
                    tags = post_tags.split(', ')
                    for t in tags:
                        tt = t.split("-")
                        for ttt in tt:
                            if ttt not in alltags:
                                alltags.add(ttt)
                            if ttt not in vocab[p]:
                                vocab[p].update({ttt: 1})
                            else:
                                vocab[p][ttt] += 1

        V.append(sum(vocab[p].values()))
    if global_var < 2:
        for alpha, _ in enumerate(vocab):
            classdict = open(
                "eattreat dictionary/dictionary_" + path1[alpha] + ".txt", "a")
            #   print vocab[alpha]
            #   print '\n\n'
            for key in vocab[alpha]:
                classdict.write(
                    str(key) + "\t" + str(vocab[alpha][key]) + "\n")

    naive = [{}, {}, {}, {}, {}, {}, {}]
    lenalltags = len(alltags)

    test_tags = [] # not being used anywhere

    total_tags = string_tags.split(", ")

    sum1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for k, voca in enumerate(vocab):
        s = 1.0
        for e in total_tags:
            t = e.split("-")
            for t2 in t:
                if t2 not in alltags:
                    alltags.add(t2)
                    lenalltags += 1
                if t2 not in voca:
                    voca.update({t2: 1})
                    V[k] += 1
                else:
                    voca[t2] += 1
                    V[k] += 1
                naive[k].update({t2: float(
                    float(1 + voca[t2]) / float(lenalltags + V[k]))})
                s = s * naive[k][t2]

        beta = float(s * (classoccur[k] / sum(classoccur)))
        sum1[k] = beta

    inputfile.close()

    max_value = max(sum1)
    max_index = sum1.index(max_value)

    classoccur[max_index] += 1

    print path1[max_index]
    return path1[max_index]

    # naivebayes()
