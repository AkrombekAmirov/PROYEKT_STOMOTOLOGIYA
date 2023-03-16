from sqlalchemy.orm.session import Session
from .models import Patients, TreatmentRecords, TreatmentTeeth, TreatmentHistory, DentalComplaints, Treatments, \
    Fillings, CleaningAgents, Extractions


class PatientRepository:
    def __init__(self, engine):
        self.engine = engine

    def create_petient(self, petient, created_by):
        session = Session(bind=self.engine)
        result = Patients(created_by=created_by, first_name=petient.first_name, last_name=petient.last_name,
                          address=petient.address, phone_number=petient.phone_number)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return Patients.from_orm(result)

    def create_treatmentteeth(self, **kwargs):
        session = Session(bind=self.engine)
        result = TreatmentTeeth(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return TreatmentTeeth.from_orm(result).id

    def get_treatment(self, **kwargs):
        session = Session(bind=self.engine)
        result = session.query(TreatmentTeeth).filter_by(**kwargs).first()
        session.close()
        return TreatmentTeeth.from_orm(result).id

    def get_treatments(self, patient_id: int):
        session = Session(bind=self.engine)
        result = session.query(TreatmentTeeth).filter_by(patient_id=patient_id).all()
        session.close()
        return result

    def get_treatment_(self, **kwargs):
        session = Session(bind=self.engine)
        result = session.query(TreatmentTeeth).filter_by(**kwargs).all()
        session.close()
        return TreatmentTeeth.from_orm(result).id

    def update_TreatmentTeeth(self, id: int, **kwargs):
        session = Session(bind=self.engine)
        for key, value in kwargs.items():
            setattr(session.query(TreatmentTeeth).filter_by(id=id).first(), key, value)
        session.commit()
        session.close()
        return True

    def TreatmentRecords(self, **kwargs):
        session = Session(bind=self.engine)
        result = TreatmentRecords(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return TreatmentRecords.from_orm(result)

    def create_dental_complaints(self, **kwargs):
        session = Session(bind=self.engine)
        result = DentalComplaints(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return DentalComplaints.from_orm(result)

    def get_treatment_records(self, **kwargs):
        session = Session(bind=self.engine)
        results = session.query(TreatmentRecords).filter_by(**kwargs).all()
        for result in results:
            result.complaint_id = session.query(DentalComplaints).filter_by(
                id=result.complaint_id).first().complaint_name
        session.close()
        return results

    def create_obj(self, table_name: str, **kwargs):
        session = Session(bind=self.engine)
        if table_name == 'Treatments': table_name = Treatments
        if table_name == 'Fillings': table_name = Fillings
        if table_name == 'CleaningAgents': table_name = CleaningAgents
        if table_name == 'Extractions': table_name = Extractions
        result = table_name(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        return result

    def create_history(self, **kwargs):
        session = Session(bind=self.engine)
        result = TreatmentHistory(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        return TreatmentHistory.from_orm(result)
