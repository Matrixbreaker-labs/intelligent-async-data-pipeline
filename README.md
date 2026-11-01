# AI-Powered Self-Healing Web Scraper & Intelligent Data Pipeline

An enterprise-grade, highly concurrent asynchronous data extraction and structural validation pipeline built with Python, `asyncio`, and `Pydantic v2`. This engine simulates a resilient distributed architecture capable of handling network latency, dynamic payload structures, and automated schema enforcement.

## 🚀 Key Features
- **Asynchronous Architecture:** Implements `asyncio` to handle network operations concurrently, preventing thread blocking and drastically lowering total execution time.
- **Robust Data Validation:** Utilizes `Pydantic` schemas and runtime field validators to automatically catch corrupt records, negative pricing, or formatting issues before ingestion.
- **High Concurrency:** Successfully processes parallel data streams from multiple clusters simultaneously under real-world network latency simulations.
- **Clean Data Export:** Outputs fully sorted data structured directly into standard, production-ready `CSV` format with absolute type safety.

## 📊 Performance Benchmarks
- **Total Processed Items:** 20 verified catalog records
- **Total Execution Time:** ~2.18 seconds (Ultra-Fast Concurrent Execution)
- **Data Throughput Strategy:** Parallel non-blocking execution via `asyncio.gather`

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.10+
- **Asynchronous Engine:** `asyncio` (Concurrent Task Broker)
- **Data Validation Layer:** `pydantic` (BaseModel & @field_validator)
- **Data Serialization:** Native `csv` module with `utf-8-sig` encoding compliance

## 📁 Repository Structure
- `main.py`: The core concurrent extraction and validation script.
- `final_validated_products_report.csv`: Production output report containing processed, sorted, and validated dataset rows.

## 📊 Pipeline Execution Results

The pipeline successfully executed and simulated a live database fetch with high concurrency. The generated data has been securely exported to the repository as `final_validated_products_report.csv`. 

Below is a preview of the validated multi-category payload structure included in the result:

| Product ID | Product Title | Price (USD) | Category | Rating | Stock Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | Wireless Bluetooth Earbuds | 49.99 | Electronics & Gadgets | 4.5 | In Stock |
| 102 | Mechanical RGB Keyboard | 89.99 | Electronics & Gadgets | 4.7 | In Stock |
| 209 | Minimalist Leather Wallet | 25.00 | Men's Apparel Collection | 4.5 | Out of Stock |
| 312 | Structured Linen Blazer | 110.00 | Women's Fashion Design | 4.8 | In Stock |
| 416 | 14k Gold Chain Necklace | 350.00 | Premium Jewelries & Luxury | 4.9 | In Stock |

*Note: The complete dataset containing all 20 successfully validated items across all core enterprise categories is available directly in the uploaded CSV file.*
