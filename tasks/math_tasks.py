from celery_app.celery import app

@app.task(name='tasks.calculate_sum')
def calculate_sum(x, y):
    """
    A task that performs a simple calculation
    """
    result = x + y
    return f"Sum of {x} and {y} is {result}"

