
def parse_citation_save(title, citation, passages):
    
    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n")
        file.write(f"Number of citations needed: {citation}\n")
        for passage in passages:
            file.write(f"Citation needed for: \"{passage}\"\n")
        
        