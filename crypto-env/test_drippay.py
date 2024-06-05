import drippay

# Initialize the library
if drippay.initialize_drip_pay():
    print("Library initialized successfully")

# Process a microtransaction
if drippay.process_microtransaction(1, 10.0, "Sample Transaction"):
    print("Transaction processed successfully")

# Finalize the library
if drippay.finalize_drip_pay():
    print("Library finalized successfully")
