# 🚢 Shipping System API
This is a Shipping System API to calculate the shipping costs based on package weight and shipping type.

# Features
- Calculate shipping cost for:
  - Ground Shipping
  - Drone Shipping
  - Premium Shipping
- Determine the cheapest shipping method
- Predefined shipping types using Enum
- Input validation using Pydantic
- Simple and structured API design

# Tools
- Python
- FastAPI
- Pydantic
- Enum

# How to Run
1. Clone the repository:

   ```
   git clone https://github.com/GabrielObuti/shipping-system
   
   cd shipping_system
   ```
   
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the server:
   ```
   uvicorn app:app --reload
   ```
5. Open in your browser:
   ```
   http://127.0.0.1:8000/docs
   ```
# What I learned
- How to build APIs using FastAPI
- How to validate data using Pydantic
- How to define fixed values using Enum
- How to structure backend logic
- How HTTP requests and responses work

# Future Improvements
- Add Docker support
- Improve error handling
   
