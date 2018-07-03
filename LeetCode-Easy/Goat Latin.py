
def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """

    def convert(S):
        vowel = set('aeiouAEIOU')
        for i, word in enumerate(S.split(), 1):
            if word[0] not in vowel:
                word = word[1:] + word[:1]
            result.append(word + 'ma' + 'a' * i)

    result= []
    convert(S)
    return " ".join(result)
