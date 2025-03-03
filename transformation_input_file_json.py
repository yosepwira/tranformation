import sys
import os 
import json
import base64
import logging
from datetime import datetime, date, timezone
import time

#setlog
logging.basicConfig(
    filename = 'transformation.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


class Transformation_1 :

    DEFAULT_VALUES = {
        "message_type": "9999",
        "processing_code": "999999",
        "amount_tran": "0.00",
        "primary_account_number": "000000********0000",
        "sender_account_number": "invalid_value",
        "beneficiary_account_number": "000000********0000",
        "transmission_date_time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
        "transaction_date": "1900-01-01"
    }

    @staticmethod
    def log_missing_field(field_name):
        logging.warning(f"Missing Field: {field_name}, setting default value ")


    @staticmethod
    def p_message_type(message_type):
        """Set message_type"""
        if not message_type:
            Transformation_1.log_missing_field("message_type")
            return Transformation_1.DEFAULT_VALUES["message_type"]
        try:
            return int(message_type)
        except ValueError as e:
            logging.error(f"Error tranform message_type : {message_type} - {e}")
            return Transformation_1.DEFAULT_VALUES["message_type"]
    
    @staticmethod
    def p_processing_code(processing_code):
        """"Set processing_code"""
        if not processing_code:
            Transformation_1.log_missing_field("processing_code")
            return Transformation_1.DEFAULT_VALUES["processing_code"]
        try:
            return int(processing_code)
        except ValueError as e:
            logging.error(f"Error tranform processing_code : {processing_code} - {e}")
            return Transformation_1.DEFAULT_VALUES["processing_code"]

        # return int(processing_code)
    
    @staticmethod
    def p_amount_tran(amount_tran):
        """ Set amount_tran """
        # return format(int(amount_tran)/100,".2f")
        if not amount_tran:
            Transformation_1.log_missing_field("amount_tran")
            return Transformation_1.DEFAULT_VALUES["amount_tran"]
        try:
            return format(int(amount_tran)/100,".2f")
        except ValueError as e:
            logging.error(f"Error tranform amount_tran : {amount_tran} - {e}")
            return Transformation_1.DEFAULT_VALUES["amount_tran"]        
    
    @staticmethod
    def p_primary_account_number(primary_account_number):
        """Set primary_account_number """
        # return primary_account_number[:6] + "*********" + primary_account_number[-4:]
        if not primary_account_number:
            Transformation_1.log_missing_field("primary_account_number")
            return Transformation_1.DEFAULT_VALUES["primary_account_number"]
        try:
            return primary_account_number[:6] + "*********" + primary_account_number[-4:]
        except ValueError as e:
            logging.error(f"Error tranform primary_account_number : {primary_account_number} - {e}")
            return Transformation_1.DEFAULT_VALUES["primary_account_number"]        
    
    
    @staticmethod
    def p_sender_account_number(sender_account_number):
        """Set sender_account_number """                   
        if not sender_account_number:
            Transformation_1.log_missing_field("sender_account_number")
            return Transformation_1.DEFAULT_VALUES["sender_account_number"]
        try:
            encoded_bytes = base64.b64encode(sender_account_number.encode("utf-8"))
            return encoded_bytes.decode("utf-8")
        except ValueError as e:
            logging.error(f"Error tranform sender_account_number : {sender_account_number} - {e}")
            return Transformation_1.DEFAULT_VALUES["sender_account_number"]                
    


    @staticmethod
    def p_beneficiary_account_number(beneficiary_account_number):
        """Set beneficiary_account_number """
        # return (beneficiary_account_number)
        # return beneficiary_account_number[:6] + "*********" + beneficiary_account_number[-4:]
        if not beneficiary_account_number:
            Transformation_1.log_missing_field("beneficiary_account_number")
            return Transformation_1.DEFAULT_VALUES["beneficiary_account_number"]
        try:
            return beneficiary_account_number[:6] + "*********" + beneficiary_account_number[-4:]
        except ValueError as e:
            logging.error(f"Error tranform beneficiary_account_number : {beneficiary_account_number} - {e}")
            return Transformation_1.DEFAULT_VALUES["beneficiary_account_number"]                
    
    @staticmethod
    def p_transmission_date_time(transmission_date_time):
        """Set transmission_date_time"""    
        if not transmission_date_time:
            Transformation_1.log_missing_field("transmission_date_time")
            return datetime.strptime(Transformation_1.DEFAULT_VALUES["transmission_date_time"], "%Y-%m-%dT%H:%M:%S.000Z")         
        try:
            current_year=date.today().year
            dt = datetime.strptime(f"{current_year}{transmission_date_time}","%Y%m%d%H%M%S")
            return dt
        except ValueError as e:
            logging.error(f"Error tranform transmission_date_time : {transmission_date_time} - {e}")
            # return Transformation_1.DEFAULT_VALUES["transmission_date_time"]       
            return datetime.strptime(Transformation_1.DEFAULT_VALUES["transmission_date_time"], "%Y-%m-%dT%H:%M:%S.000Z")         
    
    @staticmethod
    def p_transaction_date(transaction_date):
        """ Set transaction_date"""
        # current_year=date.today().year
        # dt = datetime.strftime(f"{current_year}{transaction_date}","%Y%m%d")
        # return dt.strftime("%Y-%m-%d")
        if not transaction_date:
            Transformation_1.log_missing_field("transaction_date")
            return Transformation_1.DEFAULT_VALUES["transaction_date"]
        try:
            current_year=date.today().year
            dt = datetime.strftime(f"{current_year}{transaction_date}","%Y%m%d")
            return dt.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error tranform transaction_date : {transaction_date} - {e}")
            return Transformation_1.DEFAULT_VALUES["transaction_date"]                



    @staticmethod
    def p_is_void(processing_code):
        """ Set is_void """
        if not processing_code:
            Transformation_1.log_missing_field("processing_code")
            return Transformation_1.DEFAULT_VALUES["false"]
        try:
            return "true" if str(processing_code).startswith("02") else "false"
        except ValueError as e:
            logging.error(f"Error transform is_void : {processing_code} - {e}")
            return Transformation_1.DEFAULT_VALUES["false"]
    
    @staticmethod
    def p_is_reversal(message_type):
        if not message_type:
            Transformation_1.log_missing_field("message_type")
            return Transformation_1.DEFAULT_VALUES["false"]
        try:
            return "true" if "reverse" in str(message_type).lower() else "false"
        except ValueError as e:
            logging.error(f"Error trasnform is_reversal : {message_type} - {e}" )
            return Transformation_1.DEFAULT_VALUES["false"]

    
    @staticmethod
    def process_transform_data(data):
        # set start time 
        ingest_timestamp = datetime.now() #.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        transmission_datetime = Transformation_1.p_transmission_date_time(data.get("transmission_date_time"))
        processing_duration_time = (ingest_timestamp - transmission_datetime).total_seconds()
        transmission_datetime_2 = transmission_datetime.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        processing_code = Transformation_1.p_processing_code(data.get("processing_code"))
        message_type = Transformation_1.p_message_type(data.get("message_type"))        
        transform_data = {
                "transaction_amount" : Transformation_1.p_amount_tran(data["amount_tran"]),
                "primary_account_number_masked" : Transformation_1.p_primary_account_number(data["primary_account_number"]),
                "sender_account_number" : Transformation_1.p_sender_account_number(data["sender_account_number"]),
                "beneficiary_account_number_masked" : Transformation_1.p_beneficiary_account_number(data["beneficiary_account_number"]),
                "transmission_date_time" : transmission_datetime_2,
                "ingest_timestamp" : ingest_timestamp.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "processing_duration" : format(processing_duration_time, ".2f"),
                "is_void" : Transformation_1.p_is_void(data["processing_code"]),
                "is_reversal" : Transformation_1.p_is_reversal(data["message_type"]),
                "status" : "COMPLETED",
                "source_system" : "API GATEWAY"

        }
        # transform_data = {      
        #     "ingest_timestamp" : ingest_timestamp.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        # }


        logging.info(f"Tranformed data: {json.dumps(transform_data)}" ) 
        return transform_data

# if __name__ == "__main__":
#     input_data = json.loads(sys.argv[1])
#     transformed_data = Transformation_1.process_transform_data(input_data)
#     print(json.dumps(transformed_data, indent=4))

# if __name__ == "__main__":
#     input_file = "source_1.json"
    
#     if not os.path.exists(input_file):
#         print(f"Error: File {input_file} not found.")
#         sys.exit(1)
    
#     with open(input_file, "r") as f:
#         input_data = json.load(f)
    
#     transformed_data_list = [Transformation_1.process_transform_data(item) for item in input_data]
#     print(json.dumps(transformed_data_list, indent=4))

input_file = sys.argv[1]

if not os.path.exists(input_file):
    print(f"Error: File {input_file} not found.")
    sys.exit(1)

with open(input_file, "r") as f:
    input_data = json.load(f)

transformed_data_list = [Transformation_1.process_transform_data(item) for item in input_data]
print(json.dumps(transformed_data_list, indent=4))