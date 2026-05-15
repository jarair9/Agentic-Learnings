import time


CACHE = {}


def expensive_search(query: str) -> str:
    """Pretend this search is slow."""

    time.sleep(0.1)
    return f"Search results for: {query}"


def cached_search(query: str) -> str:
    cache_key = f"search:{query.lower()}"

    if cache_key in CACHE:
        return f"CACHE HIT -> {CACHE[cache_key]}"

    result = expensive_search(query)
    CACHE[cache_key] = result
    return f"CACHE MISS -> {result}"


def main() -> None:
    print(cached_search("agent loops"))
    print(cached_search("agent loops"))


if __name__ == "__main__":
    main()

