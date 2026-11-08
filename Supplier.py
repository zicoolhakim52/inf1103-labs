class Supplier:
    def __init__(self,supplier_id: str,name: str,contact_email: str):
        self._supplier_id=supplier_id
        self._name=name
        self._contact_email=contact_email

    def display_information(self)-> None:
        print(f"Supplier name: {self._name} | Supplier ID: {self._supplier_id} | Supplier Email:{self._contact_email}", end=" | ")
