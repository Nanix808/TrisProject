from confluent_kafka import Producer
from random import choice
import socket

if __name__ == "__main__":
    print("Запускаем наш producer")
    config = conf = {
        "bootstrap.servers": "localhost:9092,localhost:9093,localhost:9094",
        "client.id": socket.gethostname(),
        # "security.protocol": "SSL",
    }

    producer = Producer(config)

    topic = "user-actions"
    user_ids = ["Иван", "Андрей", "Игорь", "Сергей", "Мухаммад", "Рамиль"]
    actions = ["регистрация", "аутентификаця", "выход", "подписка", "лайк"]

    def delivery_callback(err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(actions)
        producer.produce(topic, product, user_id, callback=delivery_callback)
        count += 1

    # producer.poll(10000)
    producer.flush()
