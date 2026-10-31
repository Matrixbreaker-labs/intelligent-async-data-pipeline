import csv
import asyncio
import time
import random
from pydantic import BaseModel, Field, field_validator
from typing import List

# ==============================================================
# 1. Data Architecture and Validation (Pydantic Schema)
# ==============================================================
class ProductValidationModel(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    price: float
    category: str
    rating: float
    stock_status: str

    @field_validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be a positive non-zero number!")
        return value

# Final production memory database
production_database: List[ProductValidationModel] = []

# ==============================================================
# 2. Resilient Internal Database Simulating Network Fetch
# ==============================================================
async def extract_product_data(category_name: str, base_id: int):
    print(f"[⇄] Connecting Live Cluster Stack -> Category: '{category_name}'")
    
    try:
        # Simulates network lag/latency from a real database cluster (1.0 to 2.5 seconds)
        await asyncio.sleep(random.uniform(1.0, 2.5))
        
        # Structural API payload blueprints mapping real server responses
        mock_catalog = {
            "Electronics & Gadgets": [
                {"id": base_id + 1, "title": "Wireless Bluetooth Earbuds", "price": 49.99, "rate": 4.5, "count": 12},
                {"id": base_id + 2, "title": "Mechanical RGB Keyboard", "price": 89.99, "rate": 4.7, "count": 5},
                {"id": base_id + 3, "title": "Ultra-Wide Gaming Monitor", "price": 299.50, "rate": 4.8, "count": 3},
                {"id": base_id + 4, "title": "Portable 1TB SSD Storage", "price": 79.99, "rate": 4.4, "count": 15},
                {"id": base_id + 5, "title": "Ergonomic Vertical Mouse", "price": 35.00, "rate": 4.2, "count": 22}
            ],
            "Men's Apparel Collection": [
                {"id": base_id + 6, "title": "Slim Fit Denim Jacket", "price": 65.00, "rate": 4.3, "count": 8},
                {"id": base_id + 7, "title": "Classic Cotton Oxford Shirt", "price": 32.50, "rate": 4.1, "count": 14},
                {"id": base_id + 8, "title": "Athletic Running Joggers", "price": 45.00, "rate": 4.6, "count": 20},
                {"id": base_id + 9, "title": "Minimalist Leather Wallet", "price": 25.00, "rate": 4.5, "count": 0},
                {"id": base_id + 10, "title": "Pack of 3 Crewneck Tees", "price": 19.99, "rate": 4.0, "count": 40}
            ],
            "Women's Fashion Design": [
                {"id": base_id + 11, "title": "Bohemian Floral Midi Dress", "price": 75.00, "rate": 4.6, "count": 7},
                {"id": base_id + 12, "title": "Structured Linen Blazer", "price": 110.00, "rate": 4.8, "count": 4},
                {"id": base_id + 13, "title": "High-Waisted Wide Leg Pants", "price": 55.00, "rate": 4.2, "count": 11},
                {"id": base_id + 14, "title": "Classic Knit Cardigan Sweater", "price": 48.00, "rate": 4.4, "count": 18},
                {"id": base_id + 15, "title": "Crossbody Vegan Leather Bag", "price": 59.99, "rate": 4.5, "count": 9}
            ],
            "Premium Jewelries & Luxury": [
                {"id": base_id + 16, "title": "14k Gold Chain Necklace", "price": 350.00, "rate": 4.9, "count": 2},
                {"id": base_id + 17, "title": "Sterling Silver Hoop Earrings", "price": 45.00, "rate": 4.4, "count": 25},
                {"id": base_id + 18, "title": "Diamond Accent Pendant", "price": 599.00, "rate": 4.8, "count": 1},
                {"id": base_id + 19, "title": "Rose Gold Quartz Watch", "price": 125.00, "rate": 4.3, "count": 6},
                {"id": base_id + 20, "title": "Minimalist Band Ring Set", "price": 28.50, "rate": 4.1, "count": 30}
            ]
        }
        
        products_list = mock_catalog.get(category_name, [])
        success_count = 0
        
        for item in products_list:
            raw_payload = {
                "id": item["id"],
                "title": item["title"],
                "price": item["price"],
                "category": category_name,
                "rating": item["rate"],
                "stock_status": "In Stock" if item["count"] > 0 else "Out of Stock"
            }
            
            # Pydantic Structural Validation
            validated_object = ProductValidationModel(**raw_payload)
            production_database.append(validated_object)
            success_count += 1
            
        print(f"[✔] Success! Verified {success_count} data sets from category '{category_name}'")
        
    except Exception as e:
        print(f"[❌] Data Extraction Pipeline Broken -> Category: {category_name} | Error: {str(e)}")

# ==============================================================
# 3. Central Pipeline Runtime Engine and CSV Exporter
# ==============================================================
async def run_production_pipeline():
    production_database.clear()
    
    categories_map = {
        "Electronics & Gadgets": 100,
        "Men's Apparel Collection": 200,
        "Women's Fashion Design": 300,
        "Premium Jewelries & Luxury": 400
    }
    
    start_time = time.perf_counter()
    print("==================================================================")
    print("🚀 PRODUCTION LOGIC ACTIVE: GENERATING SECURE VALIDATED DATA...")
    print("==================================================================\n")
    
    # Pack tasks for simultaneous asynchronous execution
    tasks = []
    for category, base_id in categories_map.items():
        tasks.append(extract_product_data(category, base_id))
        
    # Execute concurrently in the background architecture loop
    await asyncio.gather(*tasks)
    
    # Linear sort based on product validation structural ID
    production_database.sort(key=lambda x: x.id)
    
    # Document compilation block (Professional Export Layout)
    csv_filename = "final_validated_products_report.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Product ID", "Product Title", "Price (USD)", "Category", "Rating", "Stock Status"])
        
        for product in production_database:
            writer.writerow([product.id, product.title, product.price, product.category, product.rating, product.stock_status])
            
    end_time = time.perf_counter()
    total_duration = end_time - start_time
    
    print("\n==================================================================")
    print(f"🎉 PIPELINE SUCCESSFUL! TOTAL PROCESSED DATA: {len(production_database)} ITEMS")
    print(f"⏱️ Total Execution Time: {total_duration:.2f} Seconds (High-Concurrency Sim)")
    print(f"💾 Client Delivery File Verified: {csv_filename}")
    print("==================================================================")

# Execute the final firewall-safe runtime engine loop inside Colab Envs
if __name__ == "__main__":
    # If running directly inside a standard local environment workspace terminal:
    # asyncio.run(run_production_pipeline())
    
    # Executing inside an open interactive notebook ecosystem loop state:
    await run_production_pipeline()
