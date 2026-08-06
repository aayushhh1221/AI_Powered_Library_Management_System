from App.utils.llm import llm
from App.prompts.similar_books import similar_books_prompt
from App.parsers.similar_book_parser import similar_book_parse

similar_chain=similar_books_prompt|llm|similar_book_parse