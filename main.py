import json
import random
import time

from faker import Faker
from confluent_kafka import SerializingProducer
from datetime import datetime

faker = Faker()

def generate_sales_transactions():
    user = faker.simple_profile()

    return {
        "transactionId": faker.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),
        "productName": random.choice(['laptop', 'mobile', 'tablet', 'watch', 'headphone', 'speaker','sneakers', 'tshirt', 'jeans', 'sweater', 'jacket', 'socks', 'shoes', 'perfume', 'lipstick', 'shampoo', 'conditioner', 'facewash', 'bodywash', 'protein', 'vitamins', 'supplements', 'gloves', 'dumbells', 'yoga mat', 'treadmill', 'cycle', 'football', 'cricket bat', 'badminton racket', 'tennis ball', 'basketball', 'volleyball', 'skipping rope', 'gym bag', 'water bottle', 'protein shaker']),
        'productCategory': random.choice(['electronic', 'fashion', 'grocery', 'home', 'beauty', 'sports', 'fitness']),
        'productPrice': round(random.uniform(10, 1000), 2),
        'productQuantity': random.randint(1, 10),
        'productBrand': random.choice(['apple', 'samsung', 'oneplus', 'mi', 'boat', 'sony', 'jbl', 'nike', 'adidas', 'puma', 'reebok', 'zara', 'hm', 'forever21', 'mango', 'gucci', 'prada', 'versace', 'armani', 'dolce&gabbana', 'underarmour', 'asics', 'nivia', 'yonex', 'cosco', 'spalding']),
        'currency': random.choice(['USD', 'GBP']),
        'customerId': user['username'],
        'transactionDate': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer'])
    }

def delivery_report(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def main():
    topic = 'sales_transactions'
    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092',
    })

    curr_time = datetime.now()

    while (datetime.now() - curr_time).seconds < 120:
        try:
            transaction = generate_sales_transactions()
            transaction['totalAmount'] = transaction['productPrice'] * transaction['productQuantity']

            print(f"Producing transaction: {transaction}")

            producer.produce(topic=topic, key=transaction['transactionId'], value=json.dumps(transaction), on_delivery=delivery_report)
            producer.poll(0)

            # wait for 5 seconds before sending next message (transaction)
            time.sleep(5)
        except BufferError:
            print(f"Local producer queue is full ({len(producer)} messages awaiting delivery): try again")
        except Exception as e:
            print(f"An error occurred: {e}")
    
if __name__ == '__main__':
    main()
