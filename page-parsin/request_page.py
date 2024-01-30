from parsing_page import parse
from save_citation import parse_citation_save

def main():
    url = "https://en.wikipedia.org/wiki/Terraria"
    title, num_citations, citation_passages = parse(url)

    print(f"Number citations needed, {num_citations}\n")
    for passage in citation_passages:
        print(f"Citation needed for: \"{passage}\"\n")
        
    parse_citation_save(title, num_citations, citation_passages)
        
        
main()