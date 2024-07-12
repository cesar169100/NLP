from prefect import flow, task
from etl_task_definitions import factorial_task, suma_task

@flow(name='ETL Flow', log_prints=True, retries=2, retry_delay_seconds=5)
def etl_flow(numero):
    factorial = factorial_task(numero)
    suma = suma_task(factorial)
    return suma