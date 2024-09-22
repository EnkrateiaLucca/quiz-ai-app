from langchain.prompts import ChatPromptTemplate

def create_multiple_choice_template():
    """Create the prompt template for the quiz app."""
    
    template = """
You are an expert quiz maker for technical fields. Let's think step by step and
create a quiz with {num_questions} questions about the following concept/content: {quiz_context}.

The format of the quiz is as follows:
- Multiple-choice: 
- Questions:
    <Question1>: 
        - Alternatives1: <a. Answer 1>, <b. Answer 2>, <c. Answer 3>, <d. Answer 4>
    <Question2>: 
        - Alternatives2: <a. Answer 1>, <b. Answer 2>, <c. Answer 3>, <d. Answer 4>
    ....
- Answers:
    <Answer1>: <a|b|c|d>
    <Answer2>: <a|b|c|d>
    ....
    Example:
    - Questions:
    - 1. What is the time complexity of a binary search tree?
        a. O(n)
        b. O(log n)
        c. O(n^2)
        d. O(1)
    - Answers: 
        1. b
"""
    prompt = ChatPromptTemplate.from_template(template)
    
    return prompt


def create_true_false_template():
    """Create the prompt template for the quiz app."""
    
    template = """
        You are an expert quiz maker for technical fields. Let's think step by step and
        create a quiz with {num_questions} questions about the following concept/content: {quiz_context}.

The format of the quiz is as follows:
- True-false:
    - Questions:
        <Question1>: <True|False>
        <Question2>: <True|False>
        .....
    - Answers:
        <Answer1>: <True|False>
        <Answer2>: <True|False>
        .....
    Example:
    - Questions:
        - 1. A binary search tree is a data structure that is used to store data in a sorted manner.
        - 2. Binary search trees are implemented using linked lists.
    - Answers:
        - 1. True
        - 2. False
"""
    
    prompt = ChatPromptTemplate.from_template(template)
    
    return prompt


def create_open_ended_template():
    """Create the prompt template for the quiz app."""
    
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a quiz with {num_questions} questions about the following concept/content: {quiz_context}.
    The format of the quiz is as follows:
        - Open-ended:
    - Questions:
        <Question1>: 
        <Question2>:
    - Answers:    
        <Answer1>:
        <Answer2>:
    Example:
        Questions:
        - 1. What is a binary search tree?
        - 2. How are binary search trees implemented?
        
        - Answers: 
            1. A binary search tree is a data structure that is used to store data in a sorted manner.
            2. Binary search trees are implemented using linked lists.
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    return prompt