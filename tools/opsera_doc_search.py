from urllib.parse import quote_plus

def search_opsera_docs(query=None):
    if not query:
        return "No query provided."
    
    search_url = f"https://docs.opsera.io/search?q={quote_plus(query)}" # have the user click on a link provided by the ai chatbot on information about Opsera.

    return f"You can search the Opsera documentation here: \n{search_url}"

