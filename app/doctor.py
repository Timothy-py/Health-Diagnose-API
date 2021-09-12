import re
import json


class Doctor:
    """
    this class does two main things - i. to ask the patient for his feelings
    ii. to diagnose the patient base on those feelings.
    """

    # load the ailment_symptoms.json file as a json object
    with open("ailment_symptoms.json", "w+") as fileObj:
        data = json.load(fileObj)

    # this class variable stores symptoms and their most probable ailment in a dictionary
    doctor_brain = data["ailment_symptoms"]

    def __init__(self):
        """
        the constructor ask the patient for his feelings as a user-input and stores it in
        patient_response instance variable.
        """
        self.patient_symptoms = []
        # self.patient_response = ""
        self.patient_possible_ailment = []
        self.patient_ailment_count = []

    def diagnose_patient(self, patient_response):
        """
         this method contain logic to determine the most probable ailment of patient from
         the response provided.
        """

        try:
            # check for words patient_response variable which correspond to symptom in the doctor_brain variable and
            # append such word(symptom) to patient_symptoms variable. Done through the use of regular expression.
            # symptomsRegex = re.compile(r'cold|fever|cough|headache|stool|temperature|'
            #                            r'catarrh|vomiting|stomach-ache|diarrhoea', re.I)

            symptomsFileObj = open("symptomsFile.txt", "w+")
            for symptom in self.doctor_brain:
                symptomsFileObj.write(symptom + "|")
            symptomsFileObj.close()

            symptomsFileObj = open("symptomsFile.txt", 'r')
            symptoms_string = symptomsFileObj.read()

            symptomsRegex = re.compile(r"{}".format(symptoms_string), re.I)
            # print(symptoms_strings)
            self.patient_symptoms = symptomsRegex.findall(
                patient_response)
            print("PATIENT SYMPTOMS: {}".format(self.patient_symptoms))

            self.patient_symptoms = list(
                filter(lambda a: a != '', self.patient_symptoms))
            print("PATIENT SYMPTOMS: {}".format(self.patient_symptoms))

            # Store the values(ailments) of keys(symptoms) in the doctor_brain to
            # patient_possible_ailment variable. Done through the use of list comprehension
            self.patient_possible_ailment = [
                self.doctor_brain[symptom] for symptom in self.patient_symptoms]

            # This code suit does two things simultaneously:
            # At first it is a filtered list of patient_possible_ailment list to make sure an ailment appears just once.
            # It then count the original appearance of each ailment in the patient_possible_ailment list
            # and append the number of appearance of each ailment to patient_ailment_count list.
            self.patient_ailment_count = [self.patient_possible_ailment.count(ailment)
                                          for ailment in self.patient_possible_ailment
                                          if ailment not in self.patient_ailment_count]

            # This code suit determines the most probable ailment of the patient by checking
            # for the max value in patient_ailment_count list, determining the index of such value,
            # and then, list indexing the index returned from patient_ailment_count list into
            # patient_possible_ailment to determine the actual patient ailment.
            self.patient_ailment = self.patient_possible_ailment[
                self.patient_ailment_count.index
                (max(self.patient_ailment_count))]

        except ValueError:
            return "Sorry! I can't get any symptom from your response. Be detailed!"

        else:
            return "Oh Sorry! You\'re probably suffering from {} infection.".format(
                self.patient_ailment)
