from passage_loader import load_passage

def every_ith_word(passage_path: str, i: int) -> list[str]:
    passage = load_passage(passage_path)
    words = passage.split(' ')
    hints = []
    iterator = 0
    while iterator < len(words):
        hints.append(words[iterator])
        iterator += i

    return hints
    
if __name__ == '__main__':
    every_third = every_ith_word('./passages/passage1.txt', 3)
    print('h')

        
        