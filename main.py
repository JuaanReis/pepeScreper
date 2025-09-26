from src.output.banner import banner_info, display_links
from src.core.search_posts import search_threads, build_thread_links
from src.flags import parse_args

def main():
    banner_info()
    args = parse_args()
    resultados = search_threads(args)
    links = build_thread_links(resultados)
    display_links(links)
            
if __name__ == "__main__":
    main()