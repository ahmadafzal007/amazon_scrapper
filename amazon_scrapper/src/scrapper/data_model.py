from datetime import datetime

class Product:
    def __init__(self, title, total_reviews, price, image_url):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_url = image_url
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "total_reviews": self.total_reviews,
            "price": self.price,
            "image_url": self.image_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }