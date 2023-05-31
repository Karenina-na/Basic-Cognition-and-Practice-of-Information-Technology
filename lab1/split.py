if __name__ == "__main__":
    Str = '寒雨连江夜入吴，平明送客楚山孤。洛阳亲友如相问，一片冰心在玉壶。'
    sentences = Str.split(sep='，')
    for sentence in sentences:
        print(sentence)
