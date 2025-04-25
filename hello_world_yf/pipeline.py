from openhexa.sdk import current_run, parameter, pipeline


@pipeline("my_first_pipeline_yf")
@parameter("my_name", type=str, required=True)
def my_hello_world(my_name):
    message = f"Hello {my_name}"
    log_message(message)


def log_message(message):
    current_run.log_info(message)
    print(message)


if __name__ == "__main__":
    my_hello_world()
