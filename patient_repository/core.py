from sqlalchemy.sql import func
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from .models import Patients, TreatmentTeeth, TreatmentHistory, DentalComplaints, Treatments, \
    Fillings, CleaningAgents, Extractions, QueuePatient

queue = 1


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

    def get_petients(self):
        session = Session(bind=self.engine)
        result = session.query(Patients).all()
        session.close()
        return result

    def get_petient(self, id: int):
        session = Session(bind=self.engine)
        result = session.query(Patients).filter_by(id=id).first()
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
        return result

    def update_TreatmentTeeth(self, id: int, **kwargs):
        session = Session(bind=self.engine)
        for key, value in kwargs.items():
            setattr(session.query(TreatmentTeeth).filter_by(id=id).first(), key, value)
        session.commit()
        session.close()
        return True

    def create_dental_complaints(self, **kwargs):
        session = Session(bind=self.engine)
        result = DentalComplaints(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return DentalComplaints.from_orm(result)

    def create_obj(self, create_obj):
        session = Session(bind=self.engine)
        if create_obj.table_name == 'Treatments': table_name = Treatments
        if create_obj.table_name == 'Fillings': table_name = Fillings
        if create_obj.table_name == 'CleaningAgents': table_name = CleaningAgents
        if create_obj.table_name == 'Extractions': table_name = Extractions
        if create_obj.table_name == 'DentalComplaints': table_name = DentalComplaints
        result = table_name(name=create_obj.name, price=create_obj.price)
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

    def gets_history(self, **kwargs):
        session = Session(bind=self.engine)
        result = session.query(TreatmentHistory).filter_by(**kwargs).all()
        session.close()
        return TreatmentHistory.from_orm(result)

    def get_history(self, id):
        session = Session(bind=self.engine)
        result = session.query(TreatmentHistory).filter_by(id=id).first()
        session.close()
        return TreatmentHistory.from_orm(result)

    def update_history(self, id: int, **kwargs):
        session = Session(bind=self.engine)
        for key, value in kwargs.items():
            setattr(session.query(TreatmentHistory).filter_by(id=id).first(), key, value)
        session.commit()
        session.close()
        return True

    def create_queue(self, patient_id: int, doctor_id: int):
        session = Session(bind=self.engine)
        max_queue_number = session.query(func.max(QueuePatient.queue_number)).scalar()
        if session.query(QueuePatient).filter_by(patient_id=patient_id).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Patient queue conflict")
        session.add(QueuePatient(patient_id=patient_id, doctor_id=doctor_id,
                                 queue_number=max_queue_number + 1 if max_queue_number is not None else 1))
        session.commit()
        return max_queue_number + 1 if max_queue_number is not None else 1

    def get_queue(self, doctor_id: int):
        session = Session(bind=self.engine)
        results = session.query(QueuePatient).filter_by(doctor_id=doctor_id).all()
        for result in results:
            result.patient_id = session.query(Patients).filter_by(id=result.patient_id).first()
        session.close()
        return results

    def remove_queue(self, id):
        session = Session(bind=self.engine)
        session.query(QueuePatient).filter_by(id=id).delete()
        session.commit()
        session.close()
        return True

    def clear_queue(self):
        session = Session(bind=self.engine)
        session.query(QueuePatient).delete()
        session.commit()
        session.close()
        return True
