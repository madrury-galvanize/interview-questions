import random

TOPIC_COUNTS = {
    "statistics": 14,
    "kahneman": 4,
    "regression": 10
}

TOPICS = list(TOPIC_COUNTS)

def random_question():
    topic = random.choice(TOPICS)
    question = random.choice(range(TOPIC_COUNTS[topic])) + 1
    return topic, question

if __name__ == "__main__":
    topic, question = random_question()
    print("Ask question {} from topic {}.".format(question, topic))
