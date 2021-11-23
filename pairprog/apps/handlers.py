from apps.tasks import update_domain_record


class AppHandler():
    def update_domain_record(self, new_record: str):
        update_domain_record.delay(new_record=new_record)
