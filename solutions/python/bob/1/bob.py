"""
Function with Bob's answers.
"""

def response(hey_bob):
    """
    Function with Bob's answers.

    param: hey_bob - str: That's the question we ask Bob.
    return str - Bob's limited answers
    """

    element = '?'
    phrase = hey_bob.strip()
    is_shout = phrase.isupper()
    is_questions = phrase.endswith('?')

    if is_shout and is_questions:
        return "Calm down, I know what I'm doing!"
    if is_questions:
        return 'Sure.'        
    if is_shout:
        return 'Whoa, chill out!'
    if not phrase:
        return 'Fine. Be that way!'
    return 'Whatever.'
