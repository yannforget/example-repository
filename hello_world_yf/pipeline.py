from openhexa.sdk import pipeline, workspace


@pipeline("my_first_pipeline_yf")
def my_hello_world():
    log_message("Hello world")


def log_message(message):
    print(message)


if __name__ == "__main__":
    my_hello_world()
