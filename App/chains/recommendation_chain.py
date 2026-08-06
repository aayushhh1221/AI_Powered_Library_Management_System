from App.utils.llm import llm
from App.prompts.librarian import LIBRARIAN_PROMPT
from App.parsers.recommendation_parser import recommendation_parser


chat_chain=(LIBRARIAN_PROMPT|llm|recommendation_parser)