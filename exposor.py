"""
    Exposor: A Python-based tool for unified exploration across multiple
    search engines.

    This module serves as the entry point for the Exposor tool, providing a
    command-line interface to query various feeds (e.g., Shodan, Fofa, Censys,
    ZoomEye) for assets based on given CPEs, CVEs, or custom queries.

    Features:
        - Queries multiple feeds concurrently.
        - Formats and outputs results to the console or CSV.

    Author:
        - Abdulla Abdullayev (Abu)
    Version:
        - 1.0.0
"""

from exposor.exposor import main

if __name__ == "__main__":
    main()
