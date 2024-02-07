from pymongo import MongoClient

def save_to_mongodb(filename: str, cleaned_file_content: str, sentiment_results: float):
    """
    Save data to MongoDB.

    Parameters:
    - filename (str): The name of the file.
    - cleaned_file_content (str): The cleaned content of the file.
    - sentiment_results (float): The sentiment analysis results.

    Returns:
    None
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    
    # Specify the database and collection
    db = client["your_database_name"]
    collection = db["comments"]
    
    print(cleaned_file_content, 'lfeeerda')

    # Prepare the data to insert into the collection
    data_to_insert = {
        "filename": filename,
        "cleaned_file_content": cleaned_file_content,
        "Toxcity Level": sentiment_results
    }

    # Insert the data into the MongoDB collection
    collection.insert_one(data_to_insert)
