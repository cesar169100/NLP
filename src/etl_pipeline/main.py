from prefect import flow, task
from ETLPipeline import etl_flow

# @task(name="Calculo de factorial")
# def factorial_task(numero):
#     factorial = 1
#     for i in range(1, numero+1):
#         factorial = factorial*i
#     return factorial

# @task(name="Suma")
# def suma_task(factorial):
#     suma = factorial + 10
#     return suma


# @flow(name='ETL Flow', log_prints=True, retries=2, retry_delay_seconds=5)
# def execute(numero):
#     fact = factorial_task(numero)
#     suma = suma_task(fact)
#     return suma


def main(numero):
    etl = etl_flow(numero)
    return etl

if __name__=="__main__":
    print(main(5))