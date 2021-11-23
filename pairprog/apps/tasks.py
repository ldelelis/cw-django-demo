from celery import shared_task


@shared_task
async def update_domain_record(new_record: str):
    print(f"domain updated with record {new_record}")
